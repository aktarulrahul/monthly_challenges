from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse

monthly_challenges = {
  "january": "Eat no meat for the entire month!",
  "february": "Walk for at least 20 minutes every day.",
  "march": "Learn Django for at least 20 minutes every day.",
  "april": "Walk for at least 40 minutes every day.",
  "may": "Eat no meat for the entire month!",
  "june": "Learn Django for at least 20 minutes every day.",
  "july": "Walk for at least 40 minutes every day.",
  "august": "Eat no meat for the entire month!",
  "september": "Eat no meat for the entire month!",
  "october": "Learn Django for at least 20 minutes every day.",
  "november": "Walk for at least 40 minutes every day.",
  "december": "Eat no meat for the entire month!",
}

def index(request):
  list_items = ""
  months = list(monthly_challenges.keys())
  for month in months:
    capitalized_month = month.capitalize()
    month_path = reverse("month-challenge", args=[month])
    list_items += f"<li><a href=\"{month_path}\">{capitalized_month}<a></li>"
  
  response_data = f"<ul>{list_items}</ul>"

  return HttpResponse(response_data)


# Create your views here.
# def january(request):
#   return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#   return HttpResponse("Walk for at least 20 minutes every day.")

# def march(request):
#   return HttpResponse("Learn Django for at least 20 minutes every day.")

def monthly_challenges_by_number(request, month_name):
  months = list(monthly_challenges.keys())
  if month_name > len(months):
    return HttpResponseNotFound('This month is not supported!')
  redirect_month = months[month_name - 1]
  redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/january
  # return HttpResponseRedirect("/challenges/"+redirect_month)
  return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month_name):
  # challenge_text = None
  # if month_name == 'january':
  #   challenge_text = 'Eat no meat for the entire month!'
  # elif month_name == 'february':
  #   challenge_text = 'Walk for at least 20 minutes every day.'
  # elif month_name == 'march':
  #   challenge_text = 'Learn Django for at least 20 minutes every day.'
  # elif month_name == 'may':
  #   challenge_text = 'We will decide later.'
  # else:
  #   return HttpResponseNotFound('This month is not supported!')
  try:
    challenge_text = monthly_challenges[month_name]
    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)
  except:
    return HttpResponseNotFound('<h1>This month is not supported!</h2>') 
