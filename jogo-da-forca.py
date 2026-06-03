import random

# Lista de palavras
PALAVRAS = [
    "python", "programacao", "computador", "teclado", "monitor",
    "algoritmo", "variavel", "funcao", "lista", "dicionario",
    "classe", "objeto", "metodo", "biblioteca", "repositorio"
]

# Desenhos da forca
FORCA = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


def escolher_palavra():
    return random.choice(PALAVRAS)


def exibir_palavra(palavra, letras_corretas):
    return " ".join(letra if letra in letras_corretas else "_" for letra in palavra)


def jogar():
    print("=" * 40)
    print("       BEM-VINDO AO JOGO DA FORCA!")
    print("=" * 40)

    palavra = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas_maximas = 6

    while True:
        erros = len(letras_erradas)

        print(FORCA[erros])
        print(f"Palavra: {exibir_palavra(palavra, letras_corretas)}")
        print(f"Letras erradas: {', '.join(sorted(letras_erradas)) or '-'}")
        print(f"Tentativas restantes: {tentativas_maximas - erros}")
        print()

        # Verificar vitória
        if all(letra in letras_corretas for letra in palavra):
            print(f"🎉 Parabéns! Você acertou a palavra: '{palavra}'")
            break

        # Verificar derrota
        if erros >= tentativas_maximas:
            print(f"💀 Game Over! A palavra era: '{palavra}'")
            break

        # Entrada do jogador
        chute = input("Digite uma letra: ").lower().strip()

        if len(chute) != 1 or not chute.isalpha():
            print("⚠️  Digite apenas uma letra válida!")
            continue

        if chute in letras_corretas or chute in letras_erradas:
            print("⚠️  Você já tentou essa letra!")
            continue

        if chute in palavra:
            letras_corretas.add(chute)
            print("✅ Letra correta!")
        else:
            letras_erradas.add(chute)
            print("❌ Letra errada!")

    print()
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente == "s":
        jogar()
    else:
        print("Obrigado por jogar! Até a próxima. 👋")


if __name__ == "__main__":
    jogar()
