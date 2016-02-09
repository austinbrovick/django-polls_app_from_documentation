from __future__ import unicode_literals

from django.db import models

import datetime

from django.utils import timezone

# each class variable represents a database field in the model
# some field classes require arguements
  # like CharField which requires a max_length arg

class Question(models.Model):  # Question class inherits from models.Model
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
      return self.question_text
    def was_published_recently(self):
      now = timezone.now()
      return now - datetime.timedelta(days=1) <= self.pub_date <= now





class Choice(models.Model): # Choice class inherits from models.Model
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # sets default value to 0
    def __str__(self):
      return self.choice_text

