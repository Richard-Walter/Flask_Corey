from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018",
    },
]


@app.route("/")
@app.route("/home")
def home():
    # return '<h1>Home Page<h1>'  # easier to use a template
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


if __name__ == "__main__":

    app.run(
        debug=True
    )  # this means you dont have to restart the server after each change

