from django.shortcuts import render

def dashboard (requirements):
    return render(requirements, 'dashboard.html')
