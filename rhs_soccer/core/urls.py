from django.urls import path

from rhs_soccer.core.views import about
from rhs_soccer.core.views import booster
from rhs_soccer.core.views import contact
from rhs_soccer.core.views import home
from rhs_soccer.core.views import privacy
from rhs_soccer.core.views import sponsors
from rhs_soccer.core.views import sponsorship
from rhs_soccer.core.views import terms

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("terms/", terms, name="terms"),
    path("privacy/", privacy, name="privacy"),
    path("booster/", booster, name="booster"),
    path("sponsors/", sponsors, name="sponsor_page"),
    path("sponsorship/", sponsorship, name="sponsorship"),
    # path("team-page/", team_page, name="team_page"),
    # path("news-page/", news_page, name="news_page"),
    # path("press-releases-page/", press_releases_page, name="press_releases_page"),
    # path("sponsors-page/", sponsors_page, name="sponsors_page"),
]
