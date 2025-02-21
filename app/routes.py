from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Yashwanth'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie was cool!'
		}
	]
	return render_template('index.html', title="Home", user=user, posts=posts)


# '''
# <html>
# 	<head>
# 		<title>Home Page - Microblog</title>
# 	</head>
# 	<body>
# 		<h1>Hello, ''' + user['usrname'] + '''!</h1>
# 	</body>
# </html>'''


# create an about page that has movies inside it and user can view (about.html) those movie names
@app.route('/about')
def about():
	users = {'username': ['Yashwanth', 'Sawanth', 'Venkata Sai', 'Sainath', 'Piyush', 'Hitesh']}
	movies = [ 
		{
			'movie': 'Bahubhali'
			'user': users[username][0]
		},
		{
			'movie': 'Pushpa The Rise',
			'user': users[username][1]
		},
		{
			'movie': 'Pushpa The Rule'
			'user': users[username][2]
		},
		{
			'movie': 'Pushpa The Rampage',
			'user': users[username][3]
		},
		{
			'movie': 'Game Changer',
			'user': users[username][4]
		},
	]
	return render_template('about.html', title="about page",users=users, movies=movies)