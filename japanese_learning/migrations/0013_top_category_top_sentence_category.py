# Generated by Django 4.0.3 on 2022-06-16 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('japanese_learning', '0012_remove_vocabulary_next_to_learn_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Top_Sentence_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=50)),
            ],
        ),
    ]
