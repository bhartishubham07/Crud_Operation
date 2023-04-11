from django.shortcuts import render
from django.db.models.functions import Length

# Create your views here.
from app.models import *

def Show_Topic(request):
    LOT = Topic.objects.all()
    d = {'topics' : LOT}
    return render(request, 'Show_Topic.html', context=d)

def Show_Webpage(request):
    LOW = Webpage.objects.all()
    LOW = Webpage.objects.filter(topic_name='CRICKET')
    LOW = Webpage.objects.exclude(topic_name='FOOTBALL')
    LOW = Webpage.objects.all().order_by('topic_name')
    LOW = Webpage.objects.all().order_by('-topic_name')
    LOW = Webpage.objects.all().order_by(Length('topic_name'))
    LOW = Webpage.objects.all().order_by(Length('topic_name').desc())
    
    d = {'wdetails' : LOW}
    return render(request, 'Show_Webpage.html', d)

def Show_Records(request):
    LOA = AccessRecords.objects.all()
    LOA = AccessRecords.objects.filter(date__gt ='2023-03-27')
    LOA = AccessRecords.objects.filter(date__gte ='2023-03-27')
    LOA = AccessRecords.objects.filter(date__lt ='2023-03-27')
    LOA = AccessRecords.objects.filter(date__lte ='2023-03-27')
    LOA = AccessRecords.objects.all()
    
    d = {'Records' : LOA}
    return render(request, 'Show_Records.html', d)
