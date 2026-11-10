"""Decodificador para uma cifra de César com alfabeto de 16 letras (a-p),
combinada com um base16 customizado. Faz força bruta nas 16 chaves possíveis.
"""

import argparse
import string

ALFABETO = string.ascii_lowercase[:16]  # 'abcdefghijklmnop'


def validar_entrada(texto):
    invalidos = set(texto) - set(ALFABETO)
    if invalidos:
        raise ValueError(f"Caracteres inválidos (use só a-p): {sorted(invalidos)}")
    if len(texto) % 2 != 0:
        raise ValueError("O texto precisa ter um número par de letras.")


def desfazer_deslocamento(letra, chave):
    posicao = ALFABETO.index(letra) - ALFABETO.index(chave)
    return ALFABETO[posicao % len(ALFABETO)]


def decodificar_base16(texto):
    resultado = ""
    for i in range(0, len(texto), 2):
        alto = ALFABETO.index(texto[i])
        baixo = ALFABETO.index(texto[i + 1])
        resultado += chr((alto << 4) + baixo)  # alto * 16 + baixo
    return resultado


def decodificar(texto, chave):
    """Desfaz o deslocamento e depois o base16 customizado."""
    sem_deslocamento = "".join(desfazer_deslocamento(c, chave) for c in texto)
    return decodificar_base16(sem_deslocamento)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("texto_cifrado", help="texto cifrado, só com letras de a a p")
    parser.add_argument(
        "--todas",
        action="store_true",
        help="mostra todas as chaves, inclusive resultados ilegíveis",
    )
    args = parser.parse_args()

    try:
        validar_entrada(args.texto_cifrado)
    except ValueError as erro:
        parser.error(str(erro))

    for chave in ALFABETO:
        resultado = decodificar(args.texto_cifrado, chave)
        if args.todas or resultado.isprintable():
            print(f"Chave '{chave}': {resultado!r}")


if __name__ == "__main__":
    main()