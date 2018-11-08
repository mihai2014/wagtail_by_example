from django.db import models

# Create your models here.

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from app.tools import PageTree

class AppIndexPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    def get_context(self, request):
        context = super().get_context(request)

        home = Page.objects.filter(title='Home')[0]
        #home = HomePage.objects.all()[0]

        home_tree = PageTree(home).html_menu
        context['menu'] = home_tree

        return context


class AppPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]
    
