
# 📘 Assignment: Jogo da Forca

## 🎯 Objective

Pratique manipulação de strings, loops, condicionais, entrada de dados e seleção aleatória em Python ao criar um jogo da Forca jogável no terminal.

## 📝 Tasks

### 🛠️ Implementar o Jogo da Forca

#### Descrição

Crie um jogo em que o programa seleciona uma palavra secreta e o jogador tenta descobri-la, informando uma letra por vez.

#### Requisitos

O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida.
- Exibir cada letra ainda não descoberta como um sublinhado, mantendo visíveis as letras acertadas.
- Permitir palpites de letras e atualizar o progresso após cada palpite.
- Começar com seis tentativas e diminuir esse total a cada palpite incorreto.
- Encerrar quando o jogador descobrir a palavra ou ficar sem tentativas.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra secreta.

Exemplo de uma rodada com a palavra secreta `casa`:

```text
Palavra: _ _ _ _
Tentativas restantes: 6
Digite uma letra: a
Acertou! Palavra: _ a _ a
```