from django.shortcuts import render

from rhs_soccer.core.forms.contact import ContactForm
from rhs_soccer.core.forms.sponsor_application import SponsorshipApplicationForm
from rhs_soccer.core.models import AboutPage
from rhs_soccer.core.models import ContactPage
from rhs_soccer.core.models import PrivacyPolicyPage
from rhs_soccer.core.models import Sponsor
from rhs_soccer.core.models import SponsorPage
from rhs_soccer.core.models import SponsorshipPackage
from rhs_soccer.core.models import TermsOfServicePage
from rhs_soccer.teams.models import Team


def home(request):
    title = "Home of the Irish"
    about_page = AboutPage.objects.first()
    teams = Team.objects.filter(home_team=True)
    sponsors = Sponsor.objects.filter(level="Platinum").order_by("?")[:5].all()
    contact_form = ContactForm()

    context = {
        "title": title,
        "about_page": about_page,
        "teams": teams,
        "sponsors": sponsors,
        "contact_form": contact_form,
    }
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context["success"] = True
            context["contact_form"] = ContactForm()
            return render(request, "core/home.html", context)
        context["contact_form"] = form
    return render(request, "core/home.html", context)


def about(request):
    about_page = AboutPage.objects.first()
    sponsors = Sponsor.objects.all()
    context = {
        "about_page": about_page,
        "sponsors": sponsors,
        "title": about_page.title,
    }
    return render(request, "core/about.html", context)


def contact(request):
    contact_page = ContactPage.objects.first()
    if contact_page is None:
        contact_page = ContactPage()
    context = {
        "contact_page": contact_page,
        "title": contact_page.title,
        "subtitle": contact_page.subtitle,
        "contact_form": ContactForm(),
    }
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context["success"] = True
            context["contact_form"] = ContactForm()
            return render(request, "core/contact.html", context)
        context["contact_form"] = form
    return render(request, "core/contact.html", context)


def sponsors(request):
    sponsors = Sponsor.objects.all()
    sponsor_page = SponsorPage.objects.first()
    context = {
        "sponsors": sponsors,
        "sponsor_page": sponsor_page,
        "title": "Sponsors",
    }
    return render(request, "core/sponsors.html", context)


def sponsorship(request):
    packages = SponsorshipPackage.objects.all()
    application_form = SponsorshipApplicationForm()
    context = {
        "packages": packages,
        "application_form": application_form,
        "title": "Sponsorship",
    }
    if request.method == "POST":
        form = SponsorshipApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            context["success"] = True
            context["application_form"] = SponsorshipApplicationForm()
            return render(request, "core/sponsorships.html", context)
        context["application_form"] = form
    return render(request, "core/sponsorships.html", context)


def terms(request):
    terms_page = TermsOfServicePage.objects.first()
    context = {
        "terms_page": terms_page,
        "title": terms_page.title,
        "subtitle": terms_page.subtitle,
    }
    return render(request, "core/terms.html", context)


def privacy(request):
    privacy_page = PrivacyPolicyPage.objects.first()
    context = {
        "privacy_page": privacy_page,
        "title": privacy_page.title,
        "subtitle": privacy_page.subtitle,
    }
    return render(request, "core/privacy.html", context)


def booster(request):
    # booster_page = BoosterPage.objects.first()
    # context = {
    #     "booster_page": booster_page,
    #     "title": booster_page.title,
    #     "subtitle": booster_page.subtitle,
    #     "officers": BoosterOfficer.objects.filter(page=booster_page),
    # }
    return render(request, "core/booster.html")
