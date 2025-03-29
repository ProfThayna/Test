from playwright.sync_api import sync_playwright

def criar_nota():
    with sync_playwright() as p:
        # Inicia o navegador
        navegador = p.chromium.launch(headless=False)
        pagina = navegador.new_page()
        # Abrir aNotepad
        pagina.goto("https://pt.anotepad.com/", timeout=60000)

        # Espera os campos principais aparecerem
        pagina.wait_for_selector("input#edit_title")
        pagina.wait_for_selector("textarea#edit_textarea")

        pagina.fill('input#edit_title', 'Entrega trabalho TEST DAS 2024')

        conteudo = 'Nome: Thayná Schleider de Matos\nMatrícula: 40001016398E1'
        pagina.fill('textarea#edit_textarea', conteudo)

        # Salva a nota
        pagina.locator("#btnSaveNote").scroll_into_view_if_needed()
        pagina.locator("#btnSaveNote").click()

        # Fecha o navegador após 5 segundos
        pagina.wait_for_timeout(5000)
        navegador.close()

# Executa a função
criar_nota()

