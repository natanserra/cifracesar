from decoder import ALFABETO, decoder


def cifrar(texto, chave):
    """Cifra um texto (só para teste), na ordem: base16 e depois deslocamento."""
    b16 = ""
    for c in texto:
        b16 += ALFABETO[ord(c) >> 4] + ALFABETO[ord(c) & 15]
    return "".join(
        ALFABETO[(ALFABETO.index(c) + ALFABETO.index(chave)) % 16] for c in b16
    )


def test_ida_e_volta():
    mensagem = "ola mundo"
    for chave in ALFABETO:
        assert decoder(cifrar(mensagem, chave), chave) == mensagem