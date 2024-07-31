from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

chrome_options = Options()
chrome_options.add_argument(
    "user-data-dir=C:/Users/camila.aguiar/AppData/Local/Google/Chrome/User Data"
)
chrome_options.add_argument("profile-directory=Camila de Carvalho")
service = Service(
    "C:/Users/camila.aguiar/Documents/screenshots/chromedriver-win64/chromedriver.exe"
)
driver = webdriver.Chrome(service=service, options=chrome_options)


def send_whatsapp_message():
    try:
        logging.info("opening the WhatsApp Web")
        driver.get("https://web.whatsapp.com/")
        time.sleep(15)

        logging.info("Waiting for WhatsApp Web page to load")
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@role="textbox" and @data-tab="3"]')
            )
        )

        logging.info("Searching for the desired chat")
        chat_name = "Yasmin Oliveira La Monica"
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@role="textbox" and @data-tab="3"]')
            )
        )
        search_box.send_keys(chat_name)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

        logging.info("Attaching the image")
        attach_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span',
                )
            )
        )
        attach_button.click()

        time.sleep(2)

        image_path = "C:/Users/camila.aguiar/Documents/screenshots/Screenshot.png"
        logging.info(f"Using the image path: {image_path}")

        image_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
        )
        image_input.send_keys(image_path)
        time.sleep(2)

        logging.info("Sending the image")
        send_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]'))
        )
        send_button.click()

        logging.info("Image sent successfully!")

        time.sleep(5)
        driver.quit()

    except Exception as e:
        logging.error(f"An error has occurred: {e}")


# schedule.every().day.at("17:00").do(send_whatsapp_message)
send_whatsapp_message()

while True:
    schedule.run_pending()
    time.sleep(1)
