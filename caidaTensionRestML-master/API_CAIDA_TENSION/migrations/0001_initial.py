# Generated by Django 3.0.2 on 2020-01-19 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosCalculoCTModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga', models.FloatField()),
                ('temperatura', models.FloatField()),
                ('ct', models.FloatField()),
            ],
        ),
    ]