from django.db import models
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
User = get_user_model()

import misaka

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=225)
    intro_text = models.TextField(null=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField(auto_now=True, null=True)


class Question(models.Model):
    user = models.ForeignKey(User, related_name="question", default='')
    quiz = models.ForeignKey(Quiz, related_name='quiz',default='', blank=True, null=True)
    question = models.TextField(unique=False, default='')
    question_html = models.TextField(default='')
    date_created = models.DateTimeField(auto_now=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    answer = models.TextField(default='')
    answer_html = models.TextField(unique=False, default='')
    # message = models.TextField(unique=False, default='')
    # message_html = models.TextField(editable=False, default='')

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        self.question_html = misaka.html(self.question)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "questions:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        # ordering = ["-created_at"]
        unique_together = ["user", "question", "answer", ]



class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.TextField(unique=False)
    answer_html = models.TextField()
    correct = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)


