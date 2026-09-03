# Iniciação em Programação em Python

Esse é um projeto realizado pelos alunos Guilherme Lopes, Guilherme Shimano, José Hernandes, Lucas Nakamura e Vitor Teodoro, do curso de Ciência da Computação na UEM, para a matéria DIN na Comunidade lecionada pela professora Aline Miotto Amaral.

O conteúdo e os materiais utilizados foram feitos pelos alunos com base no material do [Professor Malbarbo](https://malbarbo.pro.br/). 

## Conteúdo

### Dia 1

- Introdução à linguagem Python e preparação do ambiente de desenvolvimento.
- Tipos de dados básicos (`int`, `float` e `str`), operações aritméticas e manipulação de textos.
- Variáveis, conversão de tipos e interação com a pessoa usuária por meio de `input()` e `print()`.

**Resumo:** primeiros passos para criar programas simples que recebem dados, os processam e exibem resultados.

### Dia 2

- Valores booleanos e operadores de comparação e lógicos.
- Estruturas condicionais com `if`, `elif` e `else`.
- Seleção de opções com `match-case`.

**Resumo:** uso de condições para que os programas possam tomar decisões conforme os dados recebidos.

### Dia 3

- Criação, acesso e manipulação de listas.
- Operações e métodos de listas, como `append()`, `pop()`, `sort()` e `len()`.
- Estruturas de repetição `for` e `while`.

**Resumo:** armazenamento de vários dados e repetição de tarefas de forma organizada e eficiente.

### Dia 4

- Criação e chamada de funções com parâmetros e valores de retorno.
- Escopo de variáveis e reutilização de código.
- Tipos de dados personalizados: compostos e enumerados.

**Resumo:** organização de programas em funções e modelagem de dados para deixar o código mais claro e reutilizável.

## Como entregar os exercícios pelo GitHub

Para enviar as resoluções dos exercícios, vocês vão usar o fluxo de **fork + pull request**, que é o mesmo usado em projetos reais de código aberto no mundo todo.

### Passo 1 — Faça um fork deste repositório

No canto superior direito desta página, clique no botão **Fork**. Isso vai criar uma cópia completa deste repositório na sua própria conta do GitHub.

### Passo 2 — Clone o seu fork

Já com o fork criado na sua conta, copie a URL dele (botão verde **Code**) e rode no terminal:

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
cd NOME-DO-REPOSITORIO
```

> Troque `SEU-USUARIO` pelo seu nome de usuário do GitHub e `NOME-DO-REPOSITORIO` pelo nome real do repositório.

### Passo 3 — Crie sua pasta de respostas

Dentro da pasta do exercício correspondente, crie uma pasta com o seu nome e coloque suas respostas lá dentro. Exemplo:

```
exercicios/dia1/joao-silva/exercicio1.py
```

### Passo 4 — Resolva os exercícios

Edite os arquivos normalmente no seu editor de código preferido (VS Code, PyCharm, etc.).

### Passo 5 — Envie suas mudanças (commit e push)

De volta ao terminal, na pasta do repositório:

```bash
git add .
git commit -m "Resolução da lista 01 - João Silva"
git push
```

### Passo 6 — Abra o Pull Request

Volte para a página do **seu fork** no GitHub. Vai aparecer um aviso com o botão **Compare & pull request** — clique nele.

Confira se está enviando do seu fork para o repositório original do grupo, escreva um título simples (ex: "Lista 01 - João Silva") e clique em **Create pull request**.

Pronto! Sua entrega está feita. Vamos revisar e comentar diretamente no Pull Request se for necessário algum ajuste.

---

### Resumo rápido dos comandos

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
cd NOME-DO-REPOSITORIO
# edite/crie seus arquivos de resposta
git add .
git commit -m "Resolução da lista 01 - Seu Nome"
git push
# depois, abra o Pull Request pelo site do GitHub
```

### Dúvidas comuns

- **"Não tenho Git instalado"** — baixe em [git-scm.com](https://git-scm.com/downloads) e configure seu nome/e-mail com `git config --global user.name "Seu Nome"` e `git config --global user.email "seu@email.com"`.
- **"Posso editar pelo site, sem usar o terminal?"** — sim! Depois do fork, é possível criar/editar arquivos direto pela interface do GitHub (botão de lápis ou "Add file"), sem precisar clonar nada. O commit e o pull request funcionam do mesmo jeito.
- **"Errei algo e quero corrigir depois de enviar o PR"** — sem problema, basta fazer um novo commit e `git push` novamente; o Pull Request é atualizado automaticamente.
