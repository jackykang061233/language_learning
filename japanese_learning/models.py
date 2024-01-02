from django.db import models
from django.utils import timezone
import datetime

class Top_Category(models.Model):
    cat = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.cat

class Category(models.Model):
    cat = models.CharField(max_length=50, blank=False)
    top_cat = models.ForeignKey(Top_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.cat

class Vocabulary(models.Model):
    forgetting_curve_days = [0, 1, 2, 3, 5, 10, 30 ,60, 90]
    STATUS_choices = [(i, i) for i in forgetting_curve_days]
    Next_status = {0:1, 1:2, 2:3, 3:5, 5:10, 10:30, 30:60 , 60:90}

    jp = models.CharField(max_length=50, blank=False)
    kanji = models.CharField(max_length=50, blank=False)
    zh = models.CharField(max_length=50, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    example_sentence = models.TextField(max_length=300, blank=True, default='')
    listening_status = models.PositiveSmallIntegerField(choices=STATUS_choices, default=0)
    listening_next_to_learn = models.DateField(default=timezone.now)
    translating_status = models.PositiveSmallIntegerField(choices=STATUS_choices, default=0)
    translating_next_to_learn = models.DateField(default=timezone.now)

    def __str__(self):
        return self.jp

class Top_Sentence_Category(models.Model):
    cat = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.cat

class Sentence_Category(models.Model):
    cat = models.CharField(max_length=50, blank=False)
    top_cat = models.ForeignKey(Top_Sentence_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.cat

class Sentence(models.Model):
    forgetting_curve_days = [0, 1, 2, 3, 5, 10, 30 ,60, 90]
    # STATUS_choices = [(i, i) for i in forgetting_curve_days]
    # Next_status = {0:1, 1:2, 2:3, 3:5, 5:10, 10:30, 30:60 , 60:90}

    kanji = models.CharField(max_length=200, blank=False)
    jp = models.CharField(max_length=200, blank=False)
    zh = models.CharField(max_length=200, blank=False)
    category = models.ForeignKey(Sentence_Category, on_delete=models.CASCADE)
    # listening_status = models.PositiveSmallIntegerField(choices=STATUS_choices, default=0)
    # listening_next_to_learn = models.DateField(default=timezone.now)
    # translating_status = models.PositiveSmallIntegerField(choices=STATUS_choices, default=0)
    # translating_next_to_learn = models.DateField(default=timezone.now)

    def __str__(self):
        return self.jp

class Top_Grammer_Category(models.Model):
    cat = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.cat

class Grammer_Category(models.Model):
    cat = models.CharField(max_length=50, blank=False)
    top_cat = models.ForeignKey(Top_Grammer_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.cat

class Grammer(models.Model):
    title = models.CharField(max_length=50, blank=False)
    explanation = models.TextField(max_length=1000, blank=True)
    category = models.ForeignKey(Grammer_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Grammer_Test(models.Model):
    forgetting_curve_days = [0, 1, 2, 3, 5, 10, 30 ,60, 90]
    STATUS_choices = [(i, i) for i in forgetting_curve_days]
    Next_status = {0:1, 1:2, 2:3, 3:5, 5:10, 10:30, 30:60 , 60:90}

    question = models.TextField(max_length=300, blank=False)
    category = models.ForeignKey(Grammer, on_delete=models.CASCADE)
    solution = models.TextField(max_length=300, blank=False)

    learning_status = models.PositiveSmallIntegerField(choices=STATUS_choices, default=0)
    next_to_learn = models.DateField(default=timezone.now)


    # kanji = models.CharField(max_length=50, blank=False)
    # jp = models.CharField(max_length=50, blank=False)
    # zh = models.CharField(max_length=50, blank=False)
    
    # listening_status = models.PositiveSmallIntegerField(choices=STATUS_choices, default=0)
    # listening_next_to_learn = models.DateField(default=timezone.now)
    # translating_status = models.PositiveSmallIntegerField(choices=STATUS_choices, default=0)
    # translating_next_to_learn = models.DateField(default=timezone.now)

    def __str__(self):
        return self.solution



