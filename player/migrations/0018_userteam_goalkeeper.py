# Generated by Django 3.2.7 on 2021-11-25 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0017_auto_20211125_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='userteam',
            name='goalkeeper',
            field=models.ManyToManyField(related_name='goalkeeper', to='player.Player'),
        ),
    ]