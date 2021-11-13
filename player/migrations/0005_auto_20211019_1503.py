# Generated by Django 3.2.7 on 2021-10-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_alter_coach_code_team_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='assists',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='goals',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='minutes_played',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='redcard',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='yellowcard',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default=0, max_length=10, null=True),
        ),
    ]