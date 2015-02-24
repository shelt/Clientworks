


H_STARTDOC()    # includes title, stylesheet etc.


navbar()

sidebar()

M_START() # main start

r_title("Dashboard")
r_overview("Active Investments",120,"Active Bonds",82,"New Members",24,"Reserve Assets","5.2T")

r_chart("Profit Overview") #chart is built elsewear?

r_growth_overview("Active Investments Growth",45,"Active Bonds Growth",65,"New Members Growth",48,"Reserve Assets Growth",27)

R_START() # row start

chatdata = [
chatmessage("Doc Pope", "32 min ago", "Hello, world!"),   # shouldRet a <li class="left clearfix">
chatmessage("Doc Pope", "28 min ago", "Hello, world!"),
chatmessage("Doc Pope", "24 min ago", "Hello, world!")
]
c_chat(chatdata) #  shouldRet a <div class="col-md-8">  with all things surounding the li's

c_panel("panel-danger", "heading", "body")

R_END()

M_END()

H_ENDDOC()   #includes scripts and such