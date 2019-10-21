from django.db import models
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.apps import apps

class Chatbot(models.Model):
    bot = None
    @classmethod
    def get_ChatBot(self):
        if self.bot is None:
            self.bot = ChatBot('Norman')
            trainer = ChatterBotCorpusTrainer(self.bot)
            trainer.train("chatterbot.corpus.english")
        return self.bot
    # @classmethod
    # def load(cls):
    #     try:
    #         return cls.objects.get()
    #     except cls.DoesNotExist:
    #         return cls()
