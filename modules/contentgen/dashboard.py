from modules.connect import c
from modules.contentgen.builders import GLOBAL
from modules.contentgen.builders import chat
from modules.contentgen.builders import panel
from modules.contentgen.builders import p_dashboard as LOCAL

# A file that gathers data from databases
# and passed variables to build the page.

def build(uid):
    if uid == False and uid is not 0:
        return GLOBAL.tresspass()
    
    html = GLOBAL.HTML()

    # DO DATABASESTUFF HERE WITH UID
    c.execute("SELECT username FROM Users WHERE uid = :uid",{"uid":uid})
    username = c.fetchone()[0]

    html.add(GLOBAL.STARTDOC("JIR Dashboard"))
    
    html.add(GLOBAL.navbar(username))

    html.add(GLOBAL.sidebar("dashboard"))

    html.add(GLOBAL.S_main()) # main start

    html.add(GLOBAL.pathbar(["Dashboard"]))
    html.add(GLOBAL.title("Dashboard"))
    
    html.add(LOCAL.r_overview("Active Investments",120,"Active Bonds",82,"New Members",24,"Reserve Assets","5.2T"))

    html.add(LOCAL.r_chart("Profit Review (2014)")) #chart is built elsewear?

    html.add(LOCAL.r_growth_overview("Active Investments Growth",45,"Active Bonds Growth",65,"New Members Growth",48,"Reserve Assets Growth",27))

    html.add(GLOBAL.S_row()) # row start

    chatdata = [
    chat.message("Doc Pope", "32 min ago", "Hello, world!"),   # shouldRet a <li class="left clearfix">
    chat.message("Doc Pope", "28 min ago", "Hello, world!"),
    chat.message("Doc Pope", "24 min ago", "Hello, world!")
    ]
    html.add(chat.c_chat(chatdata)) #  shouldRet a <div class="col-md-8">  with all things surounding the li's

    html.add(panel.c_basic("col-md-4","panel-danger", "heading", "body"))

    html.add(GLOBAL.F_row())

    html.add(GLOBAL.F_main())

    html.add(GLOBAL.ENDDOC())   #includes scripts and such

    return html.body
