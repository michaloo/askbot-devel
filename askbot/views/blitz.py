from django.shortcuts import render
def index(request):#generates front page - shows listing of questions sorted in various ways
    """index view mapped to the root url of the Q&A site"""
    return render(request, 'blitz.html')