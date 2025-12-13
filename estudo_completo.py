import string


def tokenize(text: str) -> list[str]:
    """
    Tokeniza o texto de entrada em palavras indivicuais e retorna uma lista de tokens limpos
    """
    #Minimiza o texto
    text: str = text.lower()
    #Dividi o texto em palavras
    raw_tokens: list[str] = text.split()
    # Cria a tabela para remoção de pontuação
    table = str.maketrans("", "", string.punctuation)
    # Aplica a tradução e remove a pontuação
    tokens: list[str] = [token.translate(table) for token in raw_tokens]

    return tokens

def mood_analyzer(text: str) -> str:
    """
    Analisa o humor o texto de entrada com base na quantidade de 
    palavras positivas e negativas
    """

    # Listas de palavras positivas e negativas
    palavras_positivas: list[str] = ['feliz', 'alegre', 'ótimo', 'excelente', 'maravilhoso', 'fantástico']
    palavras_negativas: list[str] = ['triste', 'deprimido', 'ruim', 'horrível', 'terrível', 'péssimo']

    tokens: list[str] = tokenize(text)

    humor_positivo: int = sum(1 for token in tokens if token in palavras_positivas)
    humor_negativo: int = sum(1 for token in tokens if token in palavras_negativas)

    if humor_positivo > humor_negativo and humor_positivo > 0:
        return 'Positivo'
    elif humor_negativo > humor_positivo and humor_negativo > 0:    
        return 'Negativo'
    else:
        return 'Neutro'
    
if __name__ == "__main__":
    textos = {
        1: "Estou muito feliz hoje! O dia está ótimo.",
        2: "Sinto-me triste e deprimido.",
        3: "O tempo está nublado.",
        4: "Que dia maravilhoso e fantástico!",
        5: "Isso é péssimo, estou muito ruim."
    }
    for num, text in textos.items():
        humor = mood_analyzer(text)
        print(f"Texto {num}: \nHumor: {humor}\n")