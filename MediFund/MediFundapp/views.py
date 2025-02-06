from django.shortcuts import render

def lead(request):
    return render(request, 'lead.html')  # This will look for a 'home.html' template

