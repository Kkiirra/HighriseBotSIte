# Generated by Django 5.0.4 on 2024-04-29 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botmoderator',
            name='banned_users',
            field=models.ManyToManyField(blank=True, related_name='banned_by_bots', to='API.highriseplayers'),
        ),
    ]