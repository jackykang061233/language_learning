from japanese_learning.models import Vocabulary, Sentence
import pyttsx3
import time


class Japanese():
    def __init__(self):
        self.engine = pyttsx3.init(debug=True)
        self.engine.setProperty('voice', 'com.apple.speech.synthesis.voice.kyoko')
        self.engine.setProperty('rate', 150)

    def vocabulary(self):
        words = Vocabulary.objects.filter(category__id=1)

        for w in words:
            self.engine.say(w.kanji)
            self.engine.runAndWait()

    def sentence(self):
        sentences = Sentence.objects.filter(category__id=1)
        while True:
            for s in sentences:
                self.engine.say(s.jp)
                self.engine.runAndWait()
                time.sleep(2)

class Chinese():
    def __init__(self):
        self.engine = pyttsx3.init(debug=True)
        self.engine.setProperty('voice', 'com.apple.speech.synthesis.voice.meijia.premium')
        self.engine.setProperty('rate', 150)

    def vocabulary(self):
        words = Vocabulary.objects.filter(category__id=1)

        for w in words:
            self.engine.say(w.zh)
            self.engine.runAndWait()

    def sentence(self):
        sentences = Sentence.objects.all()

        for s in sentences:
            self.engine.say(s.zh)
            self.engine.runAndWait()
            time.sleep(2)

#chinese = Chinese()
# chinese.vocabulary()
#chinese.sentence()

japanese = Japanese()
# japanese.vocabulary()
japanese.sentence()

#./manage.py shell < japanese_learning/audio_practice.py 
# if __name__ == '__main__':
#     chinese = Chinese()
#     japanese = Japanese()
#     chinese.vocabulary()