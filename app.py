from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('home.html', title='Spy website for Spies (Disclaimer, shut down by US)')

@app.route('/spygears')
def spygears():    
    spygears = ["Tracker", 'Turtle Mines', 'Tanks', "Hijack computer", "All bank accounts in the world Hijacked machine"]
    return render_template('spygears.html', title='Spygear',
    subtitle='Tools to spy your way in.',
    spygears=spygears)

@app.route('/spymissions')
def spymissions():    
    spymissions = ["Assasination", 'Hijack', 'Under cover data stealing']
    return render_template('spymissions.html', title='Spymission',
    subtitle='Earn your hard earned cash and bring your ideal justice to the world.',
    spymissions=spymissions)


@app.route('/spyshops')
def spyshops():    
    spyshops = ['spyshop.com']
    return render_template('spyshops.html', title='Spyshop',
    subtitle='Spend your hard earned cash.',
    spyshops=spyshops)

if __name__ == '__main__':
    app.run(debug=True)