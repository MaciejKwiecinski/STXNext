# Generated by Django 2.2.4 on 2019-08-30 19:46

import Library.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='imageLinks',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='language',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='pageCount',
            field=models.IntegerField(blank=True, validators=[Library.validators.MinPagesValidator]),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='publishedDate',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='identyfires',
            name='identifier',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='identyfires',
            name='type',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]