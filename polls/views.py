from django.shortcuts import render, redirect
from .models import Polls, Questions, CorrectAnswer, UserAnswer
from .forms import Answer
from user.models import PersonPolls


def index(request):
    polls = Polls.objects.values('id', 'name')
    person_id = request.session.get('person_id')
    return render(request, 'polls/index.html', context={'polls': polls, 'person_id': person_id})


def poll(request, poll_id):
    poll_one = Polls.objects.filter(id=poll_id).first()

    if request.method == 'POST':
        person_id = request.session.get('person_id')
        if person_id:
            res = PersonPolls.objects.filter(poll_id=poll_id, person_id=person_id).first()
            if res:
                return redirect('/user/poll-error')

            query = PersonPolls.objects.create(person_id=person_id, poll_id=poll_id)
            query.save()

            return redirect(f'/polls/{poll_id}/questions')
        return redirect('/user')

    return render(request, 'polls/poll.html', context={
        'id': poll_one.id,
        'name': poll_one.name,
        'start_time': poll_one.start_time,
        'end_time': poll_one.end_time,
        'description': poll_one.description
    })


def questions(request, poll_id):
    query = Questions.objects.filter(pollquestions__polls=poll_id).values('id', 'title')
    zip_data = zip(range(1, query.count() + 1), query)
    person_id = request.session.get('person_id')
    return render(request, 'polls/questions.html', context={'person_id': person_id, 'zip_data': zip_data})


def question(request, poll_id, que_id):
    person_id = request.session.get('person_id')
    person_ans = UserAnswer.objects.filter(question_id=que_id, user_id=person_id, poll_id=poll_id).first()
    if person_ans:
        return redirect(f'/polls/{poll_id}/questions/{que_id}/answer-err')

    form = ''
    ques = Questions.objects.filter(id=que_id).first()

    if ques.type == 'one correct':
        answers = CorrectAnswer.objects.filter(question_id=que_id).first()
        for answer in answers.possibilities.split(','):
            form += f'<p><input name="answer" type="radio" value="{answer}"> {answer}</p>'

    if ques.type == 'multiple choice':
        answers = CorrectAnswer.objects.filter(question_id=que_id).first()
        for answer in answers.possibilities.split(','):
            form += f'<p><input type="checkbox" name="answer" value="{answer}"> {answer}</p>'

    if ques.type == 'text':
        form = Answer(request.POST or None)

    if request.method == "POST":
        data = request.POST.getlist('title') or request.POST.getlist('answer')
        str_data = ', '.join(map(lambda x: x.strip(), data))
        user_id = request.session.get('person_id')
        ques = CorrectAnswer.objects.filter(question_id=que_id).first()

        if set(str_data) == set(ques.answer):
            result = True
        else:
            result = False

        query = UserAnswer.objects.create(
            answer=str_data, question_id=que_id, user_id=user_id, poll_id=poll_id, result=result)
        query.save()
        return redirect(f'/polls/{poll_id}/questions/{que_id}/accept')

    return render(request, 'polls/question.html', context={
        'id': que_id, 'question': ques, 'form': form, 'poll': poll_id
    })


def accept_answer(request, poll_id, que_id):
    return render(request, 'polls/accept_answer.html', context={'poll_id': poll_id})


def answer_err(request, poll_id, que_id):
    return render(request, 'polls/answer-err.html', context={'poll_id': poll_id, 'que_id': que_id})
