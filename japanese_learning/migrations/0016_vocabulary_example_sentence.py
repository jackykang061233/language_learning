# Generated by Django 4.0.3 on 2022-07-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('japanese_learning', '0015_grammer_top_grammer_category_alter_category_top_cat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabulary',
            name='example_sentence',
            field=models.TextField(blank=True, default='1', max_length=300),
        ),
    ]
