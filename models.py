from textblob import TextBlob

class SpellChecker:
    def __init__(self):
        pass

    def correct_spell(self, text):
        words = text.split()
        corrected_words = [str(TextBlob(word).correct()) for word in words]
        return " ".join(corrected_words)

    def correct_grammar(self, text, corrected_text):
        original_words = text.split()
        corrected_words = corrected_text.split()
        found_mistakes = [original for original, corrected in zip(original_words, corrected_words) if original != corrected]
        return found_mistakes
