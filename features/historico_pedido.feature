Feature: Histórico de Pedidos

  Scenario: Visualizar histórico de pedidos
    Given que o usuário está logado no sistema
    And possui um pedido realizado
    When acessa a página de histórico de pedidos
    Then os pedidos realizados devem ser exibidos na tela