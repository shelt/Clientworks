# a page-specific builder.

def r_overview(title1,value1,title2,value2,title3,value3,title4,value4):
    return """
<div class="row">
    <div class="col-xs-12 col-md-6 col-lg-3">
        <div class="panel panel-blue panel-widget ">
            <div class="row no-padding">
                <div class="col-sm-3 col-lg-5 widget-left">
                    <em class="glyphicon glyphicon-shopping-cart glyphicon-l"></em>
                </div>
                <div class="col-sm-9 col-lg-7 widget-right">
                    <div class="large">"""+str(value1)+"""</div>
                    <div class="text-muted">"""+title1+"""</div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-xs-12 col-md-6 col-lg-3">
        <div class="panel panel-orange panel-widget">
            <div class="row no-padding">
                <div class="col-sm-3 col-lg-5 widget-left">
                    <em class="glyphicon glyphicon-comment glyphicon-l"></em>
                </div>
                <div class="col-sm-9 col-lg-7 widget-right">
                    <div class="large">"""+str(value2)+"""</div>
                    <div class="text-muted">"""+title2+"""</div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-xs-12 col-md-6 col-lg-3">
        <div class="panel panel-teal panel-widget">
            <div class="row no-padding">
                <div class="col-sm-3 col-lg-5 widget-left">
                    <em class="glyphicon glyphicon-user glyphicon-l"></em>
                </div>
                <div class="col-sm-9 col-lg-7 widget-right">
                    <div class="large">"""+str(value3)+"""</div>
                    <div class="text-muted">"""+title3+"""</div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-xs-12 col-md-6 col-lg-3">
        <div class="panel panel-red panel-widget">
            <div class="row no-padding">
                <div class="col-sm-3 col-lg-5 widget-left">
                    <em class="glyphicon glyphicon-stats glyphicon-l"></em>
                </div>
                <div class="col-sm-9 col-lg-7 widget-right">
                    <div class="large">"""+str(value4)+"""</div>
                    <div class="text-muted">"""+title4+"""</div>
                </div>
            </div>
        </div>
    </div>
</div><!--/.row-->
"""

def r_chart(title):
    return """
<div class="row">
    <div class="col-lg-12">
        <div class="panel panel-default">
            <div class="panel-heading">"""+title+"""</div>
            <div class="panel-body">
                <div class="canvas-wrapper">
                    <canvas class="main-chart" id="line-chart" height="200" width="600"></canvas>
                </div>
            </div>
        </div>
    </div>
</div><!--/.row-->
"""

def r_growth_overview(title1,value1,title2,value2,title3,value3,title4,value4):
    return """
<div class="row">
    <div class="col-xs-6 col-md-3">
        <div class="panel panel-default">
            <div class="panel-body easypiechart-panel">
                <h4>"""+title1+"""</h4>
                <div class="easypiechart" id="easypiechart-blue" data-percent=\""""+str(value1)+"""" ><span class="percent">"""+str(value1)+"""%</span>
                </div>
            </div>
        </div>
    </div>
    <div class="col-xs-6 col-md-3">
        <div class="panel panel-default">
            <div class="panel-body easypiechart-panel">
                <h4>"""+title2+"""</h4>
                <div class="easypiechart" id="easypiechart-orange" data-percent=\""""+str(value2)+"""" ><span class="percent">"""+str(value2)+"""%</span>
                </div>
            </div>
        </div>
    </div>
    <div class="col-xs-6 col-md-3">
        <div class="panel panel-default">
            <div class="panel-body easypiechart-panel">
                <h4>"""+title3+"""</h4>
                <div class="easypiechart" id="easypiechart-teal" data-percent=\""""+str(value3)+"""" ><span class="percent">"""+str(value3)+"""%</span>
                </div>
            </div>
        </div>
    </div>
    <div class="col-xs-6 col-md-3">
        <div class="panel panel-default">
            <div class="panel-body easypiechart-panel">
                <h4>"""+title4+"""</h4>
                <div class="easypiechart" id="easypiechart-red" data-percent=\""""+str(value4)+"""" ><span class="percent">"""+str(value4)+"""%</span>
                </div>
            </div>
        </div>
    </div>
</div><!--/.row-->
"""