from googletrans import Translator

translator = Translator()

def translate_text(text, src_lang, tgt_lang):
    src = "en" if src_lang == "English" else "ja"
    tgt = "ja" if tgt_lang == "Japanese" else "en"

    result = translator.translate(text, src=src, dest=tgt)
    return result.text
