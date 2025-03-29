from playwright.sync_api import sync_playwright

#Teste de automação para criar uma nota no Anotepad
def test_criar_nota():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://pt.anotepad.com/")

        page.wait_for_selector("input#edit_title")
        page.fill("input#edit_title", "Entrega trabalho TEST DAS 2024")
        page.fill("textarea#edit_textarea", "Nome: Thayná Schleider de Matos\nMatrícula: 40001016398E1")

        page.locator("#btnSaveNote").scroll_into_view_if_needed()
        page.locator("#btnSaveNote").click()

        page.wait_for_timeout(3000)  

        # Verifica se a nota foi criada com sucesso
        assert "pt.anotepad.com/notes/" in page.url or page.locator("text=Nota salva").is_visible()

        browser.close()
