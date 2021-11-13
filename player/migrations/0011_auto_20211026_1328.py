# Generated by Django 3.2.7 on 2021-10-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0010_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]