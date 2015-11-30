from flask import Flask,url_for,render_template

app=Flask(__name__)


@app.route('/')
def hello():
    data={
        'title':'Hello',
        'name':'greenjoa'
        }
    return render_template('main.html',**data)

@app.route('/hello2/')
def hello2():
    data=[dict(href="http://www.naver.com", caption="네이버"), dict(href="http://www.google.com",caption="구글")]
    return render_template('hello.html',items=data)

if __name__=='__main__':
    app.debug=True
    app.run()