from flask import Flask, request, render_template
app = Flask(__name__, template_folder='templates', static_folder='static')

username = "ujju"
description = "I love developing web applications."
description += "And this text was created with Jinja"

projects = [
    {
        'id': 1,
        'title': 'E-commerce Website',
        'description': 'A website where you can buy stuff',
        'author': 'ujju',
        'category': 'Web Development'
    },
    {
        'id': 2,
        'title': 'Flask Website',
        'description': 'A website made with Flask',
        'author': 'ujju',
        'category': 'Web Development'
    },
    {
        'id': 3,
        'title': 'Cool Mobile App',
        'description': 'An app that does cool stuff',
        'author': 'ujju',
        'category': 'Mobile Development'
    }
]

@app.route('/')
def hello_world():
    return render_template('index.html', username = username, description = description, projects = projects)

if __name__ == '__main__':
    app.run()

@app.route('/about')
def about():
    return 'About Page'

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    if request.method == 'POST':
        return 'You are using POST'
    elif request.method == 'GET':
        return 'You are using GET'

