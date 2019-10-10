import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here
class Question(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, default=None
    )
    question_text = models.CharField(max_length=200)
    created = models.DateTimeField('created', default=timezone.now)
    updated = models.DateTimeField('updated', default=timezone.now)
    state = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created <= now

    was_published_recently.admin_order_field = 'created'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, default=None
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
        
    created = models.DateTimeField('created', default=timezone.now)
    updated = models.DateTimeField('updated', default=timezone.now)

class Vote(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, default=None
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created = models.DateTimeField('created', default=timezone.now)
    updated = models.DateTimeField('updated', default=timezone.now)