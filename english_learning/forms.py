from django import forms
from flashcards.models import Flashcards, Flashcard_Text
import datetime

class FlashcardsForm(forms.ModelForm):
    forgetting_curve_days = [0, 1, 2, 3, 5, 10, 30 ,60, 90]
    STATUS_choices = [(i, i) for i in forgetting_curve_days]
    
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

    word = forms.CharField(max_length=50, help_text="Word: ", widget=forms.Textarea(attrs={'cols': 40, 'rows':5}))
    meaning = forms.CharField(max_length=300, help_text="Meaning: ", widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))
    example_sentence = forms.CharField(max_length=300, help_text="Example Sentence: ", widget=forms.Textarea(attrs={'cols': 40, 'rows': 20}), required = False)
    pos = forms.ChoiceField(choices=POS_choices, help_text='POS: ')
    status = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required = False)
    next_to_learn = forms.DateField(widget=forms.HiddenInput(), initial=datetime.date.today(), required = False)
    language = forms.ChoiceField(choices=LANGUAGE_choices, help_text='Language: ')

    class Meta:
        model = Flashcards
        fields = '__all__'


class FlashcardTextForm(forms.ModelForm):
    forgetting_curve_days = [0, 1, 2, 3, 5, 10, 30 ,60, 90]
    STATUS_choices = [(i, i) for i in forgetting_curve_days]

    # language
    ENGLISH = 'en'
    JAPANESE = 'jp'
    LANGUAGE_choices = [
        (ENGLISH, 'en'),
        (JAPANESE, 'jp')
    ]

    title = forms.CharField(max_length=100, help_text="Title: ", widget=forms.Textarea(attrs={'cols': 40, 'rows':5}))
    text = forms.CharField(help_text="Text: ", widget=forms.Textarea(attrs={'cols': 40, 'rows':20}), required = False)
    status = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required = False)
    next_to_learn = forms.DateField(widget=forms.HiddenInput(), initial=datetime.date.today(), required = False)
    language = forms.ChoiceField(choices=LANGUAGE_choices, help_text='Language: ')


    class Meta:
        model = Flashcard_Text
        fields = '__all__'