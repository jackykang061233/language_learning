from django import forms
from japanese_learning.models import Vocabulary, Category, Sentence, Sentence_Category, Grammer, Grammer_Category, Grammer_Test
import datetime

class VocaForm(forms.ModelForm):
    jp = forms.CharField(max_length=50, help_text="Japanese: ", widget=forms.Textarea(attrs={'cols': 40, 'rows':5}))
    kanji = forms.CharField(max_length=50, help_text="Kanji: ", widget=forms.Textarea(attrs={'cols': 40, 'rows':5}))
    zh = forms.CharField(max_length=50, help_text="Chinese: ", widget=forms.Textarea(attrs={'cols': 40, 'rows':5}))
    example_sentence = forms.CharField(max_length=300, help_text="Example Sentence: ", widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}), required = False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), help_text="Category: ",
                                    empty_label="Select Category")
    listening_status = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required = False)
    listening_next_to_learn = forms.DateField(widget=forms.HiddenInput(), initial=datetime.date.today(), required = False)
    translating_status = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required = False)
    translating_next_to_learn = forms.DateField(widget=forms.HiddenInput(), initial=datetime.date.today(), required = False)

    class Meta:
        model = Vocabulary
        fields = '__all__'

class SenForm(forms.ModelForm):
    kanji = forms.CharField(max_length=200, help_text="Kanji: ", widget=forms.Textarea(attrs={'cols': 40, 'rows':5}))
    jp = forms.CharField(max_length=200, help_text="Japanese: ", widget=forms.Textarea(attrs={'cols': 40, 'rows':5}))
    zh = forms.CharField(max_length=200, help_text="Chinese: ", widget=forms.Textarea(attrs={'cols': 40, 'rows':5}))
    category = forms.ModelChoiceField(queryset=Sentence_Category.objects.all(),
                                    empty_label="Select Category")
    # listening_status = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required = False)
    # listening_next_to_learn = forms.DateField(widget=forms.HiddenInput(), initial=datetime.date.today(), required = False)
    # translating_status = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required = False)
    # translating_next_to_learn = forms.DateField(widget=forms.HiddenInput(), initial=datetime.date.today(), required = False)
    
    class Meta:
        model = Sentence
        fields = '__all__'

class GrammerForm(forms.ModelForm):
    title = forms.CharField(max_length=50, help_text="Title: ", widget=forms.Textarea(attrs={'cols': 40, 'rows':5}))
    explanation = forms.CharField(max_length=1000, help_text="Explanation: ", widget=forms.Textarea(attrs={'cols': 40, 'rows': 20}))
    category = forms.ModelChoiceField(queryset=Grammer_Category.objects.all(), help_text="Grammer Category: ",
                                    empty_label="Select Category")

    class Meta:
        model = Grammer
        fields = '__all__'

class GrammerTestForm(forms.ModelForm):
    question = forms.CharField(max_length=300, help_text="Question: ", widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))
    category = forms.ModelChoiceField(queryset=Grammer.objects.all(), help_text="Grammer: ",
                                    empty_label="Select Category")
    solution = forms.CharField(max_length=300, help_text="Solution: ", widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    learning_status = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required = False)
    next_to_learn = forms.DateField(widget=forms.HiddenInput(), initial=datetime.date.today(), required = False)

    class Meta:
        model = Grammer_Test
        fields = '__all__'


class CateForm(forms.ModelForm):
    cat = forms.CharField(max_length=100, help_text="Category: ", widget=forms.Textarea(attrs={'cols': 40, 'rows':5}))

    class Meta:
        model = Category
        fields = '__all__'

class SenCateForm(forms.ModelForm):
    cat = forms.CharField(max_length=100, help_text="Category: ", widget=forms.Textarea(attrs={'cols': 40, 'rows':5}))

    class Meta:
        model = Sentence_Category
        fields = '__all__'

class GrammerCateForm(forms.ModelForm):
    cat = forms.CharField(max_length=100, help_text="Category: ", widget=forms.Textarea(attrs={'cols': 40, 'rows':5}))

    class Meta:
        model = Grammer_Category
        fields = '__all__'