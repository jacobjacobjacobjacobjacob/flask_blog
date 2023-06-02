from flask import Flask, render_template

app = Flask(__name__)

# creating a list of dictionaries to represent the blog posts
posts = [
    {
        'author': 'jacob',
        'title': 'blog post 1',
        'content': 'hello, this is an example',
        'date_posted': '02.06.23'
    },
    {
        'author': 'aron',
        'title': 'blog post 2',
        'content': 'aron is my cat',
        'date_posted': '03.06.23'
    }
]


# Home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


# About page
@app.route("/about")
def about():
    return render_template('about.html', title="About")


if __name__ == '__main__':
    app.run(debug=True)
