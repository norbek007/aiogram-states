import wikipedia

def malumot(text):
    try:
        wikipedia.set_lang("uz")
        result = wikipedia.summary(text)
    except:
        return "Afsus siz izlagan ma'lumot topilmadi"
    return result
