# Generated by Django 2.2.4 on 2019-08-28 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='pageCount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='publishedDate',
            field=models.IntegerField(),
        ),
    ]
