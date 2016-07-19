from flask import Flask
app = Flask(__name__)



def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.slite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('init_db')
def init_db_command():
    init_db()
    print("Initialized the database")
