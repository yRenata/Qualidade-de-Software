class LoginPage:

    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
        self.page.wait_for_load_state("networkidle")

    def realizar_login(self, email, senha):
        self.page.wait_for_selector("#loginEmail")

        self.page.locator("#loginEmail").fill(email)
        self.page.locator("#loginPassword").fill(senha)

        self.page.locator("#loginForm button.primary-btn").click()