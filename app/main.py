import os
import json
import requests
from random import randint, choice
from ConfigParser import SafeConfigParser
from flask import Flask, render_template, send_from_directory, request

# initialization
app = Flask(__name__)
app.config.update(DEBUG = True)

def randnum(num, types):
    if num == 0:
        num = randint(0,9)
    try:
        if types is None:
            print 'nothing passed'
            return
        elif types == 'num':
            return ''.join(["%s" % randint(0,9) for i in range(0, num)])
        elif types == 'alphanum':
            return ''.join(choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(num))
        elif types == 'alpha':
            return ''.join(choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(num))
    except TypeError, e:
        return e

def readflie(file):
    try:
        file = 'options.ini'
        fo = open(file, 'r')
        return fo.read()
    except:
        return "unable to read config"

def detect_types(filehandle):
    pass

# controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    #return render_template('404.html'), 404
    output = randnum(randint(0,9), 'num')
    return render_template("blank.html", output=output)

@app.route("/")
def index():
    output = randnum(randint(0,9), 'num')
    #return render_template("blank.html", output=output)
    return render_template('index.html', output=output)

@app.route("/random/<num>/type/<types>", methods=['GET'])
def random(num, types):
    num = int(num)
    output = randnum(num, types)
    print output
    return render_template("blank.html", output=output)

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9003))
    app.run(host='0.0.0.0', port=port)
