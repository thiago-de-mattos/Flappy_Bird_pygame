# Flappy Bird Pygame

Um clone do clássico Flappy Bird feito em **Python** usando **pygame**.

## 🕹️ Gameplay

- Controle o pássaro clicando ou pressionando uma tecla para voar.
- Evite colidir com os canos.
- Pontue passando pelos obstáculos.

---

## 📂 Estrutura do projeto

flappy_bird_pygame/
│
├─ bird/ ← ambiente virtual (venv)
├─ assets/ ← imagens e sons do jogo
│ ├─ imagens/
│ │ ├─ bird.png
│ │ ├─ pipe.png
│ │ └─ background.png
│ └─ sons/
│ └─ flap.wav
├─ main.py ← ponto de entrada do jogo
├─ jogo.py ← classes e lógica do jogo
├─ constantes.py ← dimensões da tela, imagens e sons
└─ requirements.txt ← dependências (pygame)


---

## ⚡ Como rodar

1. Clone o projeto:
```bash
git clone https://github.com/SEU_USUARIO/flappy-bird-pygame.git
cd flappy-bird-pygame

py -m venv bird
bird\Scripts\activate.bat

pip install -r requirements.txt

python main.py


🛠️ Tecnologias usadas

Python 3.13

Pygame 2.6.1

Git/GitHub para versionamento

📖 Licença

Este projeto é open source. Sinta-se à vontade para estudar, modificar e compartilhar.
