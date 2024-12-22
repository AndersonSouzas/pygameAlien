# pygameAlien

Este repositório contém o código-fonte de um jogo básico desenvolvido em Pygame para a da disciplina de Laboratório de Programação. O jogo envolve um personagem jogável que deve evitar colisões com inimigos, e a dificuldade aumenta conforme o jogo progride.

## Descrição do Jogo

Neste jogo, o jogador controla um personagem que se movimenta dentro de um cenário. O objetivo é evitar colidir com os inimigos, que se movem de forma aleatória pela tela. A cada colisão, o jogo exibe uma mensagem de "Game Over" e termina. O jogo inclui um cenário de fundo, sprites de personagens e inimigos, e algumas mecânicas básicas como movimentação e detecção de colisão.

### Funcionalidades Básicas

- O jogador controla o personagem utilizando as teclas: (W, S, A, D).
- Inimigos se movem de forma aleatória e mudam de direção ao bater nas bordas da tela.
- Quando o personagem colide com um inimigo, o jogo exibe uma mensagem de "Game Over".
- Após o Game Over é possivel reiniciar o jogo usando a tecla: R

### Desafios

- **Desafio 1**: Sistema de pontuação — o jogador ganha pontos ao evitar inimigos.
- **Desafio 2**: Aumenta a velocidade dos inimigos com o tempo, aumentando a dificuldade.
- **Desafio 3**: Adição de mais inimigos que surgem de forma aleatória em diferentes posições.

## Requisitos

- Python 3.x
- Pygame

## Instruções de Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/AndersonSouzas/pygameAlien

2. Navegue até a pasta do projeto:  
   ```bash
   cd pygameAlien

3. Instale as dependências:
   ```nash
   pip install pygame

4. Execute o jogo:
   ```bash
   python main.py

## Contribuição

Sinta-se à vontade para contribuir com este projeto criando um **Pull Request** ou abrindo uma **Issue** para sugerir melhorias.
