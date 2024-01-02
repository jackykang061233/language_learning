from django.urls import path, include, re_path
from . import views

app_name = 'jp_learning'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add_vocabulary/', views.add_vocabulary, name='add_vocabulary'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_sentence/', views.add_sentence, name='add_sentence'),
    path('add_sentence_category/', views.add_sentence_category, name='add_sentence_category'),
    path('add_grammer/', views.add_grammer, name='add_grammer'),
    path('add_grammer_test/', views.add_grammer_test, name='add_grammer_test'),
    path('add_grammer_category/', views.add_grammer_category, name='add_grammer_category'),
    
    path('nav_bar/', views.nav_bar, name='nav_bar'),  

    # List
    path('list_home_page/', views.list_home_page, name='list_home_page'),
    path('list_home_page/<int:top_cat_id>/', views.list_cat_home_page, name='list_cat_home_page'),
    re_path(r'^list_home_page/([0-9]+)/(?P<cat_id>[0-9]+)/$', views.category_list, name='category_list'),

    path('list_sentence_home_page/', views.list_sentence_home_page, name='list_sentence_home_page'),
    path('list_sentence_home_page/<int:top_cat_id>/', views.list_sentence_cat_home_page, name='list_sentence_cat_home_page'),
    re_path(r'^list_sentence_home_page/([0-9]+)/(?P<cat_id>[0-9]+)/$', views.category_sentence_list, name='category_sentence_list'),

    path('list_grammer_home_page/', views.list_grammer_home_page, name='list_grammer_home_page'),
    path('list_grammer_home_page/<int:top_cat_id>/', views.list_grammer_cat_home_page, name='list_grammer_cat_home_page'),
    re_path(r'^list_grammer_home_page/([0-9]+)/(?P<cat_id>[0-9]+)/$', views.category_grammer_list, name='category_grammer_list'),

    # Practice

    path('practice_home_page/', views.practice_home_page, name='practice_home_page'),
    path('practice_home_page/<int:top_cat_id>/', views.practice_cat_home_page, name='practice_cat_home_page'),
    # re_path(r'^practice_home_page/([0-9]+)/(?P<cat_id>[0-9]+)/$', views.practice, name='practice'),
    # re_path(r'^practice_home_page/([0-9]+)/([0-9]+)/start/$', views.voca_test_start, name='voca_test_start'),
    # #re_path(r'^practice_home_page/([0-9]+)/(?P<cat_id>[0-9]+)/start/(?P<translate>[0-1])/$', views.voca_test_start, name='voca_test_start'),
    # re_path(r'^practice_home_page/([0-9]+)/(?P<cat_id>[0-9]+)/listening/(?P<voca_id>[0-9]+)/$', views.voca_listening, name='voca_listening'),
    # re_path(r'^practice_home_page/([0-9]+)/(?P<cat_id>[0-9]+)/translating/(?P<voca_id>[0-9]+)/$', views.voca_translating, name='voca_translating'),
    # re_path('practice_sentence_home_page/category/voca_result/', views.voca_result, name='voca_result'),
    
    path('practice_home_page/category/<int:cat_id>/', views.practice, name='practice'),
    path('practice_home_page/category/<int:cat_id>/start/<int:translate>', views.voca_test_start, name='voca_test_start'),
    path('practice_home_page/category/listening/<int:voca_id>/', views.voca_listening, name='voca_listening'),
    path('practice_home_page/category/translating/<int:voca_id>/', views.voca_translating, name='voca_translating'),
    path('practice_sentence_home_page/category/voca_result/', views.voca_result, name='voca_result'),
    

    path('practice_sentence_home_page/', views.practice_sentence_home_page, name='practice_sentence_home_page'),
    path('practice_sentence_home_page/<int:top_cat_id>/', views.practice_sentence_cat_home_page, name='practice_sentence_cat_home_page'),
    path('practice_sentence_home_page/category/<int:cat_id>/', views.sent_practice, name='sent_practice'),
    path('practice_sentence_home_page/category/<int:cat_id>/start/<int:translate>', views.sent_test_start, name='sent_test_start'),
    # path('practice_sentence_home_page/category/londond_hearts/', views.londond_hearts, name='londond_hearts'),
    path('practice_sentence_home_page/category/listening/<int:sent_id>/', views.sent_listening, name='sent_listening'),
    path('practice_sentence_home_page/category/translating/<int:sent_id>/', views.sent_translating, name='sent_translating'),
    path('practice_sentence_home_page/category/sent_result/', views.sent_result, name='sent_result'),

    
    path('practice/<int:voca_or_sent_id>/<int:voca>/<int:translate>/pass/', views.test_pass, name='test_pass'),
    path('practice/<int:voca_or_sent_id>/<int:voca>/<int:translate>/fail/', views.test_fail, name='test_fail'),
    path('practice/<int:voca>/<int:translate>/again/', views.test_again, name='test_again'),

#     path('practice_overview/', views.practice_overview, name='practice_overview'),
]