# Aula 6 – Planejamento e Execução de Testes

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrantes do grupo:  
> - Renata G. Bueno


---

# 1. Plano de Testes

## 1.1 Objetivo
Descreva o objetivo do plano de testes.

> Exemplo: Validar as principais funcionalidades do sistema LocalEats, garantindo que atendam aos requisitos esperados e apresentem comportamento consistente.

---

## 1.2 Escopo

### O que será testado
- [Validação do fluxo de Login]
- [Inclusão de restaurantes na lista de Favoritos]
- [Vizualizar Fluxo do Histórico de Pedidos]
- [Fluxo de Compra]
- [Pesquisar restaurante]


### O que NÃO será testado
- [Integração com sistemas externos]
- [Outros itens fora do escopo]

---

## 1.3 Funcionalidades selecionadas
Liste as funcionalidades que serão foco dos testes:

- [Login]
- [Favoritos]
- [Meus Pedidos]
- [Busca]

---

## 1.4 Estratégia de Testes

Descreva como os testes serão realizados.

- Tipos de teste:
  - (X) Funcional
  - (X) Usabilidade
  - ( ) Outros: _______

- Abordagem:
  > Testes manuais baseados em cenários de uso reais.

---

## 1.5 Responsáveis

Defina os papéis na equipe:

| Nome | Responsabilidade |
|------|----------------|
| Renata G. Bueno     | Tester/QA              |
|      |                |

---

# 2. Casos de Teste

Crie no mínimo 5 casos de teste.

---

## CT-01 – [Login]

**Pré-condição:**  
[O aplicativo deve estar na tela de login e o usuário deve possuir cadastro ativo.]

**Passos:**  
1. Inserir um e-mail válido e cadastrado.
2. Inserir a senha correta.
3. Clicar no botão "Entrar".
 

**Dados de entrada (se aplicável):**  
[Email:Renata.buenog@gmail.com]
[Senha:*********]

**Resultado esperado:**  
[O usuário é autenticado e o sistema o redireciona para a tela principal (Home).]

---

## CT-02 – [Adicionar Restaurante aos Favoritos]

**Pré-condição:**  
Usuário autenticado no sistema (CT-01 realizado) e posicionado na listagem de restaurantes.

**Passos:**  
1. Clicar no ícone de coração (vazio). 
2. Navegar até a aba "Favoritos".
3.  

**Dados de entrada (se aplicável):** 
[Clique no ícone do restaurante Restaurante Sabor3.] 

**Resultado esperado:**  
[Deve mostrar todos os restaurantes adicionado aos Favoritos.]

---

## CT-03 – [Visualizar Histórico de Pedidos Anteriores]

**Pré-condição:**
[Usuário autenticado, possuindo compras concluídas no histórico da conta.]  

**Passos:**  
1. Acessar menu superior e clicar em "Meus Pedidos".
2. Verificar a ordenação cronológica e clicar em um pedido específico para ver os detalhes.

**Dados de entrada (se aplicável):**  

**Resultado esperado:**  
[A listagem exibe todos os pedidos do mais recente ao mais antigo.]

---

## CT-04 – [Adicionar Item ao Carrinho e Finalizar Pedido]

**Pré-condição:**  
[O usuário deve estar autenticado no sistema e posicionado na tela do cardápio de um restaurante parceiro.]

**Passos:**  
1. Selecionar o item desejado e clicar no botão "Adicionar".
2. Conferir os itens e clicar em "Finalizar".
3. Logo após clicar em Ver Detalhes.

**Dados de entrada (se aplicável):**  

**Resultado esperado:**
[O pedido é processado e gerado com sucesso. O sistema limpa o carrinho.]

---

## CT-05 – [O usuário deve estar na tela principal do LocalEats, onde a barra de pesquisa está visível.]

**Pré-condição:** 
[O usuário deve estar na tela principal (Home) do LocalEats, onde a barra de pesquisa está visível.]

**Passos:**  
1. Tocar na barra de pesquisa localizada no topo da tela. 
2. Digitar o nome exato de um restaurante que está cadastrado na plataforma.
3. Clicar no ícone de lupa ou pressionar "Buscar" no teclado do dispositivo.

**Dados de entrada (se aplicável):**  
[Buscar: Restaurante Sabor3]

**Resultado esperado:** 
[O sistema filtra a listagem geral instantaneamente e renderiza na tela apenas o card correspondente à "Restaurante Sabor3".]

---

# 3. Execução dos Testes

Preencha a tabela com os resultados obtidos.

| ID     | Resultado (Passou/Falhou) | Evidência (descrição ou print) |
|--------|--------------------------|--------------------------------|
| CT-01  |        PASSOU            | ![alt text](image.png)         |
| CT-02  |        PASSOU            | ![alt text](image.png) ![alt text](image-1.png) |
| CT-03  |        FALHOU            | ![alt text](image.png) ![alt text](image-1.png) |
| CT-04  |        FALHOU            | ![alt text](image.png) ![alt text](image-1.png) ![alt text](image-2.png) |
| CT-05  |        FALHOU            | ![alt text](image-3.png) |

---

# 4. Análise dos Resultados

- Quantidade de testes executados: 5
- Quantidade de testes que passaram: 2  
- Quantidade de testes que falharam: 3  

## Principais problemas encontrados
- [Falha na ordem cronológica no Histórico de Pedidos (CT-03)]
- [Interrupção no fluxo de atualização do status do pedido estando sempre Pendente (CT-04)]
- [Falha no mecanismo de filtragem da Busca [CT-05]]

---

# 5. Reflexão

Responda às questões abaixo:

- O plano de testes ajudou a organizar melhor o processo? Por quê?
Sim. Ele evitou testes aleatórios ao definir pré-condições, dados exatos de entrada e resultados esperados.

- Algum problema só foi identificado durante a execução? Explique.
Sim, todos os três bugs. Visualmente as telas pareciam certas, mas o pedido travado em "Pendente" (CT-04), a busca sem resultados (CT-05) e o histórico bagunçado (CT-03) só apareceram ao rodar os cenários na prática.

- O que o grupo melhoraria no processo de testes?
Adotar testes automatizados para acelerar os retestes após as correções dos desenvolvedores, reduz o trabalho manual.

---

## Conclusão

O comportamento do sistema foi considerado insatisfatório. Embora o login funcione, o aplicativo falha nas funções centrais de um delivery: o usuário não consegue buscar restaurantes, o pedido fica preso e o histórico fica desordenado.

---

# 6. Conclusão Geral

Faça um resumo final:

- Qualidade geral do sistema testado:
Parcialmente funcional. O aplicativo se mostra seguro e estável para navegação básica e acessos, mas falha nas regras essenciais que envolvem persistência e requisições externas.

- Principais pontos positivos:
Excelente tempo de resposta na alternância de telas e ótimo gerenciamento do estado de login.

- Principais problemas identificados:
Quebra de fluxo na resposta assíncrona da API de pedidos e falha de comunicação entre o input de texto e a consulta do banco de dados na busca.

- Impressão geral do grupo sobre o processo de testes:
Ficou evidente que o processo de validação serve justamente para alinhar a expectativa da especificação técnica com a realidade da experiência prática antes do produto chegar ao cliente final.