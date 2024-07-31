# Python

# Automatização de Mensagens Whatsapp

Como enviar mensagens de maneira automática utilizando o Python.

**IMPORTANTE:** Esse procedimento que será ensinado tem objetivo **educacional**. Então é muito importante estar ciente disso, pois o whatsapp **não** gosta de automações e pode dar problema. Pode ter seu número bloqueado dependendo da forma que for utilizado. 

Outro ponto: neste código, ele realiza o envio de imagens a partir de um determinado diretório, mas também é possível realizar o envio de mensagens de texto mudando alguns parâmetros.

Para isso estaremos utilizando a biblioteca `Selenium Python` que faz a interação entre o navegador e o Python, e o `Webdriver` do Google Chrome. O Webdriver é a aplicação que controla os navegadores de forma automatizada. Inclusive utiliza aplicações nativas para diminuir problemas e interferências com as linguagens e tecnologias usadas nos sites.

Primeiro, é necessário de uma IDE para compilar o seu código. Estou utilizando o [Pycharm](https://www.jetbrains.com/pycharm/download/?section=windows), mas é de plena escolha do desenvolvedor. 

Depois, instale o Chrome WebDriver, garantindo que ele esteja na mesma versão do seu navegador. A versão que estou utilizando é a 127.0.6533.74. 

No link abaixo, você encontrará várias versões disponíveis do WebDriver. Baixe o arquivo correspondente à versão do seu navegador, extraia o executável e coloque-o no mesmo diretório onde o Python está instalado em seu computador.

![Untitled](Python%2054276011384c498eb9c7a848bd5726af/Untitled.png)

https://googlechromelabs.github.io/chrome-for-testing/

Clique duas vezes no executável para instalar. Após ver a mensagem de confirmação, siga para a próxima etapa.

![Untitled](Python%2054276011384c498eb9c7a848bd5726af/Untitled%201.png)

Instale o `Selenium` utilizando o comando:

```jsx
pip install selenium
```

Código:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

```

Estas importações são necessárias para configurar e usar o Selenium WebDriver para interagir com o WhatsApp Web.

```python
chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:/Caminho_para_seu_usuário/Users/")
chrome_options.add_argument("profile-directory=Camila de Carvalho")
service = Service("C:/Caminho_para_o_webdriver/chromedriver-win64/chromedriver.exe")driver = webdriver.Chrome(service=service, options=chrome_options)
```

Estas linhas configuram o WebDriver para usar o perfil do usuário existente do Chrome, onde as informações de login do WhatsApp Web já estão armazenadas, evitando assim a necessidade de login toda vez.

```python
try:
    logging.info("Opening WhatsApp Web")
    driver.get("https://web.whatsapp.com/")
    time.sleep(15)

```

- `driver.get(...)`: Abre o WhatsApp Web.
- `time.sleep(15)`: Aguarda 15 segundos para que a página carregue.

```python
logging.info("Searching for the desired chat")
chat_name = "Nome Contato"
search_box = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//div[@role="textbox" and @data-tab="3"]'))
)
search_box.send_keys(chat_name)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

```

Digita o nome do chat desejado na caixa de pesquisa. Pressiona a tecla Enter para selecionar o chat.

```python
logging.info("Attaching the image")
attach_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span'))
)
attach_button.click()
time.sleep(2)
```

Clica no botão de anexo para abrir a opção de envio de arquivos. Insere o caminho da imagem no campo de input de arquivo para anexar a imagem ao chat.

```python
logging.info("Sending the image")
send_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]'))
)
send_button.click()
logging.info("Image sent successfully!")
time.sleep(5)
driver.quit()
```

Clica no botão de envio para mandar a imagem no chat. Fecha o WebDriver após o envio da imagem.

```python
except Exception as e:
    logging.error(f"An error has occurred: {e}")
    driver.quit()
```

Captura qualquer exceção que ocorra durante o processo e registra uma mensagem de erro no log.

Esta função, quando chamada, realiza os seguintes passos:

1. Configura e inicializa o WebDriver.
2. Abre o WhatsApp Web e aguarda o carregamento completo.
3. Pesquisa pelo chat desejado.
4. Anexa a imagem ao chat.
5. Envia a imagem.
6. Fecha o WebDriver.
