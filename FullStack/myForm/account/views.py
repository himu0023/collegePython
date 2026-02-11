from django.shortcuts import render, redirect
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            return redirect("/account/success/")
    else:
        form = RegisterForm()

    return render(request, "account/register.html", {"form": form})


def success_view(request):
    return render(request, "account/success.html")