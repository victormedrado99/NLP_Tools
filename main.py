from mood_analyzer import analyze_mood

if __name__ == "__main__":
    sample_texts = {
        1:"Estou muito feliz hoje! O dia está ótimo.",
        2:"Sinto-me triste e deprimido.",
        3:"O tempo está nublado.",
        4:"Que dia maravilhoso e fantástico!",
        5:"Isso é péssimo, estou muito ruim."
    }

    for key, text in sample_texts.items():
        mood = analyze_mood(text)
        print(f"Texto: {key}\nHumor Analisado: {mood}\n")