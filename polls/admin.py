from django.contrib import admin
from .models import Polls, Questions, PollQuestions, CorrectAnswer, UserAnswer


admin.site.register(Polls)
admin.site.register(Questions)
admin.site.register(PollQuestions)
admin.site.register(CorrectAnswer)
admin.site.register(UserAnswer)
