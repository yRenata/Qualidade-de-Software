from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect

scenarios('../features/favoritos.feature')


@given('que o usuário acessa o sistema')
def acessar_sistema(page):

    page.goto(
        'https://local-eats-unisenac.vercel.app/static/login.html'
    )

    page.get_by_role('textbox',name='teste@teste.com').fill('teste@gmail.com')

    page.get_by_role('textbox',name='Sua senha secreta').fill('123456789')

    page.locator('#loginForm').get_by_role('button',name='Entrar').click()


@when('visualiza os restaurantes disponíveis')
def visualizar_restaurantes(page):

    restaurante = page.get_by_role('link',name='Restaurante Sabor 3')

    expect(restaurante).to_be_visible()

    restaurante.click()


@when('adiciona um restaurante aos favoritos')
def adicionar_favorito(page):

    favorito = page.get_by_role('button',name=' Favoritar')

    expect(favorito).to_be_visible()

    favorito.click()


@then('o restaurante deve aparecer na lista de favoritos')
def validar_favorito(page):

    favoritos = page.get_by_role('link',name='Meus Favoritos')

    favoritos.click()

    expect(page.locator('body')).to_contain_text('Restaurante Sabor 3')