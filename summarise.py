from aylienapiclient import textapi

f = open("key")
key = f.readline()
key = key.strip()
f.close()

f = open("app_id")
app_id = f.readline()
app_id = app_id.strip()
f.close()

client = textapi.Client(app_id, key)

def summarise(text, title, sentence_percentage):
    summary = client.Summarize({'title': title, 'text': text, 'sentences_percentage': sentence_percentage})
    return summary

