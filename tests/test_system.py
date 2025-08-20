import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_cadastro_sucesso(driver):
    driver.get(
        "D:\ETEC - ORGANIZAÇÃO\QTS - Proposta em Andamento\SeleniumTesteSistema\index.html")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.find_element(By.ID, "nome").send_keys("João Silva")
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("joao@teste.com")
    time.sleep(1)

    driver.find_element(By.ID, "termos").click()
    time.sleep(1)

    driver.find_element(By.ID, "btn-enviar").click()
    time.sleep(1)

    mensagem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "mensagem"))
    )

    # Processamento...

    time.sleep(1)
    assert mensagem.text == "Cadastro realizado com sucesso!"
    time.sleep(3)


def test_cadastro_falha(driver):
    driver.get(
        "D:\ETEC - ORGANIZAÇÃO\QTS - Proposta em Andamento\SeleniumTesteSistema\index.html")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.find_element(By.ID, "nome").send_keys("Maria")
    time.sleep(1)

    driver.find_element(By.ID, "btn-enviar").click()
    time.sleep(1)

    mensagem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "mensagem"))
    )
    time.sleep(1)
    assert mensagem.text == "Preencha todos os campos e aceite os termos."
    time.sleep(3)
