from flask import Flask
from flask import Flask, url_for,redirect
app=Flask(__name__)

@app.route('/')
def hello_world():
    
   return redirect(url_for('login'))


@app.route('/login')
def login():

    return 'log in'

@app.route('/profile/<username>')
def get_profile(username):
    return 'profile : '+username

@app.route('/message/<int:message_id>')
def get_message(message_id):
    return 'message_id : %d' %message_id

if __name__=='__main__':
    #app.run()
    app.debug=True
    app.run(host="172.16.32.110", port=5000)



