from django.shortcuts import render

from .models import *

# Create your views here.

def Subjects(request):
    
    all = Subject.objects.all()

    return render(request, 'b.html', {'all':all} )

def Chapter(request,chapter_id):

    chapters = Chapters.objects.all()
    # print(chapters)

    return render(request, 'chapters.html', {'chapters':chapters} )

def Topics(request, topic_id):
    
    topics = Topics.objects.all()
    print(topics)
    return render(request, 'topics.html', {'topics':topics} )

def Pages(request, page_id):
    
    pages = Pages.objects.get(id=page_id)
    print(pages)

    return render(request, 'pages.html', {'pages':pages} )

