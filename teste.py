import webbrowser
import pandas as pd
import selenium
from selenium.webdriver.common.keys import Keys
import time
import urllib


for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    webbrowser.get(link)


contatos_df = pd.read_excel("Enviar.xlsx", engine='openpyxl')

while len(webbrowser.find_elements_by_id("side")) < 1:
    time.sleep(1)