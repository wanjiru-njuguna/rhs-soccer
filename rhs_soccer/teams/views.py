from django.shortcuts import get_object_or_404
from django.shortcuts import render

# from rhs_soccer.donations.models import Campaign
from rhs_soccer.teams.enums import TeamLevel
from rhs_soccer.teams.models import Team
from rhs_soccer.teams.models import TeamPage
from rhs_soccer.profiles.models import Player



def team_page(request):
    # fundraisers = Campaign.objects.filter(is_active=True)
    teams = Team.objects.filter(home_team=True)
    return render(
        request,
        "teams/teams.html",
        {
            # "fundraisers": fundraisers,
            "teams": teams,
            "title": "Our Teams",
        },
    )


def varsity_team(request):
    team = Team.objects.filter(level=TeamLevel.VARSITY, home_team=True).first()

    # fundraisers = Campaign.objects.filter(is_active=True)
    players = Player.objects.filter(team=team)
    return render(
        request,
        "teams/team.html",
        {
            "team": team,
            # "fundraisers": fundraisers,
            "players": players,
            "title": "RHS Boys Soccer - Varsity Team",
        },
    )


def jv_team(request):
    team = Team.objects.filter(level=TeamLevel.JV).first()
    team_page = TeamPage.objects.first()
    # fundraisers = Campaign.objects.filter(is_active=True)
    return render(
        request,
        "teams/jv.html",
        {
            "team": team,
            "team_page": team_page,
            # "fundraisers": fundraisers,
            "title": "RHS Boys Soccer - JV Team",
        },
    )


def freshman_team(request):
    team = Team.objects.freshman()
    team_page = TeamPage.objects.first()
    # fundraisers = Campaign.objects.filter(is_active=True)
    return render(
        request,
        "teams/freshman.html",
        {
            "team": team,
            "team_page": team_page,
            # "fundraisers": fundraisers,
            "title": "RHS Boys Soccer - Freshman Team",
        },
    )


def sophomore_team(request):
    team = Team.objects.sophomore()
    team_page = TeamPage.objects.first()
    # fundraisers = Campaign.objects.filter(is_active=True)
    return render(
        request,
        "teams/sophomore.html",
        {
            "team": team,
            "team_page": team_page,
            # "fundraisers": fundraisers,
            "title": "RHS Boys Soccer - Sophomore Team",
        },
    )


def team(request, team_id):
    team = get_object_or_404(Team, uuid=team_id)
    team_page = TeamPage.objects.first()
    players = Player.objects.filter(team=team)
    return render(
        request,
        "teams/team.html",
        {
            "team": team,
            "players": players,
            "team_page": team_page,
            "title": team.name,
        },
    )
