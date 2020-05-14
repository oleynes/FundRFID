from manager.models import Member
from django.db.models import F
from django.http import JsonResponse


# Create your views here.
def update_cli(request, tag_id, score):
    member = Member.objects.get(tag_UID=tag_id)
    member.score = F('score') + score
    try:
        member.save()
        return JsonResponse({'status': True})
    except:
        return JsonResponse({'status': False})
