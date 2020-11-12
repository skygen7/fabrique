from django.db import models
from user.models import Person


class Polls(models.Model):
    name = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()

    class Meta:
        db_table = 'polls'

    def __str__(self):
        return f'{self.name}, {self.start_time}, {self.end_time}, {self.description}'


class Questions(models.Model):
    title = models.TextField()
    type = models.TextField()

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return self.title


class PollQuestions(models.Model):
    polls = models.ForeignKey(Polls, on_delete=models.CASCADE)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)

    class Meta:
        db_table = 'poll_questions'


class CorrectAnswer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.TextField()
    possibilities = models.TextField(null=True)

    def __str__(self):
        return self.answer

    class Meta:
        db_table = 'correct_answer'


class UserAnswer(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    answer = models.TextField()
    result = models.BooleanField(null=False)

    class Meta:
        db_table = 'user_answer'

    def __str__(self):
        return self.answer
