# Generated by Django 4.1.7 on 2023-06-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoBTC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('price', models.FloatField(max_length=256)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
