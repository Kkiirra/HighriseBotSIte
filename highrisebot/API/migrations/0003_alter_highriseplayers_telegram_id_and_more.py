# Generated by Django 5.0.4 on 2024-04-29 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_botmoderator_banned_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highriseplayers',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='highriseplayers',
            name='user_id',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='highriseplayers',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]