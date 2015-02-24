from collections import OrderedDict

# This file contains the builder functions
# used on most pages.
# This first class is slightly more meta:
# it's the object that constructs the HTML
# in the builders.

class HTML():
    body = ""
    def add(self,text):
        self.body += ("\n" + text)




NAVITEMS = OrderedDict(  #for sidebar()
[
    ("dashboard", """<a href="index.html"><span class="glyphicon glyphicon-dashboard"></span> Dashboard</a>"""),
    ("widgets", """<a href="widgets.html"><span class="glyphicon glyphicon-th"></span> Investments</a>"""),
    ("charts", """<a href="charts.html"><span class="glyphicon glyphicon-stats"></span> Data Overview</a>"""),
    ("tables", """<a href="tables.html"><span class="glyphicon glyphicon-list-alt"></span> Noticeboard</a>"""),
    ("forms", """<a href="forms.html"><span class="glyphicon glyphicon-pencil"></span> Forums</a>"""),
    ("panels", """<a href="panels.html"><span class="glyphicon glyphicon-info-sign"></span> Admin</a>""")
]
)


def STARTDOC(title):
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>"""+title+"""</title>
<link rel="icon" type="image/png" href="favicon.png"/>

<link href="css/bootstrap.min.css" rel="stylesheet">
<link href="css/datepicker3.css" rel="stylesheet">
<link href="css/bootstrap-table.css" rel="stylesheet">
<link href="css/styles.css" rel="stylesheet">

<!--[if lt IE 9]>
<script src="js/html5shiv.js"></script>
<script src="js/respond.min.js"></script>
<![endif]-->

</head>

<body>
"""

def navbar(username):
    return """
	<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<a class="navbar-brand" href="#"><span>Clientele</span>Access</a>
				<ul class="user-menu">
					<li class="dropdown pull-right">
						<a href="#" class="dropdown-toggle" data-toggle="dropdown"><span class="glyphicon glyphicon-user"></span> """+username+""" <span class="caret"></span></a>
						<ul class="dropdown-menu" role="menu">
							<li><a href="#"><span class="glyphicon glyphicon-user"></span> Profile</a></li>
							<li><a href="#"><span class="glyphicon glyphicon-cog"></span> Settings</a></li>
							<li><a href="#"><span class="glyphicon glyphicon-log-out"></span> Logout</a></li>
						</ul>
					</li>
				</ul>
			</div>
							
		</div><!-- /.container-fluid -->
	</nav>
"""

def pathbar(pathitems):
    path = ""
    for item in pathitems:
        path += ("""<li class="active">"""+item+"""</li>""" + "\n")
    return """		
<div class="row">
    <ol class="breadcrumb">
        <li><a href="#"><span class="glyphicon glyphicon-home"></span></a></li>
        """+path+"""
    </ol>
</div><!--/.row-->
"""

def title(text):
    return """
<div class="row">
    <div class="col-lg-12">
        <h1 class="page-header">"""+text+"""</h1>
    </div>
</div><!--/.row-->
"""

def sidebar(currentpage):
    list = ""
    for title,a_element in NAVITEMS.items():
        if title == currentpage:
            list += """<li class="active">""" + a_element + "</li>\n"
        else:
            list += "<li>" + a_element + "</li>\n"
            
            

            
            
            
    return """
	<div id="sidebar-collapse" class="col-sm-3 col-lg-2 sidebar">
		<form role="search">
			<div class="form-group">
				<input type="text" class="form-control" placeholder="Search">
			</div>
		</form>
		<ul class="nav menu">
			"""+list+"""
            <!-- UNUSED (dropdown comments)
			<li class="parent ">
				<a href="#">
					<span class="glyphicon glyphicon-list"></span> Dropdown <span data-toggle="collapse" href="#sub-item-1" class="icon pull-right"><em class="glyphicon glyphicon-s glyphicon-plus"></em></span> 
				</a>
				<ul class="children collapse" id="sub-item-1">
					<li>
						<a class="" href="#">
							<span class="glyphicon glyphicon-share-alt"></span> Sub Item 1
						</a>
					</li>
					<li>
						<a class="" href="#">
							<span class="glyphicon glyphicon-share-alt"></span> Sub Item 2
						</a>
					</li>
					<li>
						<a class="" href="#">
							<span class="glyphicon glyphicon-share-alt"></span> Sub Item 3
						</a>
					</li>
				</ul>
			</li>
            -->
			<li role="presentation" class="divider"></li>
			<li><a href="login.html"><span class="glyphicon glyphicon-user"></span> Login Page</a></li>
		</ul>
		<div class="attribution">© <a href="/staff">Clientalk</a> 2015</div>
	</div><!--/.sidebar-->
"""

def ENDDOC():
    return """
	<script src="js/jquery-1.11.1.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/chart.min.js"></script>
	<script src="js/chart-data.js"></script>
	<script src="js/easypiechart.js"></script>
	<script src="js/easypiechart-data.js"></script>
	<script src="js/bootstrap-datepicker.js"></script>
    <script src="js/bootstrap-table.js"></script>
	<script>
		$('#calendar').datepicker({
		});

		!function ($) {
		    $(document).on("click","ul.nav li.parent > a > span.icon", function(){          
		        $(this).find('em:first').toggleClass("glyphicon-minus");      
		    }); 
		    $(".sidebar span.icon").find('em:first').addClass("glyphicon-plus");
		}(window.jQuery);

		$(window).on('resize', function () {
		  if ($(window).width() > 768) $('#sidebar-collapse').collapse('show')
		})
		$(window).on('resize', function () {
		  if ($(window).width() <= 767) $('#sidebar-collapse').collapse('hide')
		})
	</script>	
</body>

</html>
"""

##########################
# Starters and finishers #
##########################


def S_main():
    return """
<div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">
"""

def F_main():
    return """
</div><!--/.main-->
"""

def S_row():
    return """
<div class="row">
"""

def F_row():
    return """
</div><!--/.row-->
"""




def tresspass():
    return """<h1>Permission Denied</h1>
<i>You don't have a valid session and therefore the content generator will ignore you.</i>"""











