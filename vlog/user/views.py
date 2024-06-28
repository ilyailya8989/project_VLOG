from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from user.forms import SignUpForm, SingInForm


def singup(request):
    if request.user.is_authenticated:
        return redirect('info_category')
    sign_form = SignUpForm()
    if request.method == 'POST':
        sign_form = SignUpForm(request.POST)
        if sign_form.is_valid():
            user = sign_form.save()
            login(request, user)
            return redirect('info_category')
    return render(request, 'user/register.html', {'form': sign_form})

def singin(request):
    if request.user.is_authenticated:
        return redirect('info_category')
    sign_form = SingInForm()
    if request.method == 'POST':
        sign_form = SingInForm(request.POST)
        if sign_form.is_valid():
            user_name = sign_form.cleaned_data['username']
            password = sign_form.cleaned_data['password']
            user =authenticate(request, username=user_name, password=password)
            if user:
                login(request, user)
                return redirect('info_category')
    return render(request, 'user/autorisation.html', {'form': sign_form})

