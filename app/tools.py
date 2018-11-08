class PageTree:

    def __init__(self, page):
        self.html_menu = "<p>M = in menus ; L = live(published)</p>"
        self.traverse(page)

    def traverse(self,item):
        info = ""
        if(item.show_in_menus):
            info += "M"
        if(item.live):
            info += "L"
        self.html_menu += "<li><a href="+item.url+">"+item.title+" (" + info + ") "+"</a></li>\n"

        if (item.numchild != 0):
            self.html_menu += "<ul>\n"
            for i in item.get_children():
                self.traverse(i)
            self.html_menu += "</ul>\n"



def get_tree(obj,is_live=True,is_in_menu=None):

    global html_menu

    #reset string
    html_menu = ''

    if(is_in_menu == None):
        page = obj.objects.filter(live=is_live)[0]
    else:
        page = obj.objects.filter(live=is_live, show_in_menus=is_in_menu)[0]
    traverse(page)

    return html_menu

