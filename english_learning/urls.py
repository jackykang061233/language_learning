from django.urls import path

from . import views

app_name = 'flashcards'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add_words/', views.add_words, name='add_words'),
    path('add_texts/', views.add_texts, name='add_texts'),
    
    path('nav_bar/', views.nav_bar, name='nav_bar'),
    path('search/', views.search, name='search'),

    path('words_list/', views.AllWordsView.as_view(), name='words_list'),
    path('today_test/', views.today_test_start, name='today_test_start'),#views.TodayTestView.as_view()
    path('today_test/<str:word>', views.today_test, name='today_test'),
    path('today_test/<str:word>/pass/', views.today_test_pass, name='today_test_pass'),
    path('today_test/<str:word>/fail/', views.today_test_fail, name='today_test_fail'),
    path('today_test/<str:word>/again/', views.today_test_again, name='today_test_again'),
    path('words_match/', views.words_match, name='words_match'),
    path('learn_words/', views.ToLearnWordsView.as_view(), name='learn_words'),

    # path('today_word_practice/', views.today_word_practice, name='today_word_practice'),
    # path('today_text_practice/', views.today_text_practice, name='today_text_practice'),

    path('today_text_test/', views.today_text_test_start, name='today_text_test_start'),
    path('today_text_test/<int:text_id>', views.today_text_test, name='today_text_test'),
    path('texts_list/', views.AllTextsView.as_view(), name='texts_list'),
    # path('learn_text/', views.ToLearnWordsView.as_view(), name='learn_text')
    
    # language
    path('en/', views.english, name='english'),
    path('jp/', views.japanese, name='japanese'),
]