from django.shortcuts import render
from .models import EboardMember, Event, Announcement

# Create your views here.
def index(request):
    announcements = Announcement.objects.all().order_by('post_date')
    return render(request, template_name='index.html', context={'announcements': announcements})


def about(request):
    return render(request, template_name='about.html')


def events(request):
    all_events = Event.objects.all().order_by('dt')
    return render(request, template_name='events.html', context={'events': all_events})


def sort_members(collection):
    ls = [None] * 10
    for m in collection:
        ls[int(m.position)] = m
    return ls


def eboard(request):
    eboard_members = EboardMember.objects.all()
    eboard_members = sort_members(eboard_members)

    return render(request, template_name='eboard.html', context={'eboard': eboard_members})
