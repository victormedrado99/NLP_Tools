from tokens import tokenize

def analyze_mood(text: str) -> str:
    """
    Analisa o humor do texto de entrada com base em palavras positivas e negativas.
    
    Parâmetros:
    text (str): O texto a ser analisado.
    
    Retorna:
    str: 'Positivo', 'Negativo' ou 'Neutro' com base na análise do humor.
    """
    positive_words = ['feliz', 'alegre', 'ótimo', 'excelente', 'maravilhoso', 'fantástico']
    negative_words = ['triste', 'deprimido', 'ruim', 'horrível', 'terrível', 'péssimo']

    tokens: list[str] = tokenize(text)
    
    positive_mood: int = sum(1 for token in tokens if token in positive_words)
    negative_mood: int = sum(1 for token in tokens if token in negative_words)

    if positive_mood > negative_mood and positive_mood > 0:
        return 'Positivo'
    elif negative_mood > positive_mood and negative_mood > 0:
        return 'Negativo'
    else:
        return 'Neutro'