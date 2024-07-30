from wagtail.models import Page
from solo.models import SingletonModel

class SingletonPage(Page, SingletonModel):
    class Meta:
        abstract = True