import sys
import spacy

nlp = spacy.load('pt_core_news_md')

def filter_by_open_class_words(text):
    doc = nlp(text)

    formatted_text = [token.text for token in doc if (token.pos_ == 'NOUN' or token.pos_ == 'PROPN' or token.pos_ == 'VERB' or token.pos_ == 'ADJ' or token.pos_ == 'ADV' or token.pos == 'NUM')]

    return ' '.join(formatted_text)

def read_file(file_path):
    with open(file_path, 'r') as reader:
        return reader.read()

def main():
    file_path = sys.argv[1]

    text = read_file(file_path)

    formatted_text = filter_by_open_class_words(text)

    print(formatted_text)

main()