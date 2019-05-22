from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return HttpResponse('Hi Welcome to Django')


def eggs(request):
    return HttpResponse('<h1>EGGS<h1>')


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html', {'hithere': 'This is me'})


def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            # Increase
            worddictionary[word] += 1
        else:
            # add to the dictionary
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1),reverse= True)
    return render(request, 'count.html',
                  {'fulltext': fulltext, 'count': len(wordlist), 'worddictionary': worddictionary, 'worddictionary_items': worddictionary.items(),
                   'sortedwords': sortedwords})
