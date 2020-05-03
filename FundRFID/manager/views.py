from django.shortcuts import render
from django.contrib import messages
from .forms import MemberForm, LookupForm
from .models import Member
from django.shortcuts import redirect
# Create your views here.


def register(request):
    if request.method == 'GET':
        form = MemberForm()
        return render(request, context={'form':form}, template_name='register.html')
    elif request.method == 'POST':
        member = MemberForm(request.POST)
        if member.is_valid():
            member.save()
            messages.add_message(request, messages.INFO, 'Form Submitted Successfully! Use the Fundrace Lookup page '
                                                         'to check your score!')
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Something went wrong, maybe try again in a few minutes?')
            return redirect('/fundrace/register/')

    else:
        return redirect('/')


def lookup(request):
    if request.method == 'GET':
        form = LookupForm()
        return render(request, context={'form': form}, template_name='lookup.html')
    elif request.method == 'POST':
        form_data = LookupForm(request.POST)
        if form_data.is_valid():
            _id = form_data.cleaned_data['paws_id']
            member = Member.objects.get(pk=_id)
            return render(request, context={'score': member.score}, template_name='score.html')
        else:
            form = LookupForm()
            return render(request, context={'form': form}, template_name='lookup.html')
    else:
        return redirect('/')