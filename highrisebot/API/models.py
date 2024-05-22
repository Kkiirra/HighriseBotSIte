from django.contrib.auth import get_user_model
from django.db import models


class BotModerator(models.Model):
    MUTE = 'mute'
    BAN = 'ban'
    KICK = 'kick'
    WARN_MODE_CHOICES = [
        (MUTE, 'Mute'),
        (BAN, 'Ban'),
        (KICK, 'Kick'),
    ]
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    api_key = models.CharField(max_length=64)
    room_id = models.CharField(max_length=30)
    welcome = models.BooleanField(default=True)
    set_welcome = models.TextField(default="Добро пожаловать!")
    warnmode = models.CharField(max_length=10, choices=WARN_MODE_CHOICES, default=MUTE)
    warnlimit = models.IntegerField(default=3)
    warntime = models.IntegerField(default=24)
    mute_duration = models.IntegerField(default=24)
    defaultfilter = models.BooleanField(default=True)
    banned_users = models.ManyToManyField('HighrisePlayers', related_name='banned_by_bots', blank=True)

    ignorewords = models.TextField(blank=True)
    filter_words = models.TextField(blank=True)

    def __str__(self):
        return f'{self.owner}: {self.room_id}'


class HighrisePlayers(models.Model):
    username = models.CharField(max_length=30, unique=True)
    user_id = models.CharField(max_length=30, unique=True)
    telegram_id = models.CharField(max_length=30, blank=True, unique=True)
    is_scam = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}: {self.is_scam}'
