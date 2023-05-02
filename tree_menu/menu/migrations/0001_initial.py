# Generated by Django 4.2 on 2023-05-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('ulr', models.CharField(max_length=255, verbose_name='Ссылка')),
                ('position', models.PositiveIntegerField(default=1, verbose_name='Позиция')),
            ],
        ),
    ]