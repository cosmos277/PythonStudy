import sqlite3
from flask import Flask,request,session,g,redirect,url_for,\
    abort,render_template,flash
from contextlib import closing

#configuration
DATABASE='flask.db'
DEBUG=True
SECRET_KEY='development key'
USERNAME='admin'
PASSWORD='default'

app=Flask(__name__)
app.config.from_object(__name__) #대문자로 설정된 값들을 config에 추가

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    db=connect_db()
    sql='''create table if not exists user(
    id string primary key,
    passwd string not null,
    nick string not null
    );
    '''
    db.cursor().execute(sql)
    db.commit()

@app.before_request
def before_request():
    g.db=connect_db() #g:flask의 전역 클래스 인스턴스

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    cur=g.db.execute('select id,passwd,nick from user')
    entries=[dict(id=row[0], passwd=row[1],nick=row[2])for row in cur.fetchall()]
    print(entries)
    return render_template('show_entries.html',entries=entries)

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    #if request.method=='GET':
    #    return render_template('login.html')
    if request.method == 'POST':
        query="select id, passwd from user where (id = '" +request.form['id']+ "') and (passwd = '" +request.form['passwd']+"')";
        cur=g.db.execute(query)
        for row in cur:
           if row[0]=="":
              error = 'Check your ID and password'
              flash('Check your ID and password')
              return redirect(url_for('show_entries'))

           else:
               session['logged_in'] = True
               flash('You were logged in')
               return redirect(url_for('show_entries'))
    #else:
    #    error="Invalid request method:{}".format(request.method)
    return render_template('login.html', error=error)


@app.route('/join',methods=['GET','POST'])
def join():
    error=None
    if request.method=='GET':
        return render_template('join.html')
    elif request.method=='POST':
        g.db.execute('insert into user(id,passwd,nick) values(?,?,?)',
                 [request.form['id'],request.form['passwd'],request.form['nick']])
        g.db.commit()
        flash('New entry was successfully posted')
        return render_template('join.html',error=error)
    else:
        abort(405)
    #if not session.get('logged_in'):
    #    abort(401)
    

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__=='__main__':
    #init_db()
    app.run()