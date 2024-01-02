from django.db import models
from django.utils import timezone
import datetime

class Flashcards(models.Model):
    # days for learning
    forgetting_curve_days = [0, 1, 2, 3, 5, 10, 30 ,60, 90]
    STATUS_choices = [(i, i) for i in forgetting_curve_days]
    Next_status = {0:1, 1:2, 2:3, 3:5, 5:10, 10:30, 30:60 , 60:90}
    
    # part of speech
    NOUN = 'noun'
    VERB = "verb"
    ADJ = "adjective"
    ADV = "adverb"
    PRONOUN = "pronoun"
    PREPOSITION = 'preposition'
    CONJUNCTION = 'conjunction'
    POS_choices = [
        (NOUN, 'noun'),
        (VERB, 'verb'),
        (ADJ, 'adjective'),
        (ADV, 'adverb'),
        (PRONOUN, 'pronoun'),
        (PREPOSITION, 'preposition'),
        (CONJUNCTION, 'conjunction')
    ]

    # language
    ENGLISH = 'en'
    JAPANESE = 'jp'
    LANGUAGE_choices = [
        (ENGLISH, 'en'),
        (JAPANESE, 'jp')
    ]

    word = models.CharField(max_length=50, blank=False)
    meaning = models.TextField(max_length=300, blank=False)
    example_sentence = models.TextField(max_length=300, blank=True)
    last_answer = models.TextField(max_length=300, blank=True)
    pos = models.CharField(max_length=11, choices=POS_choices, default=POS_choices[0])
    status = models.PositiveSmallIntegerField(choices=STATUS_choices, default=0)
    next_to_learn = models.DateField(default=timezone.now)
    language = models.CharField(max_length=5, choices=LANGUAGE_choices, default='en')
    # last_test_result = models.TextField(max_length=300)

    def __str__(self):
        return self.word

class Flashcard_Text(models.Model):
    # days for learning
    forgetting_curve_days = [0, 1, 2, 3, 5, 10, 30 ,60, 90]
    STATUS_choices = [(i, i) for i in forgetting_curve_days]
    Next_status = {0:1, 1:2, 2:3, 3:5, 5:10, 10:30, 30:60 , 60:90}

    # language
    ENGLISH = 'en'
    JAPANESE = 'jp'
    LANGUAGE_choices = [
        (ENGLISH, 'en'),
        (JAPANESE, 'jp')
    ]
    
    text_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True)
    text = models.TextField(blank=False)
    status = models.PositiveSmallIntegerField(choices=STATUS_choices, default=0)
    next_to_learn = models.DateField(default=timezone.now)
    language = models.CharField(max_length=5, choices=LANGUAGE_choices, default='en')


    def __str__(self):
        return self.title

