from flask import Flask, render_template

#refers the app to itself
app = Flask(__name__)

posts = [
    {
        'author':'Cate chep',
        'title':'Beautiful name',
        'content':'What a beautiful name it is, nothing compares to it',
        'date_posted':'November 17, 2018'
    },
    {
        'author':'John Doe',
        'title':'Beautiful name',
        'content':'What a beautiful name it is, nothing compares to it',
        'date_posted':'November 17, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about_page():
    return render_template('about.html', title='About')

#run the script directly in debug mode
if __name__=='__main__':
    app.run(debug=True)