#########################################
###### Student Name: Rutvik Samant ######
########## Student ID: 21014847 #########
#########################################
import dbfunc
import mysql.connector
import MySQLdb
import gc
from calendar import c
from datetime import datetime, timedelta, date
from flask import Flask,render_template,request,redirect,session,flash,url_for, jsonify
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
from functools import wraps

app=Flask(__name__)
app.secret_key = 'rutvik'

app.config['MYSQL_HOST']='127.0.0.1'    
app.config['MYSQL_USER']='rutvik2samant'
app.config['MYSQL_PASSWORD']='Innsworth@164'
app.config['MYSQL_DB']='rutvik2samant'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql=MySQL(app)

##########################################
############ Authentication ##############
##########################################
def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if ('logged_in' in session):
            return f(*args, **kwargs)
        else:
            flash("You need to login first as admin user",'danger')            
            print("You need to login first as admin user")
            #return redirect(url_for('login', error='You need to login first as admin user'))
            return render_template('adminlogin.html', error='You need to login first as admin user')    
    return wrap
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:      
            flash("You need to login first",'danger')      
            print("You need to login first")
            #return redirect(url_for('login', error='You need to login first'))
            return render_template('login.html', error='You need to login first')    
    return wrap
################################################
############ Login & Registration ##############
################################################    
@app.route("/")
def home():
    return render_template("home.html")

#Login
@app.route('/login',methods=['POST','GET'])
def login():
    status=True
    if request.method=='POST':
        email=request.form["email"]
        pwd=request.form["upass"]
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s AND password=%s",(email,pwd))
        data=cur.fetchone()  
        if data:
            session['logged_in']=True
            session['uid'] = data["id"]
            session['username'] = data["name"]
            session['mail'] = data["email"]
            session['pass'] = data["password"]
            flash('Login Successfully','success')
            return redirect('userhome')
        else:
            flash('Invalid Login. Try Again','danger')
    return render_template("login.html")

#Registration  
@app.route('/reg',methods=['POST','GET']) 
def reg():
    status=False
    if request.method=='POST':
        name=request.form["uname"]
        email=request.form["email"]
        pwd=request.form["upass"]
        usertype= "standard"
        cur=mysql.connection.cursor()
        cur.execute("INSERT into users (name, password, email, usertype) values(%s,%s,%s,%s)",(name,pwd,email,usertype))
        mysql.connection.commit()
        cur.close()
        flash('Registration has been done Successfully. Login Here...','success')
        return redirect('login')
    return render_template("reg.html",status=status)

#Admin Login
@app.route("/admin",methods=['POST','GET'])
def admin():
    status=True
    if request.method=='POST':
        email=request.form["email"]
        pwd=request.form["password"]
        cur=mysql.connection.cursor()
        cur.execute("SELECT * from users WHERE email=%s and password=%s",(email,pwd))
        data=cur.fetchone()
        if data:
            session['logged_in']=True
            session['username']=data["name"]
            session['mail']=data["email"]
            flash('Logged in Successfully as Admin','success')
            return redirect('adminhome')
        else:
            flash('Invalid Login. Try Again','danger')
    return render_template("adminlogin.html")

##########################################
############ Admin Controls ##############
##########################################
@app.route('/generateadminreport')
@login_required
@admin_required
def generate_admin_report():
    print('admin reports')
    #here you can generate required data as per business logic
    return """
        <h1> This is admin report for {} </h1>
        <a href='/adminhome')> Go to Admin Features page </a>
    """.format(session['username'])

#Users Dashboard Page
@app.route('/users')
@admin_required
def users():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('SELECT * FROM users ORDER BY id')
    data = cur.fetchall()  
    cur.close()
    return render_template('users.html', user = data)
 
@app.route('/add_admin', methods=['POST'])
@admin_required
def add_admin():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        usertype = "admin"
        cur.execute("INSERT INTO users (name, email, password, usertype) VALUES (%s,%s,%s,%s)", (name, email, password, usertype))
        mysql.connection.commit()
        flash('Admin Added successfully','success')
        return redirect(url_for('users'))
    
@app.route('/add_user', methods=['POST'])
@admin_required
def add_user():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        usertype = "standard"
        cur.execute("INSERT INTO users (name, email, password, usertype) VALUES (%s,%s,%s,%s)", (name, email, password, usertype))
        mysql.connection.commit()
        flash('User Added successfully','success')
        return redirect(url_for('users'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
@admin_required
def get_details(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', user = data[0])
 
@app.route('/update/<id>', methods=['POST'])
@admin_required
def update(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s', (name, email, password, id))
        flash('Details Updated Successfully','success')
        mysql.connection.commit()
        return redirect(url_for('users'))
 
@app.route('/delete/<string:id>', methods = ['POST','GET'])
@admin_required
def delete(id):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('DELETE FROM users WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('The User has been removed successfully','success')
    return redirect(url_for('users'))

#Displaying Hotels Page
@app.route("/displayhotels")
@admin_required
def displayhotels():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM accomodation ORDER BY accCity")
    data = cur.fetchall()
    return render_template("displayhotels.html", hotel = data)

@app.route("/add_hotel_page")
def add_hotel_page():
    return render_template("addhotels.html")

@app.route('/add_hotel', methods=['POST'])
@admin_required
def add_hotel():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        id = request.form['accomodationid']
        city = request.form['city']
        address = request.form['address']
        features = request.form['features']
        fare = request.form['fare']
        roomtype = request.form['roomtype']
        smoking = request.form['smoking']
        cur.execute("INSERT INTO accomodation (idAccomodation, accCity, address, accFeatures, accFare, roomtype, smoking) VALUES (%s,%s,%s,%s,%s,%s,%s)", (id, city, address, features, fare, roomtype, smoking))
        mysql.connection.commit()
        flash('The Hotel has been added successfully','success')
        return redirect(url_for('displayhotels'))
    
@app.route('/hotelsedit/<id>', methods = ['POST', 'GET'])
@admin_required
def get_hoteldetails(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM accomodation WHERE idAccomodation = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('hotel_edit.html', hotel = data[0])

@app.route('/hotelsupdate/<id>', methods=['POST'])
@admin_required
def hotel_update(id):
    if request.method == 'POST':
        city = request.form['city']
        address = request.form['address']
        features = request.form['features']
        fare = request.form['fare']
        roomtype = request.form['roomtype']
        smoking = request.form['smoking']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('UPDATE accomodation SET accCity = %s, address = %s, accFeatures = %s, accFare = %s, roomtype = %s, smoking = %s WHERE idAccomodation = %s', (city, address, features, fare, roomtype, smoking, id))
        flash('The Hotel details have been updated successfully','success')
        mysql.connection.commit()
        return redirect(url_for('displayhotels'))

@app.route('/hotelsdelete/<string:id>', methods = ['POST','GET'])
@admin_required
def delete_hotel(id):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('DELETE FROM accomodation WHERE idAccomodation = {0}'.format(id))
    mysql.connection.commit()
    flash('The Hotel has been removed successfully','success')
    return redirect(url_for('displayhotels'))

#View Bookings Page
@app.route('/viewallbookings')
@admin_required
def viewbookings():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('SELECT * FROM accomodationbookings')
    data = cur.fetchall()  
    cur.close()
    return render_template('viewbookings.html', user = data)

@app.route('/viewuserbookings')
@admin_required
def viewuserbookings():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('SELECT * FROM accomodationbookings')
    data = cur.fetchall()  
    cur.close()
    return render_template('viewuserbookings.html', user = data)

@app.route('/add_booking', methods=['POST'])
@admin_required
def add_booking():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        checkin = request.form["Checkin"]
        checkout = request.form["Checkout"]
        accomodationid = request.form["Accomodationid"]
        numofguests = request.form["NoofGuests"]
        fare = request.form["Totalfare"]
        paymentstatus = 'N'
        cur.execute("INSERT INTO accomodationbookings (checkinDate, checkoutDate, idAccomodation, noOfGuests, totFare, paymentstatus) VALUES (%s,%s,%s,%s,%s,%s)", (checkin, checkout, accomodationid, numofguests, fare, paymentstatus))
        mysql.connection.commit()
        flash('The Custom Booking has been added successfully','success')
        return redirect(url_for('viewbookings'))
    
@app.route('/bookingedit/<id>', methods = ['POST', 'GET'])
@admin_required
def get_bookingdetails(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM accomodationbookings WHERE idBooking = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('booking_edit.html', booking = data[0])

@app.route('/userbookingedit/<id>', methods = ['POST', 'GET'])
@admin_required
def get_userbookingdetails(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM accomodationbookings WHERE idBooking = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('userbooking_edit.html', booking = data[0])

@app.route('/bookingupdate/<id>', methods=['POST'])
@admin_required
def booking_update(id):
    if request.method == 'POST':
        checkin = request.form['Checkin']
        checkout = request.form['Checkout']
        accomodationid = request.form['accomodationid']
        numofguests = request.form['numofguests']
        fare = request.form['fare']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('UPDATE accomodationbookings SET checkinDate = %s, checkoutDate = %s, idAccomodation = %s, noOfGuests = %s, totFare = %s WHERE idBooking = %s', (checkin, checkout, accomodationid, numofguests, fare, id))
        flash('The Booking details have been updated successfully','success')
        mysql.connection.commit()
        return redirect(url_for('viewbookings'))

@app.route('/userbookingupdate/<id>', methods=['POST'])
@admin_required
def user_booking_update(id):
    if request.method == 'POST':
        checkin = request.form['Checkin']
        checkout = request.form['Checkout']
        numofguests = request.form['numofguests']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('UPDATE accomodationbookings SET checkinDate = %s, checkoutDate = %s, noOfGuests = %s WHERE idBooking = %s', (checkin, checkout, numofguests, id))
        flash('The Booking details have been updated successfully','success')
        mysql.connection.commit()
        return redirect(url_for('viewuserbookings'))
    
@app.route('/bookingdelete/<string:id>', methods = ['POST','GET'])
@admin_required
def delete_booking(id):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('DELETE FROM accomodationbookings WHERE idBooking = {0}'.format(id))
    mysql.connection.commit()
    flash('The Booking has been removed successfully','success')
    return redirect(url_for('viewbookings'))

@app.route('/userbookingdelete/<string:id>', methods = ['POST','GET'])
@admin_required
def delete_userbooking(id):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('DELETE FROM accomodationbookings WHERE idBooking = {0}'.format(id))
    mysql.connection.commit()
    flash('The Booking has been removed successfully','success')
    return redirect(url_for('viewbookings'))

########################################
############ Booking Form ##############
########################################
@app.route('/getbooking')	
@login_required
# gets all distinc list of cities from DB and passes to html template for dynamic web page generation
def getbooking():
	conn = dbfunc.getConnection()
    #Checking if connection is none
	if conn != None:   
        #Prints 'MySQL Connection is established'
		print('MySQL Connection is established')                          
        #Creating cursor object
		dbcursor = conn.cursor()   
		dbcursor.execute('SELECT DISTINCT accCity FROM accomodation;')   		           
        #Fetches all the rows
		rows = dbcursor.fetchall()                                    
		dbcursor.close()              
		conn.close() #Connection must be 
		cities = []				#list of all cities where accomodation can be booked
		for city in rows:		#as we used fetchall we must clean the data
			city = str(city).strip("(")
			city = str(city).strip(")")
			city = str(city).strip(",")
			city = str(city).strip("'")
			cities.append(city)
		return render_template('booking.html', accCitylist=cities)
	else:
		print('DB connection Error')
		return 'DB Connection Error'

@app.route("/selectBooking", methods=["POST", "GET"])
@login_required
def get():
    if request.method == 'POST':
        accCity = request.form["accCitylist"]
        checkindate = request.form["checkindate"]
        checkoutdate = request.form["checkoutdate"]
        noofadults = request.form["noofadults"]
        noofchildren = request.form["noofchildren"]
        currencyfare = request.form["fare"]
        noofnights = datetime.strptime(checkoutdate, '%Y-%m-%d') - datetime.strptime(checkindate, '%Y-%m-%d')		
        lookupdata = [accCity, checkindate, checkoutdate, noofadults, noofchildren ,noofnights.days, currencyfare]
        conn = dbfunc.getConnection()	
        if conn != None:
            #Prints out 'MySQL Connection is Established'
            print('MySQL Connection is established')     
            #It prints out in terminal how many number of nights there are
            print(noofnights)
            #Creating Cursor Object
            dbcursor = conn.cursor()
            #Executing SELECT statement to get list of cities 
            dbcursor.execute('SELECT * FROM accomodation WHERE accCity = %s;', (accCity, ))
            print("SELECT statement executed successfully") 
            #Fetches all the rows
            rows = dbcursor.fetchall()   
            datarows = []                         
            
            #The Business logic for cost multiplication
            for row in rows:
                data = list(row)
                #Standard Price
                price = (int(row[1]))
                #Adding num of children plus num of adults
                acfare = (int(noofchildren) + int(noofadults))
                #Calculating the fare = standard rate * Per person
                acfare = (acfare * price)  
                #The Discount Process
                #If there are more than 45 days and less than 59 days chosen then 10% discount is applied    
                if (int(noofnights.days) > 45 and int(noofnights.days <= 59)):
                    discount = 0.95
                    acfare = acfare * discount      
                #If there are more than 60 days and less than 79 days chosen then 10% discount is applied    
                if (int(noofnights.days > 60) and int(noofnights.days <= 79)):
                    discount = 0.90
                    acfare = acfare * discount  
                #If there are more than 80 days and less than 90 days chosen then 20% discount is applied
                if (int(noofnights.days > 80) and int(noofnights.days <= 90)):
                    discount = 0.80
                    acfare = acfare * discount
                #Currency Conversion   
                if currencyfare == "GBP (British Pounds Sterling)":
                    acfare = acfare
                if currencyfare == "USD (United States Dollar)":
                    acfare = acfare * 1.6 
                if currencyfare == "EUR (Euros)":
                    acfare = acfare * 1.2 
                round(acfare,2)
                data.append(acfare)
                datarows.append(data)  
            #Flash Messages for discount and currency conversion
            if (int(noofnights.days) > 45 and int(noofnights.days <= 59)):
                flash('The 5% discount has been applied','success')  
            if (int(noofnights.days > 60) and int(noofnights.days <= 79)):
                flash('The 10% discount has been applied','success')  
            if (int(noofnights.days > 80) and int(noofnights.days <= 90)):
                flash('The 20% discount has been applied','success') 
            if currencyfare == "USD (United States Dollar)":
                flash("The GBP Price has been converted into USD Price, 1 GBP = 1.6 USD",'success')
            if currencyfare == "EUR (Euros)":
                flash("The GBP Price has been converted into EUR Price, 1 GBP = 1.2 EUR  ",'success')
            
            dbcursor.close()
            conn.close()
            return render_template('booking_start.html', resultset = datarows, lookupdata = lookupdata)

@app.route ('/booking_confirm/', methods = ['POST', 'GET'])
@login_required
def booking_confirm():
    if request.method == 'POST':
        print('Booking confirm initiated')
        accid = request.form['bookingchoice']
        print('Testing booking choice : ', accid)		
        acccity = request.form['acccity']	
        checkindate = request.form['checkindate']
        checkoutdate = request.form['checkoutdate']
        noofadults = request.form['noofadults']
        noofchildren = request.form['noofchildren']
        currencyfare = request.form['fare']
        noofnights = datetime.strptime(checkoutdate, '%Y-%m-%d') - datetime.strptime(checkindate, '%Y-%m-%d')
        totalfare = ''
        address = ''
        smoking = ''
        features = ''
        
        conn = dbfunc.getConnection()
        #Checking if connection is none
        if conn != None:
            print('MySQL Connection is established')    
            #Creating cursor object                                 	
            dbcursor = conn.cursor()
            #Executing the SELECT statement to get specified data from the idAccomodation table
            dbcursor.execute('SELECT accFare, smoking, address, accFeatures FROM accomodation WHERE idAccomodation = %s;', (accid,))
            #Fetches one row at a time
            row = dbcursor.fetchone()
            while row is not None:
                data = list(row)    
                #Adding the num of children and num of adults
                acfare = ( int(noofchildren) + int(noofadults))
                #This is the standard price
                price = (int(row[0]))
                #Calculating the fare = Standard Rate * Per person
                totalfare = (acfare * price)    
                
                #Discount Process   
                if (int(noofnights.days) > 45 and int(noofnights.days <= 59)):
                    discount = 0.95
                    totalfare = totalfare * discount      
                #If there are more than 60 days and less than 79 days chosen then 10% discount is applied    
                if (int(noofnights.days > 60) and int(noofnights.days <= 79)):
                    discount = 0.90
                    totalfare = totalfare * discount  
                #If there are more than 80 days and less than 90 days chosen then 20% discount is applied
                if (int(noofnights.days > 80) and int(noofnights.days <= 90)):
                    discount = 0.80
                    totalfare = totalfare * discount  
                    
                #Currency COnversion    
                if currencyfare == "GBP (British Pounds Sterling)":
                    totalfare = totalfare
                if currencyfare == "USD (United States Dollar)":
                    totalfare = totalfare * 1.6 
                if currencyfare == "EUR (Euros)":
                    totalfare = totalfare * 1.2 
                smoking = row[1]
                address = row[2]
                features = row[3]
                #Fetches one row at a time
                row = dbcursor.fetchone() 

            dbcursor.close()
            conn.close()
        cardnumber = request.form['cardnumber']
        #you can also get customer details entered in the form
        bookingdata = [accid, acccity, checkindate, checkoutdate, noofadults, noofchildren ,totalfare, address, smoking, features, noofnights.days]
        #Now we need to save booking data in DB
        conn = dbfunc.getConnection()
        if conn != None:
            print('MySQL Connection is established')                          
            #Creating Cursor Object
            dbcursor = conn.cursor()      	
            #This is a INSERT Statement to insert the specifie data into accomodationbookings table
            dbcursor.execute('INSERT INTO accomodationbookings (checkinDate, checkoutDate, idAccomodation, noOfGuests, totFare) VALUES (%s, %s, %s, %s, %s);', (checkindate, checkoutdate, accid, acfare, totalfare))   
            #This prints out 'booking statement executed successfully'
            print('Booking statement executed successfully.') 
            #It executes the INSERT statement into the database            
            conn.commit()
			#As bookingid is autogenerated so we can get it by running following SELECT
            dbcursor.execute('SELECT LAST_INSERT_ID();')			
            rows = dbcursor.fetchone()			
            bookingid = rows[0]
            bookingdata.append(bookingid)			
            #Slicing card number as displaying full card number is a security risk
            cardnumber = cardnumber[-4:16]
            #Prints out the last 4 digits of the card number
            print(cardnumber)
            dbcursor.execute
            dbcursor.close()
            #Connection must be closed
            conn.close()
            return render_template('booking_confirm.html', resultset=bookingdata, cardnumber=cardnumber )
        
#This route is a generic route and displays all the received data.. good for testing
@app.route ('/dumpsVar/', methods = ['POST', 'GET'])                             
@login_required
def dumpVar():
	if request.method == 'POST':
		result = request.form
		output = "<H2>Data Received: </H2></br>"
		output += "Number of Data Fields : " + str(len(result))
		for key in list(result.keys()):
			output = output + " </br> " + key + " : " + result.get(key)
		return output
	else:
		result = request.args
		output = "<H2>Data Received: </H2></br>"
		output += "Number of Data Fields : " + str(len(result))
		for key in list(result.keys()):
			output = output + " </br> " + key + " : " + result.get(key)
		return output  

################################
###########App Routes###########
################################
#Admin home page
@app.route("/adminhome")
@admin_required
def adminhome():
    return render_template('adminhome.html')

#User home page
@app.route("/userhome")
@login_required
def userhome():
    return render_template('userhome.html')

#View admin profile page
@app.route("/viewadminprofile")
@admin_required
def viewadminprofile():
    return render_template("viewadminprofile.html")

#View user profile page
@app.route("/viewuserprofile")
@login_required
def viewuserprofile():
    return render_template("viewuserprofile.html")

#Logout
@app.route("/logout")
def logout():
	session.clear()
	flash('You are now logged out','success')
	return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)