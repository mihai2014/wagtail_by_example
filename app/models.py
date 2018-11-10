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

        bs = request.GET.get('bs')
        event = request.GET.get('event')
        template_menu = request.GET.get('template_menu')

        context['bs'] = bs
        context['event'] = event
        context['template_menu'] = template_menu
        
        description = "Multi-line drop-down menu"

        if(event == 'click'):
            description += " (click) "
            if(template_menu == 'native'):
                context['menu'] = "menus/bootstrap3/main_menu_dropdown.html" 
            if(template_menu == 'custom'):
                context['menu'] = "app/menu_bs4/menu.html"

        if(bs == '3'):
            description += "using bootstrap 3"
            context['layout'] = 'app/layout_bs3.html'
        if(bs == '4'):
            description += "using bootstrap 4"
            context['layout'] = 'app/layout_bs4.html'

        context['description'] = description


        home = Page.objects.filter(title='Home')[0]
        #home = HomePage.objects.all()[0]

        home_tree = PageTree(home).html_menu
        context['tree'] = home_tree

        return context


class AppPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]
   
