from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'person'

    def __str__(self):
        return self.name


from polls.models import Polls


class PersonPolls(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)

    class Meta:
        db_table = 'person_polls'

    def __str__(self):
        return self.poll
