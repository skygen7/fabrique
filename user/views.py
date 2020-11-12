from django.shortcuts import render, redirect
from .forms import UserName
from .models import Person
from polls.models import Polls, Questions


def index(request):
    form = UserName(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data.get('name')

            if not Person.objects.filter(name=data).first():
                query = Person.objects.create(name=data)
                query.save()

            info = Person.objects.filter(name=data).first()

            return redirect(f'/user/{info.id}')

        query = Person.objects.create(name=None)
        query.save()
        info = Person.objects.values('id').order_by('-id').first()
        return redirect(f'/user/{info.id}')
    return render(request, 'user/index.html', {'form': form})


def person(request, person_id):
    name = 'Stranger'
    info = Person.objects.filter(id=person_id).first()
    if info.name:
        name = info.name
    request.session['person_id'] = person_id
    return render(request, 'user/person.html', context={'name': name, 'id': person_id})


def person_polls(request, person_id):
    query = Polls.objects.filter(personpolls__person=person_id).values('id', 'name')
    return render(request, 'user/person_polls.html', context={'query': query, 'id': person_id})


def person_answers(request, person_id, poll_id):
    poll = Polls.objects.filter(id=poll_id).first()
    name = poll.name
    description = poll.description

    query = Questions.objects.filter(useranswer__poll=poll_id,
                                     useranswer__user=person_id,
                                     ).values('title', 'useranswer__answer', 'correctanswer__answer',
                                              'useranswer__result',)

    count = range(1, query.count() + 1)
    zip_data = zip(count, query)
    return render(request, 'user/answers.html', context={
        'name': name, 'description': description, 'zip_data': zip_data, 'person_id': person_id
    })


def person_poll_error(request):
    person_id = request.session.get('person_id')
    return render(request, 'user/person_poll_error.html', context={'id': person_id})