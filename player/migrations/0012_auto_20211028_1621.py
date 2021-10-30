# Generated by Django 3.2.7 on 2021-10-28 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0011_auto_20211026_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='status',
            new_name='approved',
        ),
        migrations.AlterField(
            model_name='player',
            name='coach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coach', to='player.coach'),
        ),
        migrations.AlterField(
            model_name='playerimage',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playerimage', to='player.player'),
        ),
        migrations.AlterField(
            model_name='point',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playerpoint', to='player.player'),
        ),
    ]
