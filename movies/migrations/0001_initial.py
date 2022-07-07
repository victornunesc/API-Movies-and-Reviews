# Generated by Django 4.0.6 on 2022-07-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('duration', models.CharField(max_length=10)),
                ('premiere', models.DateField()),
                ('classification', models.IntegerField()),
                ('synopsis', models.TextField()),
                ('genres', models.ManyToManyField(to='movies.genre')),
            ],
        ),
    ]