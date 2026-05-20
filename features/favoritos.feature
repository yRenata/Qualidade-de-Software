Feature: Favoritos

  Scenario: Adicionar restaurante aos favoritos
    Given que o usuário acessa o sistema
    When visualiza os restaurantes disponíveis
    And adiciona um restaurante aos favoritos
    Then o restaurante deve aparecer na lista de favoritos