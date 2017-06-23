from django.shortcuts import render, redirect
from . models import User
from django.core.validators import ValidationError


# Create your views here.

def register(request):
    context = {}
    if request.POST['password'] != request.POST['password_confirm']:
        context['password_confirm'] = "No"
    new_user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
    try:
        new_user.full_clean()
    except ValidationError as err:
        for key in err:
            context[key[0]] = key[1][0]
    if context == {}:
            new_user.save()
            return redirect('/success')
    else:
        request.session['context'] = context
        return redirect('/')

def success(request):
    return render(request, "login_app/success.html")

def index(request):
    print "i am index"
    try:
        context = request.session['context']
        request.session.pop('context')
    except:
        context = {}
    return render(request, 'login_app/index.html', context)
