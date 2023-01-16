from distutils.log import warn
from pickle import TRUE
from fabric import Connection
from flask import Flask, render_template
#from flask_api import FlaskAPI
from flask_cors import CORS
#from flask import make_response
import re

#app=Flask(__name__,template_folder='templates')
app=Flask(__name__)
pattern=re.compile(r'Senseh\s*version.*R')
pattern_2=re.compile(r'command\s*not\s*found')

CORS(app)
#username="root"
#host_="172.16.7.40"
#pass_w="root"

#login=["root","172.16.7.40","root"] #username, IP address, password of the target computer

@app.route('/')
def senseh_version():
    #with Connection(host="root@172.18.0.221",connect_kwargs={"password":"MTLCMM-108631"}) as c:
    #with Connection(host="root@172.16.7.40",connect_kwargs={"password":"root"}) as c:
    with Connection(host="minesense@172.16.7.43",connect_kwargs={"password":"minesense"}) as c:
    #with Connection(host="{0}@{1}".format(login[0],login[1]), connect_kwargs={"password":"{0}".format(login[-1])}) as c:
        initial_str=str(c.run("version"))
        match_1=re.search(pattern, initial_str)
        match_2=re.search(pattern_2, initial_str)
        if match_1:
            return match_1.group()
        #elif match_2:
        #    return "SensEh not installed"
        #elif is_server_error():
        #    return "SensEh is not installed"
        #return make_response("SensEh not installed", 500)
        #match_2=re.search(pattern_2,initial_str)
        #if match_2:
        #    return match_2.group()
        #return "SensEh is not installed"

@app.errorhandler(404)
def page_not_found(error):
    return render_template('templates/400.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('templates/500.html'), 500
