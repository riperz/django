from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from pybox.forms import UserRegistrationForm


def thanks(request, name):
    return HttpResponse('Thank you {}, your registration is successful!'.format(name))


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']

            if form.cleaned_data['signup_to_newsletter']:
                print('Signed up {} to the newsletter'.format(form.cleaned_data['email']))

            return HttpResponseRedirect(reverse('thanks', args=[name]))
    else:
        form = UserRegistrationForm()
    return render(request, 'pypymusic/user_registration.html', {'form': form})
