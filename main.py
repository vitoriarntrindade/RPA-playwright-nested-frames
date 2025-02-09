from playwright.sync_api import sync_playwright

URL = "https://the-internet.herokuapp.com/nested_frames"


def extract_iframe_text():
    """
    Acessa a página com iframes aninhados e extrai o conteúdo de cada um deles.

    O script realiza as seguintes etapas:
    1. Inicializa o navegador usando Playwright.
    2. Carrega a página especificada pela URL.
    3. Identifica todos os iframes presentes na página.
    4. Para cada iframe:
       - Verifica se contém um elemento <body> acessível.
       - Se sim, extrai e imprime seu conteúdo.
       - Se não, exibe uma mensagem informando a inacessibilidade.
    5. Fecha o navegador após a extração.

    Iframes que possuem apenas um <frameset> (como "frame-top") não contêm <body>,
    e por isso não podem ser acessados diretamente.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)

        frames = page.frames
        print(f"\n🔍 {len(frames)} iframes encontrados!\n")

        for frame in frames:
            try:
                body = frame.locator("body")
                if body.count() > 0:
                    body_content = body.inner_text()
                    print(f"\nConteúdo do iframe '{frame.name}':\n{body_content or '(iframe vazio)'}")
                else:
                    print(f"\nIframe '{frame.name}' não tem um <body> acessível.")
            except Exception as e:
                print(f"\nErro ao acessar o iframe '{frame.name}': {str(e)}")

        browser.close()


if __name__ == "__main__":
    extract_iframe_text()