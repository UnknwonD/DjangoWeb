from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

# python manage.py startapp accountapp
# python manage.py runserver
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        #return render(request, 'accountapp/hello_world.html', context={'hello_world_list' : hello_world_list})
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    elif request.method == "GET":
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})