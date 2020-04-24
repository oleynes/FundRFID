from django.shortcuts import render
from .forms import MemberForm
# Create your views here.


def register(request):
    if request.method == 'GET':
        form = MemberForm()
        return render(request, context={'form':form}, template_name='register.html')
    elif request.method == 'POST':
        member = MemberForm(request.POST)
        if member.is_valid():
            member.save()
