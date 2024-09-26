from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.common.keys import Keys
import shutil
import os
from pywinauto import Application, timings
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
prefs = {
    "profile.default_content_setting_values.notifications": 2  # 2 bloqueia notificações
}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.bandlab.com/library/projects/my-projects')
sleep(2)
driver.maximize_window()

# Entrada do Usuario
usuario = driver.find_element(By.XPATH,"//input[@placeholder='Nome de usuário ou e-mail']")
sleep(0.5)
usuario.click()
usuario.send_keys('aghastvirus47@gmail.com')
sleep(0.5)
# Entrada da Senha
senha = driver.find_element(By.XPATH,"//input[@placeholder='Insira ao menos 6 caracteres']")
sleep(0.5)
senha.click()
senha.send_keys('7355608n')
sleep(0.5)
# Clique em entrar
entrar = driver.find_element(By.XPATH, "//button[@class='button-dark button-height-40 button-rounded button-padding-fill']")
entrar.click()
sleep(4)

# Try verificando se existe o botao "entendi", caso exista ele clica, caso não, ele ignora
try:
    botao_entendi = driver.find_element(By.XPATH, "//button[@class='ds-button ds-button-primary ds-button-medium ds-button-padding-default']")
    botao_entendi.click()
except:
    print('O elemento não existe')
sleep(0.5)

# Define os links onde estão as musicas
links = driver.find_elements(By.XPATH, '//a[@ng-href]')
#Define suas urls 'song/valor'
urls = set([link.get_attribute('ng-href') for link in links])
#Para cada URL tirada acima, coloca numa lista 'i', enumera ''enumerate'' e depois entra em cada link
for i, url in enumerate(urls):
    print(f'Entrando na música número {i+1}: {url}')
    #Como o URL gerado é relativo, se cria um caminho para acessar ele completo
    url_completo = 'https://www.bandlab.com' + url
    driver.get(url_completo)
    sleep(5)
    #Clica no botão de download para baixar a música
    baixar = driver.find_element(By.XPATH, "//div[@ng-if='data.canDownload.value']")
    baixar.click()
    sleep(2)
    #Define o XPATH de cada elemento button
    botao_download = driver.find_elements(By.XPATH,"//button[@ng-click='mixdown.id = file.id']")
    # Define o elemento Button que vai ser clicado, no caso o botao mp3 que está em segundo lugar
    if len(botao_download) >= 2:
        download_mp3 = botao_download[1]
        download_mp3.click()
        sleep(35)
    # Fechar janela de Download
    fechar = driver.find_element(By.XPATH, "//div[@class='modal-close']")
    fechar.click()
    sleep(1)
    #Define as pastas de origem e Destino
    caminho_origem = os.path.expanduser("C:/Users/aghas/Downloads")
    caminho_destino = os.path.expanduser("C:/Users/aghas/Desktop/Freelancer/Selenium/Musicas/MusicasMp3")

    #Lista os arquivos na pasta de origem
    for arquivo in os.listdir(caminho_origem):
         if arquivo.endswith(".mp3"): #verifica se o arquivo é '.mp3'
            caminho_arquivo = os.path.join(caminho_origem, arquivo) # Define de onde será tirado o arquivo original e o nome dele
            shutil.move(caminho_arquivo, caminho_destino) # Move o arquivo definido acima para a pasta de destino
driver.close()
sleep(5)


input('Digite enter para fechar')
