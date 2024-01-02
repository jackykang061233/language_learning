from japanese_learning.models import Vocabulary, Sentence, Sentence_Category
import pandas as pd


def add_sentence(file, cat_id):
    df = pd.read_csv(file)
    for index, row in df.iterrows():
        sent = Sentence(jp=row[1], kanji=row[0], zh=row[2], category_id=cat_id) 
        sent.save()


def add_vocabulary(file, cat_id):
    df = pd.read_csv(file)
    for index, row in df.iterrows():
        voca = Vocabulary(jp=row[1], kanji=row[0], zh=row[2], category_id=cat_id) 
        voca.save()

def get_sentences_to_csv(cat_id, output_dir='japanese_learning/日中文/'):
    category = Sentence_Category.objects.filter(id=cat_id)[0].cat
    Sentences = Sentence.objects.filter(category=cat_id)
    translation = [(sentence.jp, sentence.zh) for sentence in Sentences]
    df = pd.DataFrame(translation, columns=['日文', '中文'])
    df.to_csv(output_dir+category+'.csv', index=False)

# get_sentences_to_csv(9)         

add_sentence('/Users/kangchieh/Dev/dev/django/django/src/mysite/japanese_learning/csv/read_csv.csv', 14)
# ./manage.py shell < japanese_learning/add_from_csv.py 
