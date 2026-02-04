from googletrans import Translator

def translate_to_hindi(text):
    try:
        translator = Translator()
        # Translate from English (en) to Hindi (hi)
        translation = translator.translate(text, dest='hi')
        return translation.text
    except Exception as e:
        return str(e)

# Example usage
input_text = "Hello, how are you?"
hindi_text = translate_to_hindi(input_text)

print(f"Original: {input_text}")
print(f"Hindi: {hindi_text}")