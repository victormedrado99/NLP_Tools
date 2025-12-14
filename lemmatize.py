import string
import spacy

# Carrega o modelo de linguagem do spaCy para português
try:
    nlp = spacy.load("pt_core_news_sm")
except OSError:
    print("Modelo 'pt_core_news_sm' não encontrado. Por favor, instale-o usando:")
    print("python -m spacy download pt_core_news_sm")
    exit()


def tokenize_and_lemmatize(text: str) -> list[str]:
    """
    Realiza tokenização e lematização do texto de entrada.
    """

    # 1 Processa o texto com o modelo SpaCy
    doc = nlp(text.lower())
    tks = []

    for tk in doc:
        # 2. Ignora pontuação e espaços
        if tk.text not in string.punctuation and not tk.is_space:
            # 3. Adiciona a forma lematizada do token à lista
            tks.append(tk.lemma_)
    return tks


# Uso:

text = "Estou muito feliz hoje! O dia está ótimo."
lemmas = tokenize_and_lemmatize(text)
print(lemmas)