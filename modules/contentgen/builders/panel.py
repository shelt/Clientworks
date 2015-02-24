
def alert():
    return False

def c_basic(colclass, type, header, body):
    return """
<div class=\""""+colclass+"""">

    <div class=\""""+type+"""">
        <div class="panel-heading">
            """+header+"""
        </div>
        <div class="panel-body">
            <p>"""+body+"""</p>
        </div>
    </div>
                    
</div><!--/.col-->
"""

def c_widget(colclass, type):
    return False

def c_tab(colclass, type):
    return False