from datetime import datetime
from flask import render_template
from Python_Flask_Project_1 import app

posts = [
    {
        'author': 'Pan Jello',
        'title': 'Blog Post 1',
        'content': 'First Post',
        'date': '1/1/24'  
    }, 
    {
        'author': 'Matt Han',
        'title': 'Blog Post 2',
        'content': 'Second Post',
        'date': '1/2/24'  
    }
  ]

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/test')
def test():
    return render_template('test.html',
                           title='Jello',
                           year=datetime.now().year,
                           posts=posts)


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )




