from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


posts = [ 
    {
        'author': 'stany',
        'title': 'blog 1',
        'content': 'first blog post',
        'date_posted': 'nov 19 2024' ,  
    },

    {
        'author': 'sumanth',
        'title': 'blog 2',
        'content': 'second blog post',
        'date_posted': 'nov 19 2024',   
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

if __name__=="__main__":
    app.run(debug=True)