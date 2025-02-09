# 🚀 Playwright Iframe Scraper


### 📌 Sobre o Projeto

Este script automatiza a extração de conteúdo de iframes aninhados usando Playwright. Ele acessa página do site Nested
Frames, 
identifica os iframes disponíveis e imprime o conteúdo de cada um.

🎯 Funcionalidades

✅ Identifica automaticamente todos os iframes na página.

✅ Extrai e imprime o conteúdo do <body> de cada iframe.

✅ Ignora iframes sem <body> ou inacessíveis.

✅ Trata exceções para evitar falhas durante a execução.

✅ Código modular e bem documentado.

### 🛠️ Tecnologias Utilizadas

- Python 3 🐍

- Playwright 🌐

- Git e GitHub 🛠️

#### 📂 Estrutura do Projeto

📁 playwright-iframe-scraper

│── 📜 main.py  # Script principal

│── 📜 README.md  # Documentação do projeto

│── 📜 requirements.txt  # Dependências

### 🚀 Como Executar o Script

🔧 1️⃣ Instale as dependências

```
    pip install -r requirements.txt
```

▶️ 2️⃣ Execute o script

```
    python playwright_iframe_scraper.py
``` 

### 📝 Exemplo de Saída no Terminal

- 🔍 5 iframes encontrados!

- Conteúdo do iframe 'frame-left':
LEFT

- Conteúdo do iframe 'frame-middle':
MIDDLE

- Conteúdo do iframe 'frame-right':
RIGHT

- Conteúdo do iframe 'frame-bottom':
BOTTOM

