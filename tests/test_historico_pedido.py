import re
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect

scenarios('../features/historico_pedido.feature')


@given('que o usuário está logado no sistema')
def login(page):

    page.goto(
        'https://local-eats-unisenac.vercel.app/static/login.html'
    )

    page.get_by_role('textbox',name='teste@teste.com').fill('teste@gmail.com')

    page.get_by_role('textbox',name='Sua senha secreta').fill('123456789')

    page.locator("#loginForm").get_by_role('button',name='Entrar').click()

    page.wait_for_load_state('networkidle')


@given('possui um pedido realizado')
def criar_pedido(page):

    page.get_by_role('link',name='Restaurante Sabor 3').click()

    page.wait_for_load_state('networkidle')

    adicionar = page.get_by_role('button',name=' Adicionar').first

    expect(adicionar).to_be_visible()

    adicionar.click()

    page.wait_for_timeout(2000)

    finalizar = page.get_by_role('button',name='Finalizar Pedido')

    expect(finalizar).to_be_visible()

    finalizar.click()

    page.wait_for_timeout(3000)

    page.goto('https://local-eats-unisenac.vercel.app/static/orders.html')
    page.wait_for_load_state('networkidle')


@when('acessa a página de histórico de pedidos')
def acessar_historico(page):
    expect(page).to_have_url(re.compile(r'.*orders\.html'))


@then('os pedidos realizados devem ser exibidos na tela')
def validar_pedidos(page):
    expect(page.locator('#ordersList')).to_be_visible()
    expect(page.get_by_text('Pedido').first).to_be_visible(timeout=10000)