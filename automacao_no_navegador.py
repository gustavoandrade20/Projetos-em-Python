from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


navegador = webdriver.Chrome()

navegador.maximize_window()

navegador.get("https://www.hashtagtreinamentos.com/curso-python?utm_source=site&utm_medium=header&utm_content=link-header-cursos&utm_campaign=programacao&conversion=lpy22-abr-25")

navegador.maximize_window()


navegador.find_element("id", "firstname").send_keys("Gustavo")
navegador.find_element("id", "email").send_keys("gugusdbsekjheu@gmail.com")
navegador.find_element("id", "phone").send_keys("2199999999")

boatao_quero_clicar = navegador.find_element("id", "_form_2475_submit")

navegador.execute_script("arguments[0].scrollIntoView()",
                         boatao_quero_clicar)


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

espera = WebDriverWait(navegador, 10)
espera.until(EC.element_to_be_clickable(boatao_quero_clicar))

boatao_quero_clicar.click()
sleep(10)