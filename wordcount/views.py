from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']

    wordlist= fulltext.split()
    worddictonary={}
    for word in wordlist:
        if word in worddictonary:
            worddictonary[word]+=1
        else:
            worddictonary[word]=1
        sortedwords=sorted(worddictonary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
def about(request):
    return render(request,'about.html')
