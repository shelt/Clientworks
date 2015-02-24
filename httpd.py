import sys,os
import re
import cgi
from mimetypes import guess_type
from http.server import HTTPServer, BaseHTTPRequestHandler
from http.cookies import SimpleCookie

# Local imports
from modules import auth

# Pagebuilder imports
from modules.contentgen import dashboard

### TODO ###
# apply page
# add email format verification
# better form identification (login vs apply vs chat input)
# add "incorrect login" (at end of post request)

# Content-Types associated with extensions
CTYPE_PATH = {
".html"    :"text/html",
".css"     :"text/css",
".css.map" :"text/css",
".jpg"     :"image/jpg",
".jpeg"    :"image/jpg",
".png"     :"image/png",
".ico"     :"image/ico",
".js"      :"text/javascript",
".json"    :"application/json",
".eot"     :"application/vnd.ms-fontobject",
".otf"     :"application/font-sfnt",
".svg"     :"image/svg+xmlt",
".ttf"     :"application/font-sfnt",
".woff"    :"application/font-woff"
}

# Whether or not file extensions belong to binary files
CTYPE_ISBINARY = {
".html"    :False,
".css"     :False,
".css.map" :False,
".jpg"     :True,
".jpeg"    :True,
".png"     :True,
".ico"     :True,
".js"      :False,
".json"    :False,
".eot"     :False,
".otf"     :False,
".svg"     :False,
".ttf"     :True,
".woff"    :True
}

CTYPE_ISCACHE = {
".html"    :False,
".css"     :True,
".css.map" :True,
".jpg"     :False,
".jpeg"    :False,
".png"     :False,
".ico"     :False,
".js"      :True,
".json"    :True,
".eot"     :True,
".otf"     :True,
".svg"     :True,
".ttf"     :True,
".woff"    :True
}





# Imported page builders
BUILDERS = {
"dashboard":dashboard
}

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE'  : self.headers['Content-Type'],})
        if form.list[0].name == "username" and form.list[1].name == "password":
            uid = auth.verify_user(form.list[0].value, form.list[1].value)
            if uid is not None:
                print("* "+self.client_address[0]+" authenticated as "+str(uid)+".")
                sid = auth.add_session(uid)
                print("* "+str(uid)+" is now sessioned at "+self.client_address[0])
                
                self.respond(302,[("Location","/dashboard/"),
                                  ('Set-Cookie', 'session=%s; path=/' % sid)])
            else:
                print("! "+self.client_address[0]+" entered invalid login info.")

    def do_GET(self):
        if lacks_trailing_slash(self.path):
            self.respond(302,[("Location",self.path + "/")])
            return
        # Get cookies
        cookies = SimpleCookie()
        cookies.load(self.headers)
        
        ### SESSION CHECKING ###
        
        # Check cookies for active sessions
        cookie_val = has_session_cookie(cookies)
        if cookie_val:
            # User says they are sessioned
            sid = cookie_val
            uid = auth.verify_session(sid)
            if uid is not None:
                sessioned = uid # TRUE
            else:
                print("! "+self.client_address[0]+" lied about being sessioned.")
                # Refresh and clear the session cookie.
                self.respond(302,[("Location","/login/"),
                                  ('Set-Cookie', 'session=')])
                return
        else:
            # User is not sessioned
            print("* "+self.client_address[0]+" arrived as a guest.")
            sessioned = False
            
        print(self.client_address[0] +" requests "+self.path)
        ### SESSION DECISION ###
        
        
        # Redirect non-sessioned users away from illegal pages
        # Redirect sessioned users away from non-session pages (and "/")
        if sessioned is False and not (self.path.startswith("/login") or self.path.startswith("/apply")):
            self.respond(302,[("Location","/login/")])
            return
        elif sessioned is not False and (self.path == "/" or self.path.startswith("/login") or self.path.startswith("/apply")):
            self.respond(302,[("Location","/dashboard/")])
            return

        ### SEND DYNAMIC CONTENT ###
        if not is_content(self.path):
            try:
                builder = BUILDERS[self.path.strip("/")]
                
                # Begin response
                self.respond(200,[("Content-type","text/html")])
                data = builder.build(sessioned).encode("UTF-8")
                self.wfile.write(data)
                return
            except KeyError:
                print("! Directory "+self.path+" has no content builder! Attempting static directory.")
                self.path += "/index.html"

        ### SEND FILE CONTENT ###
        # Direct to HTML folder
        self.path = "html" + self.path

        # Get Content-Type
        _,ext = os.path.splitext(self.path)
        # Open the file
        if CTYPE_ISBINARY[ext]:
            f = open(self.path, 'rb')#, errors='ignore')
        else:
            f = open(self.path)
        
        # Respond
        try:
            self.respond(200, [("Content-type",CTYPE_PATH[ext])], CTYPE_ISCACHE[ext])
        except KeyError:
            print("! Unhandled extension: "+ext)
            f.close()
            return

        # Send the file (encode if necessary)
        data = f.read()
        if type(data) == str:
            data = data.encode("UTF-8")
        self.wfile.write(data)
        f.close()
        return
        
    def respond(self,code,headers=[],cache=False): # list of tuples
        self.send_response(code)
        for header in headers:
            self.send_header(header[0], header[1])
        if cache:
            self.send_header("Cache-Control","public; max-age=31536000")
        self.end_headers()
    
    # Silence terribly annoying stdout.
    def log_message(self, format, *args):
        return

def has_session_cookie(cookies):
    try:    
        c = cookies["Cookie"].value.split('=', 1)
        if c[0] == "session":
            return c[1]
    except KeyError:
        return False

FILE_PATTERN = re.compile(".*\..{1,4}$")
def is_content(path):
    if FILE_PATTERN.match(path):
        return True

def lacks_trailing_slash(path):
    return (("." not in path) and (not path.endswith("/")))

def run(server_class, server_handler):
    server_address = ("", 8000)
    httpd = server_class(server_address, server_handler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.socket.close()

run(HTTPServer, RequestHandler)