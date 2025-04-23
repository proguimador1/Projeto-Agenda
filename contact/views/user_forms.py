from django.shortcuts import render, redirect
from contact.forms import RegisterForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()


    return render(
        request,
        'contact/register.html',
        {
            'form': form,
            'site_title': 'Register',
        }
    )