from pages.login_page import LoginPage

def test_login(page):
    login = LoginPage(page)

    login.acessar()
    login.realizar_login("teste@email.com", "123456")

    page.wait_for_timeout(2000)

    assert page.locator("text=Bem-vindo").is_visible()