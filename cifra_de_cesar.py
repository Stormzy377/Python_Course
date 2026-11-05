# Cifra de César, um método de criptografia que desloca letras no alfabeto para codificar mensagens.

def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int) or isinstance(shift, bool):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

# Atribuição da mensagem criptografada
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'

# Chamada da função decrypt com deslocamento 13
decrypted_text = decrypt(encrypted_text, 13)

# Impressão do texto descriptografado
print(decrypted_text)
