import requests
import socket
from flask import Flask, render_template, redirect,request
app = Flask(__name__)

line_token = 'UawjDRkARXD9k49XaSlEIe3iOwpieifdApbjo3wtrI1'

@app.route('/')
def root_html():
    return redirect('index')

@app.route('/index')
def index_html(name=None):
    return render_template('index.html')


@app.route('/tell/',methods=['POST','GET'])
@app.route('/tell',methods=['POST','GET'])
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


#curl -X POST -H 'Authorization: Bearer UawjDRkARXD9k49XaSlEIe3iOwpieifdApbjo3wtrI1' -F 'message=foobar' https://notify-api.line.me/api/notify