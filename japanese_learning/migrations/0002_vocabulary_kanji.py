# Generated by Django 4.0.3 on 2022-06-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('japanese_learning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabulary',
            name='kanji',
            field=models.CharField(default='家族', max_length=50),
        ),
    ]