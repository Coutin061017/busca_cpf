"""Automação Selenium sobre uma página de CPFs fictícios de treinamento."""

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_DIR = Path(__file__).resolve().parent
CPF_DE_TESTE = "11111111111"


def abrir_navegador():
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    return navegador


def abrir_pagina(navegador):
    pagina = BASE_DIR / "consulta_cpf.html"
    if not pagina.is_file():
        raise FileNotFoundError(f"Arquivo HTML não encontrado: {pagina}")
    navegador.get(pagina.as_uri())


def consultar_cpf(navegador, cpf):
    campo = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.ID, "cpf"))
    )
    campo.clear()
    campo.send_keys(cpf)
    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.ID, "consultar"))
    ).click()


def obter_resultado(navegador):
    resultado = WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located((By.ID, "registro"))
    )
    return resultado.text


def main():
    navegador = None
    try:
        navegador = abrir_navegador()
        abrir_pagina(navegador)
        consultar_cpf(navegador, CPF_DE_TESTE)
        print("Resultado da consulta fictícia:")
        print(obter_resultado(navegador))
    except Exception as erro:
        print(f"Erro durante o teste automatizado: {erro}")
        return 1
    finally:
        if navegador is not None:
            navegador.quit()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
