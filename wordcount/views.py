from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddict = {}

    for words in wordlist:
        if words in worddict:
            #Increment words by 1#
            worddict[words] += 1

            
        else:
            #Add new word#
            worddict[words] = 1

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddict':worddict.items()})