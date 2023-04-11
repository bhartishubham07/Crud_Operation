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

def Update_Webpage(request):
    Webpage.objects.filter(name='DHONI').update(url='https://www.dhoni.in')
    Webpage.objects.filter(name='VIRAT').update(url='https://www.vk18.in')
    Webpage.objects.filter(topic_name='CRICKET').update(url='https://www.vk18.in')
    Webpage.objects.update_or_create(name='DHONI', defaults={'url':'https://msdhoni.com'})
    T=Topic.objects.get_or_create(topic_name='CRICKET')[0]
    T.save()
    Webpage.objects.update_or_create(name='HARDIK',defaults={'topic_name':T,'url':'https://hardik.in'})
    
    d = {'wdetails' : Webpage.objects.all()}
    return render(request,'Show_Webpage.html', d)


def Delete_Webpage(request):
    Webpage.objects.filter(topic_name='CHESS').delete()
    
    d = {'wdetails' : Webpage.objects.all()}
    return render(request, 'Show_Webpage.html', d)
