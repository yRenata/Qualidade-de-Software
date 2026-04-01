# 🧪 Aula 5 – Testes Funcionais vs Estruturais  
## LocalEats

---

## 👥 Integrantes do Grupo
- Renata G. Bueno

---

## 🎯 1. Funcionalidade escolhida

**Funcionalidade selecionada:**  
Favoritos

**Descrição da funcionalidade:**  
O sistema permite que o usuário favorite seus restaurantes preferidos.

**O que o usuário espera:**  
O usuário espera que ao clicar no ícone de favoritos o restaurante seja salvo instantaneamente e que a lista dos favoritos seja persistente.

---

## 🔍 2. Testes Caixa-Preta (Visão do Usuário)

**Quais testes vocês fariam sem conhecer o código?**

### 🔹 Cenários de teste

- Cenário 1:  
  *Adicionar aos Favoritos*: Clicar no ícone de (coração) em um restaurante da lista.
  *Esperado*: O ícone muda de cor/estado e o restaurante deve aparecer na aba favoritos.

- Cenário 2: 
    *Remover dos Favoritos*: Ao clicar no ícone de favorito em um restaurante já marcado.
    *Esperado*: O ícone deve ficar "vazio" e o restaurante deve sumir da aba favoritos.

- Cenário 3:  
    *Login Off*: Tentar favoritar um restaurante sem estar logado no sistema.
    *Esperado*: O sistema deve redirecionar para a aba de login ou exibir uma mensagem informativa.

- Cenário 4:  
    *Double click*: Tentar favoritar o mesmo restaurante diversas vezes rapidamente.
    *Esperado*: O sistema deve processar uma ação evitando duplicidade.

---

### 🔹 Possíveis erros identificados

-  Inconsistência na lista de favoritos (restaurante aparece sem ter sido favoritado).
-  Ícone de favorito não atualiza após o clique.
-  Lentidão ao adicionar/remover favoritos.
- Falha ao persistir dados após atualizar página.

---

## 🔧 3. Testes Caixa-Branca (Visão do Sistema)

**Como essa funcionalidade poderia estar implementada internamente?**

### 🔹 Lógica hipotética (pseudo-código ou descrição)

```pseudo
Funcao alternarStatusFavoritos(idUsuario, idRestaurante){

    Se (idUsuario == NULL) {
            DispararErro("Usuário não autenticado")
    }

    Tentar {
        Se (favorito != NULL) {
            Banco.Favoritos.deletar(favorito.id)

            Retornar "Restaurante Removido com sucesso!"
        } Senão {
            Banco.Favoritos.inserir({ usuario: idUsuario, restaurante: idRestaurante})

            Retornar "Restaurante Adicionado com sucesso!"
        }
        
    } Capturar(erroBanco) {
        Log.erro("Falha na persistência de dados", erroBanco)

        DispararErro("Erro interno ao salvar favorito")
    }
}

```

### 🔹 Situações a serem testadas

- Situação 1: Tentar favoritar um restaurante que acabou de ser deletado do banco de dados.

- Situação 2: Testar se o código não buga com cliques rápido simultâneos evitando duplicidade.

- Situação 3: Testar logs de usuários/restaurantes.

### 🔹 Possíveis erros identificados

- O código não valida se o usuário enviado na requisição é o mesmo do token de login.

-  Pode permitir duplicidade de favoritos se não houver restrição no banco.

- Pode falhar em mandar o feedback de erro para o usuário.  

## ⚖️ 4. Comparação entre as abordagens

Qual a principal diferença entre testar sem ver o código e com acesso ao código?

O teste sem ver o código é como na visão do usuário, com o acesso ao código conseguimos atuar e pensar como dev.

Que tipo de problema cada abordagem ajuda a encontrar?

Caixa-preta:
- Problemas de usabilidade
- Bugs na interface
- Detalhes esquecidos
- Funções não funcionais

Caixa-branca:
- Falhas na lógica do código
- Código sujo
- Problemas de segurança
- Bugs escondidos

## 💡 5. Reflexão no contexto do LocalEats

Qual abordagem parece mais importante neste momento do projeto?

Caixa-branca pois os erros no código estão persistentes em relação a inconsistência e falhas específicas o que geralmente estão relacionados a lógica interna.

Apenas uma abordagem seria suficiente? Por quê?

Não, porque as duas abordagens são importantes para os dois lados do sistema, tendo a visão do usuário e a visão do desenvolvedor juntas para uma melhor avaliação completa.

## 🚀 Conclusão

Com essa atividade aprendi que testar um sistema é além de verificar se ele funciona.
Entendi que a diferença dos testes caixa-preta e caixa-branca revela a importância de fazer uma análise da lógica interna quanto da lógica externa sendo essencial a junção dos dois para desenvolver um sistema confiável, consistente e melhor para o mercado.