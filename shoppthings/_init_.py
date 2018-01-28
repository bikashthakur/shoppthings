from flask import Flask, render_template, flash, url_for, redirect, request, session
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
from functools import wraps
from jinja2 import Template



from dbconnect import connection
from content_management import Content, homeContent




app = Flask(__name__)
app.secret_key = 'super_secret_key'


class RegistrationForm(Form):
	name = TextField('Name',[validators.Length(min=1, max=50)])
	#username = TextField('username',[validators.Length(min=4, max=20)])
	email = TextField('Email Address',[validators.Length(min=6, max=50)])
	password = PasswordField('Password',[validators.Required(),validators.EqualTo('confirm', message="Passwords must match.")])
	confirm = PasswordField('Repeat password')
	accept_tos = BooleanField('I accept the Terms of Service.',[validators.Required()])

'''------------------------------------------------------------------METHODS ARE DEFINED HERE----------------------------------------------------------------------'''

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash("You need to login first")
			return redirect(url_for('login_page'))
	return wrap

def addWish(items):
	for item in items:
		for itm in items[item]:
			if str(request.form['btn-wish']) == str(itm):
				try:
					cur, conn = connection()
					SQLSelectCommand=(" select * from wishlist where uid = %s and itemid = %s")
					values = [session.get('user'),str(itm)]
					cur.execute(SQLSelectCommand,values)
					data = cur.fetchall()
					flash("The Selected Item is Added to Your Wishlist.")

					if len(data) > 0:
						flash("The item is already in your wishlist.")

					else:
						cur, conn = connection()
						SQLInsertCommand = ("insert into wishlist "
	 										"(itemid, uid) "
											"values (%s,%s)")
						values = [str(itm),session.get('user')]
						cur.execute(SQLInsertCommand,values)
						conn.commit()

				except:
					flash("An unknown problem occured, please try again!")

				finally:
					cur.close()
					conn.close()

			else:
				continue
	return

def delete_Wish():
	user_id = session.get('user')
	item_id = request.form['btn-del-wish']
	try:
		cur, conn = connection()
		SQLDeleteCommand=("delete from wishlist where uid = %s and itemid = %s")
		values = [user_id,item_id]
		cur.execute(SQLDeleteCommand,values)
		conn.commit()
		flash("The Selected Item is beinyg Removed from Your Wishlist.")
	except:
		flash("An unknown problem occured, please try again!")

	finally:
		cur.close()
		conn.close()
	return

def getWish():

	_user = session.get('user')
	wishes = []
	wishlist={}

	cur,conn = connection()
	cur.execute('select * from wishlist where uid = %s',(_user, ))
	wish = cur.fetchall()
	
	for w in wish:
		wishes.append(w[1])

	items = Content()
	for item in items:
		for itm in items[item]:
			for w in wishes:
				if w == itm:
					wishlist[w]=items[item][w]
	home_items = homeContent()
	for item in home_items:
		for itm in home_items[item]:
			for w in wishes:
				if w == itm:
					wishlist[w] = home_items[item][w]
	

	return wishlist

'''------------------------------------------------------------------------END METHODS---------------------------------------------------------------------------------------'''

@app.route('/', methods=["GET","POST"])
def index():
	items = homeContent()
	if request.method == "POST":
		if 'logged_in' in session:
			addWish(items)
		else:
			flash("You need to login first")
	return render_template('index.html', items=items)

@app.route('/store/', methods=["GET","POST"])
def store():
	items = homeContent()
	if request.method == "POST":
		if 'logged_in' in session:
			addWish(items)
		else:
			flash("You need to login first")
	return render_template('home.html', items=items)


@app.route('/register/', methods=["GET","POST"])
def register_page():
	try:
		form = RegistrationForm(request.form)
		if request.method == "POST" and form.validate():
			name = form.name.data
			email = form.email.data
			password = sha256_crypt.encrypt((str(form.password.data)))
			cur, conn = connection()

			x = cur.execute("select * from users where email = (%s)",(thwart(email)))

			if int(x) > 0:
				flash("This email is already registered, please choose another", "warning")
				return render_template("register.html", form=form)
			else:
				cur.execute("insert into users (name, email, password) values (%s, %s, %s)",
							(thwart(name), thwart(email), thwart(password)))
				conn.commit()
				flash("Thank you for registering!")
				cur.close()
				conn.close()

				session['logged_in'] = True
				session['user'] = email

				return redirect(url_for('index'))

		return render_template("register.html", form=form)

	except Exception as e:
		return(str(e))

@app.route('/login/', methods=["GET","POST"])
def login_page():
	error = ''
	try:
		#form = LoginForm(request.form)
		cur, conn = connection()
		if request.method == "POST":
			#email = form.email.data
			email = request.form['email']
			cur.execute("select * from users where email = (%s)", (thwart(email)))
			data = cur.fetchone()[3]
			
			if sha256_crypt.verify(request.form['password'], data):
				session['logged_in'] = True
				cur.execute("select * from users where email = (%s)", (thwart(email)))
				uid = cur.fetchone()[0]
				session['user'] = uid
				flash("You've been' logged in")
				return redirect(url_for("index"))
			else:
				error = "Invalid credentials, try again."

		return render_template("login.html", error=error)

	except Exception as e:
		error = "Invalid credentials, try again."
		return render_template("login.html", error=error)

@app.route('/mobile-phones/',  methods=["GET","POST"])
def mobile_phones():
	items=Content()
	if request.method == "POST":
		if 'logged_in' in session:
			addWish(items)
		else:
			flash("You need to login first")
	return render_template('mobilephones.html', items=items)

@app.route('/mens-clothing/',  methods=["GET","POST"])
def mens_clothing():
	items=Content()
	if request.method == "POST":
		if 'logged_in' in session:
			addWish(items)
		else:
			flash("You need to login first")
	return render_template('mensclothing.html', items=items)

@app.route('/get-wishlist/', methods=["GET","POST"])
def getWishlist():
	wishlist = {}
	items = homeContent()
	if 'logged_in' in session:
		if request.method == "POST":
				if request.form['btn-del-wish']:
					delete_Wish()
	else:
		flash("You need to log in to view the list.")
	wishlist = getWish()
	return render_template('wishlist.html', wishlist=wishlist)

@app.route('/logout/')
@login_required
def logout():
	session.clear()
	flash("You've been logged out.")
	return redirect('/login/')



if __name__ == "__main__":
	app.run()