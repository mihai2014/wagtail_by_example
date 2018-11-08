from home.models import HomePage
from wagtail.core.models import Page

from app.models import AppIndexPage, AppPage

html_menu = ""

def traverse(item):

    global html_menu

    #item.show_in_menus
    #item.live

    html_menu += "<li><a href="+item.url+">"+item.title+"</a></li>\n"

    if (item.numchild != 0):
        html_menu += "<ul>\n"
        for item in item.get_children():
            print(item)
            traverse(item)
        html_menu += "</ul>\n"



home = Page.objects.filter(title='Home')[0]
#home = HomePage.objects.all()[0]

p = home.get_children()[0]
print(p)
p1 = p.get_children()[0]

print(p1)

