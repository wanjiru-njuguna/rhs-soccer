from django.shortcuts import get_object_or_404
from django.shortcuts import render

from rhs_soccer.profiles.models import Coach
from rhs_soccer.profiles.models import Player


def coaches(request):
    coaches = Coach.objects.all()
    context = {
        "coaches": coaches,
        "title": "Coaches",
    }
    return render(request, "profiles/coaches.html", context)


def coach(request, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id)
    context = {
        "coach": coach,
    }
    return render(request, "profiles/coach.html", context)


def players(request):
    players = Player.objects.filter(is_published=True)
    context = {
        "players": players,
        "title": "Players",
    }
    return render(request, "profiles/players.html", context)


def player(request, id):
    player = get_object_or_404(Player, id=id)

    goal = 0
    raised = 0

    if player.team and player.team.fundraiser and player.team.fundraiser.is_active:
        goal = player.team.fundraiser.goal
        raised = player.team.fundraiser.raised
        percentage = (raised / goal) * 100 if goal > 0 else 0

    context = {
        "player": player,
        "goal": goal,
        "raised": raised,
        "percentage": percentage,
    }
    return render(request, "profiles/player.html", context)
