import string


# Função Tokenizadora
def tokenize(text):
    """
    Tokeniza o texto de entrada em palavras individuais.
    
    Parâmetros:
    text (str): O texto a ser tokenizado.
    
    Retorna:
    list: Uma lista de tokens (palavras).
    """
    #Minizar o texto
    text = text.lower()
    # Dividir o texto em palavras usando espaços em branco como delimitadores
    raw_tokens = text.split()
    # Remover pontuação e converter para minúsculas
    table = str.maketrans('','', string.punctuation)
    tokens = [raw_token.translate(table) for raw_token in raw_tokens]
    return tokens



text = 'Olá, mundo! Este é um teste de tokenização.'
tokens = tokenize(text)
print(tokens)