# Tutorial from flask.pocoo.org
from flask import Flask, render_template, request


@app.route('/announcment_archive')
def show_announcements():
    db = get_db()
    cur = db.execute('select title, text, publication_date from announcements order by id desc')
    entries = cur.fetchall()
    return render_template("announcement_archive.html", entries = entries)

#add new announcement
@app.route('/add', methods=['POST'])
def add_anouncment():
    if not session.get('logged_in'):
        abort(401)
    db = get_db
    db.execute('insert into announcements(title, text, publication_date) values (?, ?, ?)',
                [request.form['title'], request.form['text'], request.form['publication_date']])
    db.commit()
    return redirect(url_for('show_announcements'))

#Change with actual users, stored in db and encrypted passwords.
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.methpd = 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            return redirect(url_for('show_announcements'))
    return render_template('login.html', error=error)

@app.route('/ticket')
def submit_ticket():
    return render_template("ticket.html")
