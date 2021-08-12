from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no Meat",
    "february": "Walk for 20 minutes!",
    "march": "Learn Django for at least 20 minutes daily!",
    "april": "Learn Django for at least 20 minutes daily!",
    "may": "Walk for 20 minutes!",
    "june": "Walk for 20 minutes!",
    "july": "Eat no Meat",
    "august": "Eat no Meat",
    "september": "Learn Django for at least 20 minutes daily!",
    "october": "Learn Django for at least 20 minutes daily!",
    "november": "November",
    "december": None
}
# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month,
        })
    except:
        raise Http404()
