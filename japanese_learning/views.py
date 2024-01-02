from django.shortcuts import render
from .models import Vocabulary, Category, Sentence, Sentence_Category, Top_Category, Top_Sentence_Category, Grammer, Grammer_Test, Grammer_Category, Top_Grammer_Category
from .forms import VocaForm, CateForm, SenForm, SenCateForm, GrammerForm, GrammerTestForm, GrammerCateForm
import pyttsx3
import time
from django.http import HttpResponseRedirect, HttpResponse
from queue import Queue
from threading import Thread
from django.urls import reverse
from gtts.templatetags.gTTS import say
import datetime
from collections import OrderedDict
from django.core.paginator import Paginator

# BASIC
q = Queue()
engine = pyttsx3.init(debug=True)
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.kyoko')

# HOME PAGE
def home_page(request):
    return render(request, 'japanese_learning/home_page/home_page.html')

# NAV BAR
def nav_bar(request):
    return render(request, 'japanese_learning/nav_bar/nav_bar.html')

# ADDING

def add_vocabulary(request):
    if request.method == 'POST':
        form = VocaForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        else:
            print(form.errors)
    else:
        form = VocaForm()
    
    return render(request, 'japanese_learning/adding/add_vocabulary.html', {'form': form})

def add_category(request):
    if request.method == 'POST':
        form = CateForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        else:
            print(form.errors)
    else:
        form = CateForm()
    
    return render(request, 'japanese_learning/adding/add_category.html', {'form': form})

def add_sentence(request):
    if request.method == 'POST':
        form = SenForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        else:
            print(form.errors)
    else:
        form = SenForm()

    return render(request, 'japanese_learning/adding/add_sentence.html', {'form': form})

def add_sentence_category(request):
    if request.method == 'POST':
        form = SenCateForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        else:
            print(form.errors)
    else:
        form = SenCateForm()

    return render(request, 'japanese_learning/adding/add_sentence_category.html', {'form': form})

def add_grammer(request):
    if request.method == 'POST':
        form = GrammerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        else:
            print(form.errors)
    else:
        form = GrammerForm()
    
    return render(request, 'japanese_learning/adding/add_grammer.html', {'form': form})

def add_grammer_test(request):
    if request.method == 'POST':
        form = GrammerTestorm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        else:
            print(form.errors)
    else:
        form = GrammerTestForm()
    
    return render(request, 'japanese_learning/adding/add_grammer_test.html', {'form': form})

def add_grammer_category(request):
    if request.method == 'POST':
        form = GrammerCateForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        else:
            print(form.errors)
    else:
        form = GrammerCateForm()
    
    return render(request, 'japanese_learning/adding/add_grammer_category.html', {'form': form})

# Practicing

def practice_home_page(request):
    cat = Top_Category.objects.all()
    return render(request, 'japanese_learning/practice/vocabulary/practice_home_page.html', {'cats': cat})

def practice_cat_home_page(request, top_cat_id):
    cat = Category.objects.filter(top_cat=top_cat_id)
    return render(request, 'japanese_learning/practice/vocabulary/practice_cat_home_page.html', {'cats': cat})

def practice(request, cat_id): 
    return render(request, 'japanese_learning/practice/vocabulary/listening_translating_voca.html', {'cat_id': cat_id})
   
def voca_test_start(request, cat_id, translate):
    if translate:
        words = Vocabulary.objects.filter(category=cat_id).filter(translating_next_to_learn__lte=datetime.date.today())
    else:
        words = Vocabulary.objects.filter(category=cat_id).filter(listening_next_to_learn__lte=datetime.date.today())

    if not words:
        cat = Top_Category.objects.get(cat=Category.objects.get(id=cat_id).top_cat).id
        return HttpResponseRedirect(reverse('jp_learning:practice_cat_home_page', args=(cat, )))

    request.session['fail'] = []
    request.session['words'] = [word.id for word in words]
    request.session['index'] = 0

    return render(request, 'japanese_learning/practice/vocabulary/voca_test_start.html', {'first_word': request.session['words'][0], 'translate': translate}) 

def voca_listening(request, voca_id):
    current_word = Vocabulary.objects.filter(id=voca_id)[0]
    if request.method == 'POST':
        answer = request.POST['answer']
        example = request.POST.get('example', '')

        if answer == current_word.kanji and example == current_word.example_sentence:
            return test_pass(request, voca_id, 1, 0)

        return render(request, 'japanese_learning/practice/check/test_check.html', {'question': current_word, 'answer': answer, 'example': example, 'voca':1, 'translate': 0})
                
    else:
        chinese = current_word.zh
        voca = say(language='ja', text=current_word.jp)
        try:
            example = say(language='ja', text=current_word.example_sentence)
        except AssertionError:
            example = 0

        progress = str(request.session['words'].index(voca_id)+1) + " \ "+ str(len(request.session['words']))

        return render(request, 'japanese_learning/practice/vocabulary/practice_voca.html', {'translate':False, 'chinese': chinese, 'voca':voca, 'example':example, 'progress': progress})

def voca_translating(request, voca_id):
    current_word = Vocabulary.objects.filter(id=voca_id)[0]
    if request.method == 'POST':
        answer = request.POST['answer']
        example = request.POST.get('example', '')

        if answer == current_word.kanji and example == current_word.example_sentence:
            return test_pass(request, voca_id, 1, 1)

        return render(request, 'japanese_learning/practice/check/test_check.html', {'question': current_word, 'answer': answer, 'example': example, 'voca':1, 'translate': 1})
        
    else:
        chinese = current_word.zh
        progress = str(request.session['words'].index(voca_id)+1) + " \ "+ str(len(request.session['words']))
        example = current_word.example_sentence
       

        return render(request, 'japanese_learning/practice/vocabulary/practice_voca.html', {'translate':True, 'chinese': chinese, 'example':example, 'progress': progress})

def voca_result(request):
    cat = Category.objects.get(cat=Vocabulary.objects.filter(id=request.session['words'][0])[0].category)
    words = [Vocabulary.objects.get(id=voca_id) for voca_id in request.session['words']]
    sucess = len(words) - len(request.session['fail'])
    
    return render(request, 'japanese_learning/practice/result/voca_result.html', {'fail':request.session['fail'], 'words': words, 'cat':cat, 'sucess':sucess})


def practice_sentence_home_page(request):
    cat = Top_Sentence_Category.objects.all()
    return render(request, 'japanese_learning/practice/sentence/practice_sentence_home_page.html', {'cats': cat})

def practice_sentence_cat_home_page(request, top_cat_id):
    cat = Sentence_Category.objects.filter(top_cat=top_cat_id)
    cat = sorted(cat, key=lambda x:int(x.cat), reverse=True)
    print(type(cat))
    return render(request, 'japanese_learning/practice/sentence/practice_sentence_cat_home_page.html', {'cats': cat})

def sent_practice(request, cat_id):
    return render(request, 'japanese_learning/practice/sentence/listening_translating_sent.html', {'cat_id': cat_id})

def sent_test_start(request, cat_id, translate):
    if translate:
        sentences = Sentence.objects.filter(category=cat_id).filter(translating_next_to_learn__lte=datetime.date.today())
        sentences = Sentence.objects.filter(category=cat_id)
    else:
        sentences = Sentence.objects.filter(category=cat_id).filter(listening_next_to_learn__lte=datetime.date.today())
        sentences = Sentence.objects.filter(category=cat_id)

    if not sentences:
        cat = Top_Sentence_Category.objects.get(cat=Sentence_Category.objects.get(id=cat_id).top_cat).id
        return HttpResponseRedirect(reverse('jp_learning:practice_sentence_cat_home_page', args=(cat, )))

    request.session['fail'] = []
    request.session['sentences'] = [sentence.id for sentence in sentences]
    request.session['index'] = 0

    return render(request, 'japanese_learning/practice/sentence/sent_test_start.html', {'first_sentence': request.session['sentences'][0], 'translate': translate}) 

def sent_listening(request, sent_id):
    current_sentence = Sentence.objects.filter(id=sent_id)[0]
    if request.method == 'POST':
        answer = request.POST['answer']

        if answer == current_sentence.kanji:
            return test_pass(request, sent_id, 0, 0)

        return render(request, 'japanese_learning/practice/check/test_check.html', {'question': current_sentence, 'answer': answer, 'voca':0, 'translate': 0})
    else:
        chinese = current_sentence.zh
        obj = say(language='ja', text=current_sentence.jp)
        progress = str(request.session['sentences'].index(sent_id)+1) + " \ "+ str(len(request.session['sentences']))

        return render(request, 'japanese_learning/practice/sentence/practice_sentence.html', {'translate':False, 'chinese': chinese, 'obj':obj, 'progress': progress})

def sent_translating(request, sent_id):
    current_sentence = Sentence.objects.filter(id=sent_id)[0]
    if request.method == 'POST':
        answer = request.POST['answer']

        if answer == current_sentence.kanji:
            return test_pass(request, sent_id, 0, 1)
            
        return render(request, 'japanese_learning/practice/check/test_check.html', {'question': current_sentence, 'answer': answer, 'voca':0, 'translate': 1})
        
    else:
        chinese = current_sentence.zh
        progress = str(request.session['sentences'].index(sent_id)+1) + " \ "+ str(len(request.session['sentences']))

        return render(request, 'japanese_learning/practice/sentence/practice_sentence.html', {'translate':True, 'chinese': chinese, 'progress': progress})


def sent_result(request):
    cat = Sentence_Category.objects.get(cat=Sentence.objects.filter(id=request.session['sentences'][0])[0].category)
    sents = [Sentence.objects.get(id=sent_id) for sent_id in request.session['sentences']]
    sucess = len(sents) - len(request.session['fail'])
    
    return render(request, 'japanese_learning/practice/result/sent_result.html', {'fail':request.session['fail'], 'sents': sents, 'cat':cat, 'sucess':sucess})


def test_pass(request, voca_or_sent_id, voca, translate):
    if voca:
        current = Vocabulary.objects.filter(id=voca_or_sent_id)[0]
        if translate:
            current.translating_status = Vocabulary.Next_status[current.translating_status]
            current.translating_next_to_learn = datetime.date.today() + datetime.timedelta(days = current.translating_status)
        else:
            current.listening_status = Vocabulary.Next_status[current.listening_status]
            current.listening_next_to_learn = datetime.date.today() + datetime.timedelta(days = current.listening_status)
        current.save()
    else:
        current = Sentence.objects.filter(id=voca_or_sent_id)[0]
    
    if translate:
        current.translating_status = Vocabulary.Next_status[current.translating_status]
        current.translating_next_to_learn = datetime.date.today() + datetime.timedelta(days = current.translating_status)
    else:
        current.listening_status = Vocabulary.Next_status[current.listening_status]
        current.listening_next_to_learn = datetime.date.today() + datetime.timedelta(days = current.listening_status)
    current.save()

    return test_continue(request, voca, translate)

def test_again(request, voca, translate):
    current_index = request.session['index']
    if voca:
        if translate: # translating
            return HttpResponseRedirect(reverse('jp_learning:voca_translating', args=(request.session['words'][current_index],)))
        return HttpResponseRedirect(reverse('jp_learning:voca_listening', args=(request.session['words'][current_index],))) # listening
    
    else:
        if translate: # translating
            return HttpResponseRedirect(reverse('jp_learning:sent_translating', args=(request.session['sentences'][current_index],)))
        return HttpResponseRedirect(reverse('jp_learning:sent_listening', args=(request.session['sentences'][current_index],))) # listening

def test_fail(request, voca_or_sent_id, voca, translate):
    request.session['fail'] += [voca_or_sent_id]
    if voca:
        current = Vocabulary.objects.filter(id=voca_or_sent_id)[0]
        if translate:
            current.translating_status = 0
            current.translating_next_to_learn = datetime.date.today() + datetime.timedelta(days = 1)
        else:
            current.listening_status = 0
            current.listening_next_to_learn = datetime.date.today() + datetime.timedelta(days = 1)
    else:
        current = Sentence.objects.filter(id=voca_or_sent_id)[0]

    if translate:
        current.translating_status = 0
        current.translating_next_to_learn = datetime.date.today() + datetime.timedelta(days = 1)
    else:
        current.listening_status = 0
        current.listening_next_to_learn = datetime.date.today() + datetime.timedelta(days = 1)
    current.save()
    
    return test_continue(request, voca, translate)

def test_continue(request, voca, translate):
    next_index = request.session['index'] + 1
    request.session['index'] += 1
    
    if voca:
        if next_index >= len(request.session['words']): # end
            return HttpResponseRedirect(reverse('jp_learning:voca_result'))
        if translate: # translating
            return HttpResponseRedirect(reverse('jp_learning:voca_translating', args=(request.session['words'][next_index],)))        
        return HttpResponseRedirect(reverse('jp_learning:voca_listening', args=(request.session['words'][next_index],))) # listening
    
    else:
        if next_index >= len(request.session['sentences']):# end
            return HttpResponseRedirect(reverse('jp_learning:sent_result'))
        if translate: # translating
            return HttpResponseRedirect(reverse('jp_learning:sent_translating', args=(request.session['sentences'][next_index],)))
        return HttpResponseRedirect(reverse('jp_learning:sent_listening', args=(request.session['sentences'][next_index],))) # listening

# List

def list_home_page(request):
    cat = Top_Category.objects.all()
    return render(request, 'japanese_learning/list/list_home_page.html', {'cats': cat})

def list_cat_home_page(request, top_cat_id):
    cat = Category.objects.filter(top_cat=top_cat_id)
    return render(request, 'japanese_learning/list/list_cat_home_page.html', {'cats': cat})

def category_list(request, cat_id):
    words = Vocabulary.objects.filter(category=cat_id)
    cat = Category.objects.filter(id=cat_id)[0].cat
    total = len(words)

    return render(request,'japanese_learning/list/show_cat_voca.html', {'words': words, 'cat': cat, 'total': total})

def list_sentence_home_page(request):
    cat = Top_Sentence_Category.objects.all()
    return render(request, 'japanese_learning/list/list_sentence_home_page.html', {'cats': cat})


def list_sentence_cat_home_page(request, top_cat_id):
    cat = Sentence_Category.objects.filter(top_cat=top_cat_id)
    return render(request, 'japanese_learning/list/list_sentence_cat_home_page.html', {'cats': cat})

def category_sentence_list(request, cat_id):
    sentences = Sentence.objects.filter(category=cat_id)
    paginator = Paginator(sentences, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    cat = Sentence_Category.objects.filter(id=cat_id)[0].cat
    total = len(sentences)

    return render(request,'japanese_learning/list/show_cat_sen.html', {'page_obj': page_obj, 'sents': sentences, 'cat': cat, 'total': total})



def list_grammer_cat_home_page(request, top_cat_id):
    cat = Grammer_Category.objects.filter(top_cat=top_cat_id)
    return render(request, 'japanese_learning/list/list_grammer_cat_home_page.html', {'cats': cat})

def list_grammer_home_page(request):
    cat = Top_Grammer_Category.objects.all()
    return render(request, 'japanese_learning/list/list_grammer_home_page.html', {'cats': cat})

def category_grammer_list(request, cat_id):
    grammers = Grammer.objects.filter(category=cat_id)[0]
    cat = Grammer_Category.objects.filter(id=cat_id)[0].cat


    return render(request,'japanese_learning/list/show_cat_grammer.html', {'grammers': grammers, 'cat': cat,})



