from django.contrib import admin

from .models import Flashcards, Flashcard_Text

class FlashcardsAdmin(admin.ModelAdmin):
    list_display = ('word', 'next_to_learn')

class FlashcardTextAdmin(admin.ModelAdmin):
    list_display = ('text_id', 'title', 'language')

admin.site.register(Flashcards, FlashcardsAdmin)

admin.site.register(Flashcard_Text, FlashcardTextAdmin)
