# Generated by Django 4.1.3 on 2022-11-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=300)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
