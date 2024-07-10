from django.shortcuts import get_object_or_404
from django.shortcuts import render

from rhs_soccer.matches.models import Match
from rhs_soccer.matches.models import Highlight


def matches(request):
    matches = Match.objects.upcoming()
    upcoming = bool(matches.exists())
    context = {
        "matches": matches,
        "title": "Upcoming Matches",
        "upcoming": upcoming,
    }
    return render(request, "matches/matches.html", context)


def past_matches(request):
    matches = Match.objects.finished()
    finished = bool(matches.exists())
    context = {
        "matches": matches,
        "title": "Past Matches",
        "finished": finished,
    }
    return render(request, "matches/matches.html", context)


def today_matches(request):
    matches = Match.objects.today()
    today = bool(matches.exists())
    context = {
        "matches": matches,
        "title": "Today's Matches",
        "today": today,
    }
    return render(request, "matches/matches.html", context)


def match(request, match_id):
    match = get_object_or_404(Match, uuid=match_id)
    context = {
        "match": match,
        "title": match,
    }
    return render(request, "matches/match.html", context)
