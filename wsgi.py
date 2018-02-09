import requests
import socket
import os
import signal
from flask import Flask, render_template, redirect,request
application = Flask(__name__)

line_token = 'UawjDRkARXD9k49XaSlEIe3iOwpieifdApbjo3wtrI1'

@application.route('/')
def root_html():
    return redirect('index')

@application.route('/index')
def index_html(name=None):
    try:
        hostname = os.environ['HOSTNAME']
    except KeyError:
        hostname = 'Unknown'
    return render_template('index.html',hostname=hostname)


@application.route('/tell/',methods=['POST','GET'])
@application.route('/tell',methods=['POST','GET'])
def tell_html():
    if request.method == 'GET':
        return render_template('tell.html',result='begin')

    if request.method == 'POST':
        message = request.form['message']
        if message == None or message.strip()=='':
            return render_template('tell.html',result='Empty message not delivered!\n')

        headers = {'Authorization': 'Bearer ' + line_token}
        params = {'message': message}
        r = requests.post('https://notify-api.line.me/api/notify', params=params, headers=headers)
        if r.status_code != 200:
            return render_template('tell.html',result='Fail to deliver message :\n' + message + '\n')
        return render_template('tell.html',result='Message :\n' + message + '\nDelivered\n')

@application.route('/crash/',methods=['POST','GET'])
@application.route('/crash',methods=['POST','GET'])
def crash_down():
    pid = os.getpid()
    ppid = os.getppid()
    if request.method == 'GET':
        return render_template('crash.html',pid=pid,ppid=ppid)
    if request.method == 'POST':
        target = request.form['terminateTarget']
        if target =='pid':
            os.kill(pid,signal.SIGTERM)
        if target =='ppid':
            os.kill(ppid,signal.SIGTERM)
    return render_template('crash.html',pid=pid,ppid=ppid)

if __name__ == '__main__':
    application.run()

#curl -X POST -H 'Authorization: Bearer UawjDRkARXD9k49XaSlEIe3iOwpieifdApbjo3wtrI1' -F 'message=foobar' https://notify-api.line.me/api/notify