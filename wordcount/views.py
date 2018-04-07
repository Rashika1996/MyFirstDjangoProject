from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html',{'HiThere':'Count as many words You want!!'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    uniqueword = {}
    for word in wordlist:
        try:
            uniqueword[word]+=1
        except:
            uniqueword[word] = 1
    sortedList = sorted(uniqueword.items(), key=operator.itemgetter(1),reverse = True)
    return render(request,'count.html',{'fulltext':fulltext,'wordcount': len(wordlist),'uniquewords':len(uniqueword),'inorderlist':sortedList})

def about(request):
    return render(request,'about.html')