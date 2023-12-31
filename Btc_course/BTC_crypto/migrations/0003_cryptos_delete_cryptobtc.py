# Generated by Django 4.1.7 on 2023-06-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BTC_crypto', '0002_alter_cryptobtc_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=10)),
                ('price', models.FloatField(max_length=256)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='CryptoBTC',
        ),
    ]
