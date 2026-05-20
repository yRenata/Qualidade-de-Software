# Aula 12 – BDD e Automação Orientada a Comportamento

## 👥 Integrantes

- Renata G. Bueno


---

# 🔹 1. Fluxo escolhido

## Integrante: Renata G. Bueno

### Fluxo
Histórico de pedidos

### Objetivo
Validar se os pedidos realizados pelo usuário são exibidos corretamente.

---

# 🔹 2. Cenários BDD

## Arquivo

```text
features/historico_pedidos.feature
```

## Conteúdo

```gherkin
Feature: Histórico de Pedidos

  Scenario: Visualizar histórico de pedidos
    Given que o usuário está logado no sistema
    And possui um pedido realizado
    When acessa a página de histórico de pedidos
    Then os pedidos realizados devem ser exibidos na tela
```

---

# 🔹 3. Automação com pytest-bdd

## Estrutura do projeto

```text
projeto/
│
├── features/
│   └── historico_pedidos.feature
│
├── tests/
│   └── test_historico_pedidos.py
│
├── evidencias/
│
└── README.md
```

---

## Arquivo

```text
tests/test_historico_pedidos.py
```

## Código

```python
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
```

---

# 🔹 4. Execução dos testes

## Comando executado

```bash
pytest -v
```

---

## Resultado

```text
=================== test session starts ===================

9 passed in 18.42s

==========================================================
```

---

# 🔹 5. Evidências

## Print da execução

![alt text](image.png)

## Print da aplicação

![alt text](image-1.png)

---

### Fluxo 2
Favoritar restaurantes

### Objetivo
Validar se o usuário consegue adicionar restaurantes à lista de favoritos corretamente.

---

# 🔹 2. Cenários BDD

## Arquivo

```text
features/favoritos.feature
```

## Conteúdo

```gherkin
Feature: Favoritos

  Scenario: Adicionar restaurante aos favoritos
    Given que o usuário acessa o sistema
    When visualiza os restaurantes disponíveis
    And adiciona um restaurante aos favoritos
    Then o restaurante deve aparecer na lista de favoritos

```

---

# 🔹 3. Automação com pytest-bdd

## Estrutura do projeto

```text
projeto/
│
├── features/
│   └── favoritos.feature
│
├── tests/
│   └── tests/test_favoritos.py
│
├── evidencias/
│
└── README.md
```

---

## Arquivo

```text
tests/test_favoritos.py
```

## Código

```python
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
```
---

# 🔹 4. Execução dos testes

## Comando executado

```bash
pytest -v
```

---

## Resultado

```text
=================== test session starts ===================

9 passed in 18.42s

==========================================================
```

---

# 🔹 5. Evidências

## Print da execução

![alt text](image.png)

## Print da aplicação

![alt text](image.png)

---

# 🔹 6. Análise crítica

## O cenário ficou legível?

Sim. O padrão Given-When-Then deixou o comportamento do sistema mais claro e organizado.

---

## O BDD ajudou a entender o comportamento?

Sim. Mesmo sem analisar o código, foi possível compreender o fluxo do login.

---

## O teste ficou robusto?

Parcialmente. Alguns seletores ainda dependem diretamente da interface visual.

---

## Quais dificuldades surgiram?

- Encontrar seletores corretos
- Resolver conflitos entre elementos da página
- Ajustar o Playwright com pytest-bdd

---

## O teste ficou dependente da interface?

Sim. Alterações no frontend podem impactar o funcionamento da automação.

---

# 🔹 7. Reflexão final

## BDD melhora comunicação entre equipe?

Sim. O comportamento esperado do sistema ficou mais fácil de entender entre desenvolvimento e testes.

---

## Todo teste deve usar BDD?

Não. O BDD é mais útil em funcionalidades principais e fluxos importantes do sistema.

---

## Quando vale a pena usar BDD?

Quando existe necessidade de documentar comportamentos de forma clara e compreensível.

---

## Como isso ajuda no projeto do grupo?

Ajuda a transformar requisitos em cenários automatizados mais organizados e fáceis de manter.

---

# 📦 Repositório GitHub

```text
https://github.com/grupo-exemplo/local-eats-bdd
```

---

# ✅ Conclusão

A atividade permitiu compreender:

- O BDD ajudou a deixar os testes mais organizados e compreensíveis
- Os cenários facilitaram a visualização do comportamento esperado do sistema
- A automação com pytest-bdd deixou os testes mais próximos da linguagem de negócio
- Foi possível perceber a importância de utilizar seletores mais estáveis
- A atividade ajudou a entender melhor a integração entre Playwright, Pytest e BDD