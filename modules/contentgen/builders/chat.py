



def message(poster, time, body):
    return """
<li class="left clearfix">
    <span class="chat-img pull-left">
        <img src="http://placehold.it/80/30a5ff/fff" alt="User Avatar" class="img-circle" />
    </span>
    <div class="chat-body clearfix">
        <div class="header">
            <strong class="primary-font">"""+poster+"""</strong> <small class="text-muted">"""+time+"""</small>
        </div>
        <p>
            """+body+"""
        </p>
    </div>
</li>
"""

def c_chat(messagelist):
    messages = ""
    for message in messagelist:
        messages += (message + "\n")

    return """
<div class="col-md-8">

    <div class="panel panel-default chat">
        <div class="panel-heading" id="accordion"><span class="glyphicon glyphicon-comment"></span> Chat</div>
        <div class="panel-body">
            <ul>
                """+messages+"""
            </ul>
        </div>
        
        <div class="panel-footer">
            <div class="input-group">
                <input id="btn-input" type="text" class="form-control input-md" placeholder="Type your message here..." />
                <span class="input-group-btn">
                    <button class="btn btn-success btn-md" id="btn-chat">Send</button>
                </span>
            </div>
        </div>
    </div>
    
</div><!--/.col-->
"""