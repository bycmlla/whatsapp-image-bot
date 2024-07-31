import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def capture_screenshot():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service("C:/Users/camila/AppData/Local/Programs/Python/Python312/chromedriver.exe") # Caminho pro seu driver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = "URL PARA SEU DAHSBOARD"
    driver.get(url)
    time.sleep(20)

    screenshot_path = "CAMINHO DE ONDE VOCÊ IRÁ SALVAR SUA IMAGEM"
    driver.save_screenshot(screenshot_path)

    driver.quit()

    logging.info(f"Screenshot saved in: {screenshot_path}")
    return screenshot_path


def send_whatsapp_message(image_path):
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=C:/Users/seuUser/AppData/Local/Google/Chrome/User Data")
    chrome_options.add_argument("profile-directory=Camila de Carvalho")
    service = Service("C:/Users/seuUser/Documents/screenshots/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        logging.info("Opening WhatsApp Web")
        driver.get("https://web.whatsapp.com/")
        time.sleep(15)

        logging.info("Waiting for WhatsApp Web page to load")
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="textbox" and @data-tab="3"]'))
        )

        logging.info("Searching for the desired chat")
        chat_name = "meu bem"
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="textbox" and @data-tab="3"]'))
        )
        search_box.send_keys(chat_name)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

        logging.info("Attaching the image")
        attach_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span'))
        )
        attach_button.click()

        time.sleep(2)

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
        driver.quit()


def capture_and_send():
    screenshot_path = capture_screenshot()
    send_whatsapp_message(screenshot_path)

# schedule.every().day.at("17:00").do(capture_and_send)

capture_and_send()

while True:
    schedule.run_pending()
    time.sleep(1)
