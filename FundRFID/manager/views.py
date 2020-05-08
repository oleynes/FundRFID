from django.shortcuts import render
from django.contrib import messages
from .forms import MemberForm, LookupForm
from .models import Member
from django.shortcuts import redirect
import pdb
# Create your views here.


def register(request):
    if request.method == 'GET':
        form = MemberForm()
        return render(request, context={'form':form}, template_name='register.html')
    elif request.method == 'POST':
        member = MemberForm(request.POST)

        if member.is_valid():
            print('inside member valid')
            post = member.save(commit=False)
            post.save()
            messages.add_message(request, messages.INFO, 'Form Submitted Successfully! Use the Fundrace Lookup page '
                                                         'to check your score!')
            return redirect('/')
        else:

            print('member was invalid')
            messages.add_message(request, messages.INFO, 'Something went wrong, maybe try again in a few minutes?')
            return render(request, context={'form': MemberForm()}, template_name='register.html')

    else:
        form = MemberForm()
        return render(request, context={'form': form}, template_name='register.html')


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