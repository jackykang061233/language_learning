from django.contrib import admin

from .models import Category, Vocabulary, Sentence, Sentence_Category, Top_Category, Top_Sentence_Category, Grammer_Test, Grammer, Grammer_Category, Top_Grammer_Category

class VocaAdmin(admin.ModelAdmin):
    list_display = ('jp', 'kanji', 'zh', 'category')

class CateAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat', )

class SenAdmin(admin.ModelAdmin):
    # list_display = ('kanji', 'listening_next_to_learn', 'translating_next_to_learn', 'category')
    list_display = ('kanji', 'category')

class SenCatAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat', )

class GrammerAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')

class GrammerTestAdmin(admin.ModelAdmin):
    list_display = ('solution', )

class GrammerCatAdmin(admin.ModelAdmin):
    list_display = ('cat', )

class TopCatAdmin(admin.ModelAdmin):
    list_display = ('cat', )

class TopSenCatAdmin(admin.ModelAdmin):
    list_display = ('cat', )

class TopGrammerCatAdmin(admin.ModelAdmin):
    list_display = ('cat', )

admin.site.register(Category, CateAdmin)
admin.site.register(Vocabulary, VocaAdmin)
admin.site.register(Sentence, SenAdmin)
admin.site.register(Sentence_Category, SenCatAdmin)
admin.site.register(Top_Category, TopCatAdmin)
admin.site.register(Top_Sentence_Category, TopSenCatAdmin)
admin.site.register(Grammer, GrammerAdmin)
admin.site.register(Grammer_Test, GrammerTestAdmin)
admin.site.register(Grammer_Category, GrammerCatAdmin)
admin.site.register(Top_Grammer_Category, TopGrammerCatAdmin)