# Automação de consulta de CPF — Selenium (ambiente de treinamento)

Projeto de estudo que utiliza **Python e Selenium WebDriver** para automatizar uma consulta em uma página HTML local com registros **fictícios**. Não acessa bases governamentais nem consulta CPFs reais.

## Objetivo

Demonstrar uma automação de navegador com etapas bem definidas:

1. Abrir o Google Chrome.
2. Carregar `consulta_cpf.html` a partir da pasta do projeto.
3. Informar um CPF de teste no formulário.
4. Clicar no botão **Consultar**.
5. Aguardar o resultado com `WebDriverWait` e mostrar o texto no terminal.
6. Encerrar o navegador, inclusive em caso de erro.

O HTML contém dados de treinamento e um pequeno atraso proposital para exercitar **esperas explícitas**.

## Tecnologias

- Python
- Selenium WebDriver
- HTML, CSS e JavaScript
- Google Chrome

## Arquivos

```text
busca_cpf/
├── consulta_cpf.py     # script principal com Selenium
├── consulta_cpf.html   # página local de treinamento
├── consulta_cpf.ipynb  # notebook de estudo
└── README.md
```

## Como executar

Requisitos: Python instalado e navegador Google Chrome disponível.

```powershell
git clone https://github.com/Coutin061017/busca_cpf.git
cd busca_cpf
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install selenium
python consulta_cpf.py
```

O exemplo do script usa o CPF **11111111111**, presente apenas na base fictícia do arquivo HTML. Em instalações recentes, o Selenium Manager normalmente ajuda a localizar ou preparar o driver compatível.

## O que aprendi

- Automatizar o navegador com Selenium.
- Localizar elementos por `id`.
- Usar `WebDriverWait` e condições de espera.
- Separar a automação em funções e liberar o navegador com `try/finally`.

## Observações

Este repositório é **uma demonstração educacional**, não um serviço de consulta real. Não utilize informações pessoais reais para testar o formulário.

**Autor:** [André Coutinho](https://github.com/Coutin061017)
