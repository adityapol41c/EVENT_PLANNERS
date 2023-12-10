from flask import Flask, render_template,jsonify,redirect,request,url_for,session,flash
import sqlite3
import jwt
from datetime import datetime, timedelta,timezone

app = Flask(__name__)
app.secret_key="123"

con=sqlite3.connect("realwork.db")
con.execute("create table if not exists users(uid integer primary key,name text,email text,password text)")
con.execute("create table if not exists contact(name text,email text,message test)")

con.close()

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        con=sqlite3.connect("realwork.db")
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from users where email=? and password=?",(email,password))
        data=cur.fetchone()
        

        if data:
            session["email"]=data["email"]
            session["password"]=data["password"]
            # session["email"]="k@gmail.com"
            # session["password"]="k@gmail.com"
            session['logged_in'] = True
            token = jwt.encode({
                'user': request.form['email'],
                "exp": datetime.now(tz=timezone.utc)
            },
            app.config['SECRET_KEY'])
            return render_template("index.html")
        else:
            flash("username and password mismatch","warning")
    return redirect(url_for("signup"))

@app.route("/welcome", methods=['GET','POST'])
def welcome():
    return render_template("welcome.html")


@app.route('/')
def hello_world():
    return render_template("index.html")
   
@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

   
@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/checking')
def checking():
    print(session.get('logged_in'))
    if not session.get('logged_in'):
        return jsonify({"Value": "False"})
    else: 
        return  jsonify({"Value": "True"})

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        con=sqlite3.connect("realwork.db")
        cur=con.cursor()
        cur.execute("insert into contact(name,email,message)values(?,?,?)",(name,email,message))
        con.commit()
    return redirect(url_for("aboutus"))

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method=='POST':
        try:
            name=request.form['name']
            email=request.form['email']
            password=request.form['password']
            print(name,email,password)
            con=sqlite3.connect("realwork.db")
            cur=con.cursor()
            con.execute("insert into users(name,email,password)values(?,?,?)",(name,email,password))
            con.commit()
            flash("record added successfully","success")
        except:
            flash("error in insert operation","danger")
        finally:
            return render_template("index.html")
            con.close()
    return render_template("signup.html")

@app.route('/package')
def package():
    return render_template("package.html")

@app.route('/moreDetails')
def moreDetails():
    return render_template("moreDetails.html")


@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/card',methods=['GET'])
def card():
    card =[
    {
        "id": 1,
        "header": "Bronze",
        "subtitle": "Best Bronze option for personal use & for your event planning.",
        "price": "999"
    },
    {
        "id": 2,
        "header": "Gold",
        "subtitle": "Best gold option for personal use & for your event planning.",
        "price": "2999"
    },
    {
        "id": 3,
        "header": "Platinum",
        "subtitle": "Best platinum option for personal use & for your event planning.",
        "price": "4999",
    }
]
    return jsonify(card)

@app.route('/data',methods=['GET'])
def data():
    data = [
    {
        "id":1,
        "place": "Nerul",
        "Event": "Marriage",
        "Name": "Welcome Hall Nerul",
        "Price": "25000",
        "accommodation": 250,
        "img": "https://lh3.googleusercontent.com/uUJiwzZmgTEei4Po8zbIccZmvZ_SdI19iuFzs8UiN1Sb8o4rLARGtyNYOHdviaGPXD-jN73PaZ9OMQHvWtHlnXpG=w746-h498-l95-e31"
        
    },
    {
        "id":2,
        "place": "Nerul",
        "Event": "Birthday",
        "Name": "Kff Banquet Hall (Party Hall)",
        "Price": "15000",
        "accommodation": 150,
        "img": " https://www.chennaiconventioncentre.com/wp-content/uploads/2019/03/ccc-blog-824x412.jpg"

    },
    {
        "id":3,
        "place": "Nerul",
        "Event": "Marriage",
        "Name": "Jhulelal Mandir Banquet Hall",
        "Price": "35000",
        "accommodation": 300,
        "img": "https://lh3.googleusercontent.com/uUJiwzZmgTEei4Po8zbIccZmvZ_SdI19iuFzs8UiN1Sb8o4rLARGtyNYOHdviaGPXD-jN73PaZ9OMQHvWtHlnXpG=w746-h498-l95-e31"

    },
    {
        "id":4,
        "place": "Nerul",
        "Event": "Baby shower",
        "Name": "Sterling Banquet & Lawn",
        "Price": "10000",
        "accommodation": 120,
        "img": "https://www.7eventzz.com/public/media/original-images/1644221028_0.jpg"
    },
    {
        "id":5,
        "place": "Juinagar",
        "Event": "Baby shower",
        "Name": "Celebrations Banquet",
        "Price": "16000",
        "accommodation": 150,
        "img": "https://www.7eventzz.com/public/media/original-images/1644221028_0.jpg"
    },
    {
        "id":6,
        "place": "Juinagar",
        "Event": "Birthday",
        "Name": "Aansha Banquet Hall",
        "Price": "26000",
        "accommodation": 350,
        "img": "https://www.chennaiconventioncentre.com/wp-content/uploads/2019/03/ccc-blog-824x412.jpg"

    },
    {
        "id":7,
        "place": "Belapur",
        "Event": "Marriage",
        "Name": "Sankalp Bhavan",
        "Price": "23000",
        "accommodation": 320,
        "img": "https://lh3.googleusercontent.com/uUJiwzZmgTEei4Po8zbIccZmvZ_SdI19iuFzs8UiN1Sb8o4rLARGtyNYOHdviaGPXD-jN73PaZ9OMQHvWtHlnXpG=w746-h498-l95-e31"

    },
    {
        "id":9,
        "place": "Seawood",
        "Event": "Clubbing",
        "Name": "Clubbing Hall",
        "Price": "13000",
        "accommodation": 140,
        "img": "https://www.chennaiconventioncentre.com/wp-content/uploads/2019/03/ccc-blog-824x412.jpg"

    }

]
    return jsonify(data)


@app.route('/paymentGateway')
def paymentGateway():
    return render_template("paymentGateway.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__=="__main__":
    app.run(debug=True, port=8000)
    