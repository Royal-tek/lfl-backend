# Generated by Django 3.2.7 on 2021-10-25 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0008_alter_userteam_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userteam',
            name='team',
            field=models.ManyToManyField(max_length=2, to='player.Player'),
        ),
    ]
