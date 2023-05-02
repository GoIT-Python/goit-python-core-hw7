from transliterate.decorators import transliterate_function

# from transliterate.contrib.apps.translipsum import TranslipsumGenerator

text = "Лорем ипсум долор сит амет"

# pg_uk = TranslipsumGenerator(language_code="uk")

# text = pg_uk.generate_sentence()

# print(text)


@transliterate_function(language_code="uk", reversed=True)
def translit(text):
    return text


print(translit(text))
