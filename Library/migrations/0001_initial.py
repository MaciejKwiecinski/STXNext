# Generated by Django 2.2.4 on 2019-08-26 19:48

import Library.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Identyfires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('identifier', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authors', models.TextField()),
                ('publishedDate', models.IntegerField(validators=[Library.validators.MinYearValidator, Library.validators.MaxYearValidator])),
                ('pageCount', models.IntegerField(validators=[Library.validators.MinPagesValidator])),
                ('imageLinks', models.TextField()),
                ('language', models.TextField()),
                ('industryIdentifiers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Identyfires')),
            ],
        ),
    ]
