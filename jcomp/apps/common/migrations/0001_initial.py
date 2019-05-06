# Generated by Django 2.2.1 on 2019-05-01 15:48

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
                ('lecture', models.CharField(max_length=50)),
                ('kanji', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kanji.Kanji')),
            ],
        ),
    ]
