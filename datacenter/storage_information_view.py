from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone

STRANGE_DURATION = 3600 # seconds

def get_duration(visit):
  if visit.leaved_at == None:
    end_date = timezone.now()
  else:
    end_date = visit.leaved_at

  duration = end_date - visit.entered_at

  return duration

def is_visit_long(visit):
  duration = get_duration(visit)

  return duration.seconds > STRANGE_DURATION

def storage_information_view(request):

  non_closed_visits = []

  visits = Visit.objects.filter(leaved_at=None)
  for visit in visits:
    non_closed_visits.append(
      {
        "who_entered": visit.passcard,
        "entered_at": visit.entered_at,
        "duration": get_duration(visit),
        "is_strange": is_visit_long(visit),
      }
    )  

  context = {
      "non_closed_visits": non_closed_visits,  # не закрытые посещения
  }
  
  return render(request, 'storage_information.html', context)
