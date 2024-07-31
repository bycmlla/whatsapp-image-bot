import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument(
    "--headless"
)


service = Service(
    "C:/Users/camila/AppData/Local/Programs/Python/Python312/chromedriver.exe"
)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abre a página web
url = "URL PARA SEU DASHBOARD"
driver.get(url)
time.sleep(20)
# Tira a captura de tela
screenshot_path = "Screenshot.png"
driver.save_screenshot(screenshot_path)

# Fecha o navegador
driver.quit()

print(f"Screenshot saved in:{screenshot_path}")
