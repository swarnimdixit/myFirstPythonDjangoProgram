
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def count(request):
    if request.GET['fulltext'] != '':
        fulltext = request.GET['fulltext'].strip()
        if fulltext != '':
            wordList = fulltext.split(' ')
            wordCount = len(wordList)
        else:
            wordCount = 0
    else: 
        wordCount = 0

    return render(request, 'count.html', {'wordcount': '66'})

