from django.db import models

class TelegramUser(models.Model):
    chat_id = models.CharField(max_length=15)

class TelegramOption(models.Model):
    OPTION_1 = 0
    OPTION_2 = 1
    OPTION_3 = 2
    CHOICES = ((OPTION_1,'OPTION_1'),(OPTION_2,'OPTION_2'),(OPTION_3,'OPTION_3'))
    choice = models.IntegerField(choices=CHOICES)
    chat = models.ForeignKey(TelegramUser, on_delete=models.PROTECT)


