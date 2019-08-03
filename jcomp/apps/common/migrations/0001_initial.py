# Generated by Django 2.2.2 on 2019-08-03 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kanji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hiragana', models.CharField(blank=True, max_length=50, null=True)),
                ('romaji', models.CharField(blank=True, max_length=100, null=True)),
                ('translation', models.CharField(max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(default='slug')),
                ('kanji', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='kanji.Kanji')),
            ],
            options={
                'verbose_name': 'Palabra',
                'verbose_name_plural': 'Palabras',
                'ordering': ['-id'],
            },
        ),
    ]
