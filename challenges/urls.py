from django.urls import path
from . import views

urlpatterns = [
  # path("january", views.january),
  # path("february", views.february),
  # path("march", views.march),
  path("", views.index), # trigger for /challenges/
  path("<int:month_name>", views.monthly_challenges_by_number),
  path("<str:month_name>", views.monthly_challenge, name="month-challenge")
]