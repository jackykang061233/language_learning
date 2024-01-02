from django.http import HttpResponseRedirect, HttpResponse
from .models import Flashcards, Flashcard_Text
from django.views import generic
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import FlashcardsForm, FlashcardTextForm
from django.contrib import messages
import datetime
from django.utils import timezone
from django.core.paginator import Paginator
from gtts.templatetags.gTTS import say


def home_page(request):
    return render(request, 'flashcards/home_page.html')


# WORD
class ToLearnWordsView(generic.ListView):
    context_object_name = 'flashcards'
    template_name = 'flashcards/learn_words.html'

    paginate_by = 20
    model = Flashcards

    def get_queryset(self):
        """Return all users."""
        return Flashcards.objects.filter(next_to_learn__lte=timezone.now()).filter(language=self.request.session['lang']).order_by('-next_to_learn')

def add_words(request):
    if request.method == 'POST':
        form = FlashcardsForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Thank you for adding')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            # return render(request, 'flashcards/add_words.html', {'form': form})
        else:
            print(form.errors)
    else:
        form = FlashcardsForm()
    
    return render(request, 'flashcards/add_words.html', {'form': form})

def words_match(request):
    
    return HttpResponse('hello4')

class AllWordsView(generic.ListView):
    context_object_name = 'flashcards'
    template_name = 'flashcards/all_words.html'

    paginate_by = 20
    model = Flashcards

    def get_queryset(self):
        """Return all users."""
        return Flashcards.objects.order_by('pk').filter(language=self.request.session['lang'])

def today_test_start(request):
    test_words = [word.word for word in Flashcards.objects.filter(next_to_learn__lte=datetime.date.today()).order_by('-next_to_learn')]
    if not test_words:
        return home_page(request)
    request.session['today_test'] = test_words
    request.session['index'] = 0

    return render(request, 'flashcards/test_start.html', {'first_word': request.session['today_test'][0]})

def today_test(request, word):
    if request.method == 'POST':
        current_word = Flashcards.objects.filter(word=word)[0]
        current_word.last_answer = request.POST['example']
        current_word.save()

        if current_word.last_answer == current_word.example_sentence:
            return today_test_pass(request, word)

        return render(request, 'flashcards/today_test_check.html', {'word': current_word})
        
    else:
        #obj = say(language='en', text=word)
        obj = 1
        progress = str(request.session['index']+1) + " \ "+ str(len(request.session['today_test']))

        return render(request, 'flashcards/today_test.html', {'word': word, 'obj':obj, 'progress':progress})

def today_test_pass(request, word):
    current_word = Flashcards.objects.filter(word=word)[0]
    if current_word.status == 90:
         current_word.next_to_learn = datetime.date.today() + datetime.timedelta(days = 10*365)
    else:
        current_word.status = Flashcards.Next_status[current_word.status]
        current_word.next_to_learn = datetime.date.today() + datetime.timedelta(days = current_word.status)
    current_word.save()

    next_index = request.session['index'] + 1
    request.session['index'] += 1

    if next_index >= len(request.session['today_test']):
        return home_page(request)
    return HttpResponseRedirect(reverse('flashcards:today_test', args=(request.session['today_test'][next_index],)))

def today_test_again(request, word):
    current_index = request.session['index']
    return HttpResponseRedirect(reverse('flashcards:today_test', args=(request.session['today_test'][current_index],)))

def today_test_fail(request, word):
    current_word = Flashcards.objects.filter(word=word)[0]
    current_word.status = 0
    current_word.next_to_learn = datetime.date.today() + datetime.timedelta(days = 1)
    current_word.save()

    next_index = request.session['index'] + 1
    request.session['index'] += 1

    if next_index >= len(request.session['today_test']):
        return home_page(request)
    return HttpResponseRedirect(reverse('flashcards:today_test', args=(request.session['today_test'][next_index],)))


# # PRACTICING
# def today_word_practice(request):
    
# TEXT
def add_texts(request):
    if request.method == 'POST':
        form = FlashcardTextForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Thank you for adding')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        else:
            print(form.errors)
    else:
        form = FlashcardTextForm()
    
    return render(request, 'flashcards/add_texts.html', {'form': form})
def today_text_test_start(request):
    if request.method == 'POST':
        to_test_id = int(request.POST['to_test_id'])
        if Flashcard_Text.objects.filter(text_id=to_test_id).exists():
            return HttpResponseRedirect(reverse('flashcards:today_text_test', args=([to_test_id])))

        return HttpResponseRedirect(reverse('flashcards:home_page'))

        
    return render(request, 'flashcards/text_test_start.html')

def today_text_test(request, text_id):
    if request.method == 'POST':
        text = Flashcard_Text.objects.filter(text_id=to_test_id)[0]

        return HttpResponse('hello')
    
    else:
        return render(request, 'flashcards/today_text_test.html', {'text_id': text_id})

class AllTextsView(generic.ListView):
    context_object_name = 'texts_flashcards'
    template_name = 'flashcards/all_texts.html'

    paginate_by = 1
    model = Flashcard_Text

    def get_queryset(self):
        """Return all users."""
        return Flashcard_Text.objects.order_by('pk').filter(language=self.request.session['lang'])

# NAV BAR
def nav_bar(request):
    return render(request, 'flashcards/nav_bar.html')

# LANGUAGE
def english(request):
    request.session['lang'] = 'en'
    return home_page(request)

def japanese(request):
    request.session['lang'] = 'jp'
    return home_page(request)

# Search
def search(request):
    if request.method == 'POST':
        searched_word = request.POST['search_word']
        return search_show_word(request, searched_word)
    return home_page(request)

def search_show_word(request, searched_word):
    try:
        words = Flashcards.objects.filter(word__contains=searched_word)
        return render(request, 'flashcards/search_show_word.html', {'words': words})
    except IndexError:
        return home_page(request)


