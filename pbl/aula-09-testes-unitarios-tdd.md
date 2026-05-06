t# Aula 9 – Testes Unitários e TDD

## 👥 Integrantes
- Renata G. Bueno

---

## 📁 Estrutura do Projeto

.  
├── src/  
│   ├── pedido.py  
│   ├── desconto.py  
│   └── entrega.py  
└── tests/  
    ├── test_pedido.py  
    ├── test_desconto.py  
    └── test_entrega.py  

---

## 🔹 1. Funcionalidades escolhidas

Cada integrante ficou responsável por uma regra de negócio do sistema.

---

### 👤 Integrante 1 – Cálculo do total do pedido com valor mínimo

**Arquivo da implementação:** `/src/pedido.py`  
**Arquivo de testes:** `/tests/test_pedido.py`

#### Descrição
Soma os valores dos itens do pedido e valida se o total atinge o valor mínimo.

#### Regras de negócio
- Soma dos itens define o total  
- Pedido deve atingir valor mínimo  
- Caso contrário, deve gerar erro  

---

### 👤 Integrante 2 – Aplicação de desconto percentual

**Arquivo da implementação:** `/src/desconto.py`  
**Arquivo de testes:** `/tests/test_desconto.py`

#### Descrição
Aplica um desconto percentual sobre o valor total do pedido.

#### Regras de negócio
- Percentual deve estar entre 0 e 100  
- Valor final não pode ser negativo  

---

### 👤 Integrante 3 – Cálculo de taxa de entrega

**Arquivo da implementação:** `/src/entrega.py`  
**Arquivo de testes:** `/tests/test_entrega.py`

#### Descrição
Calcula a taxa de entrega com base na distância.

#### Regras de negócio
- Até 3km → taxa fixa  
- Acima de 3km → taxa adicional por km  
- Distância negativa → erro  

---

## 🔹 2. Testes Unitários

Cada integrante implementou seus testes unitários no respectivo arquivo dentro da pasta `/tests`.

---

### 🧪 Integrante 1 – Testes (pedido)
Foram criados testes para validar cenários principais, incluindo casos limite como valores zero, valores altos e situações de erro.

#### Teste 1 – Valor acima do mínimo
Para rodar os testes copie e cole: pytest tests/test_pedido.py

- Nome: calcular_total_quando_valor_minimo_atingido
- Cenário: pedido com valor maior ou igual ao mínimo
- Entrada: itens = [10, 20], valor_minimo = 15
- Resultado esperado: retornar 30 

##### TDD
- Red: Primeiro escrevi o teste, mas ele falhou porque a função ainda não existia.  
![alt text](image-5.png)
![alt text](image.png)
- Green: Fiz primeiro a versão mais simples possível, só somando os valores pra fazer o teste passar.  
![alt text](image-2.png)
![alt text](image-1.png)
- Refactor: Depois melhorei o código adicionando a validação do valor mínimo e tratamento de erro, garantindo que a regra de negócio fosse atendida.
![alt text](image-3.png)

##### Refatoração
- Melhoria nos nomes das variáveis para maior clareza 
- Organização da função
- Inclusão da validação do valor mínimo
- Código mais simples e legível   

##### Execução
- Resultado: Passou  

---

#### Teste 2 – Valor abaixo do mínimo
Para rodar os testes copie e cole: pytest tests/test_pedido.py

- Nome: test_deve_gerar_erro_quando_valor_minimo_nao_atingido  
- Cenário: pedido com valor abaixo do mínimo  
- Entrada: itens = [5, 5], valor_minimo = 20  
- Resultado esperado: gerar erro    

##### TDD
-  Red: O teste foi criado esperando erro, mas inicialmente falhou pois a função não tratava o caso de valor abaixo do mínimo.
![alt text](image.png)
![alt text](image-1.png)
- Green: Adicionei uma validação simples para lançar exceção quando o valor mínimo não é atingido, fazendo o teste passar.
![alt text](image-2.png)
![alt text](image-3.png)
- Refactor: O código foi melhorado para tratar melhor entradas inválidas e ficar mais organizado, mantendo os testes passando.
![alt text](image-4.png)

##### Refatoração
- Inclusão de tratamento de erro  
- Código mais robusto  

##### Execução
- Resultado: Passou  


#### Teste 3 – Valor igual ao minímo
Para rodar os testes copie e cole: pytest tests/test_pedido.py

- Nome: test_deve_aceitar_valor_igual_ao_minimo  
- Cenário: pedido com valor igual ao mínimo  
- Entrada: itens = [10, 5], valor_minimo = 15  
- Resultado esperado: retornar 15  

##### TDD
- Red: O teste foi criado para aceitar valores iguais ao mínimo, mas inicialmente falhou porque a validação estava incorreta (tratando como erro).
![alt text](image-6.png)
![alt text](image-7.png)
- Green:  Ajustei a condição para permitir valores iguais ao mínimo, fazendo o teste passar.
![alt text](image-8.png)
![alt text](image-9.png)
- Refactor: Melhorei a legibilidade da validação, deixando a regra mais clara sem alterar o comportamento. 
![alt text](image-10.png)

##### Refatoração
- Ajuste da condição de validação  
- Melhoria na leitura da lógica  

##### Execução
- Resultado: Passou  

---

### 🧪 Integrante 2 – Testes (desconto)

#### Teste 1 – Aplicação de desconto válido

- Cenário: Desconto dentro do limite  
- Resultado esperado: Valor reduzido corretamente  

##### TDD
- Red: falha inicial  
- Green: cálculo simples  
- Refactor: validação de percentual  

##### Refatoração
- Garantia de limites do desconto  

##### Execução
- Resultado: Passou  

---

#### Teste 2 – Percentual inválido

- Cenário: Desconto maior que 100%  
- Resultado esperado: Erro  

##### TDD
- Red: falha  
- Green: validação adicionada  
- Refactor: melhoria da mensagem de erro  

##### Refatoração
- Tratamento de entrada inválida  

##### Execução
- Resultado: Passou  

---

### 🧪 Integrante 3 – Testes (entrega)

#### Teste 1 – Distância até 3km

- Cenário: Taxa fixa  
- Resultado esperado: Valor fixo  

##### TDD
- Red: falha inicial  
- Green: retorno fixo  
- Refactor: lógica condicional  

##### Refatoração
- Inclusão de regra de distância  

##### Execução
- Resultado: Passou  

---

#### Teste 2 – Distância negativa

- Cenário: Entrada inválida  
- Resultado esperado: Erro  

##### TDD
- Red: falha  
- Green: validação implementada  
- Refactor: melhoria da estrutura  

##### Refatoração
- Garantia de integridade dos dados  

##### Execução
- Resultado: Passou  

---

## 🔹 3. Reflexão

### Foi difícil escrever testes antes do código?
Sim, no começo é meio estranho porque a gente sempre faz o código primeiro, mas depois começa a fazer mais sentido

---

### O TDD ajudou no desenvolvimento?
Sim, ajudou a pensar melhor na lógica antes de implementar e evitar erros.

---

### Os testes aumentaram a confiança no código?
Sim, porque dá mais segurança pra alterar o código sem quebrar tudo.

---

### O que melhorariam?
- Criaria mais testes, principalmente de casos diferentes.
- Organizaria melhor alguns testes.

---

### Como isso ajuda no projeto?
Ajuda a garantir que as regras do sistema estão funcionando e evita problemas quando o código for alterado.