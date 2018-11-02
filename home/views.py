from django.shortcuts import render

def index(index):
    """A view that displays the index page"""
    return render(request, "index.html")
