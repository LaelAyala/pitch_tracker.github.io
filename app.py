# MY PERSONAL TOUCH WAS THAT THE PASSWORD NEEDED TO BE LONGER THAN 5 CHARACTERS
# MY PERSONAL TOUCH WAS THAT THE PASSWORD NEEDED TO BE LONGER THAN 5 CHARACTERS
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from datetime import date
from decimal import Decimal

current_datetime = datetime.now()

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Custom filter


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///tracker.db")




@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required

# MY PERSONAL TOUCH WAS THAT THE PASSWORD NEEDED TO BE LONGER THAN 5 CHARACTERS
def index():

    """Show frequency  of pitch in each count"""



    names = db.execute("SELECT first_name,last_name FROM pitchers WHERE user_id = ? AND id = ?", session["user_id"], session["pitcher_id"] )
    first_name= names[0]["first_name"]
    last_name= names[0]["last_name"]



    global pitches

    #selects name and pitch count from pitches with the same pitcher id
    pitches = db.execute("SELECT name, pitch_count FROM pitches WHERE user_id = ? AND pitcher_id = ? GROUP BY name HAVING COUNT(pitch_count) > 0", session["user_id"], session["pitcher_id"] )



    #team the pitcher plays on
    team = db.execute("SELECT team FROM games JOIN pitchers ON games.id = pitchers.game_id JOIN pitches ON pitchers.id = pitches.pitcher_id WHERE games.user_id = ? AND pitcher_id =? AND game_id =?", session["user_id"], session["pitcher_id"],session["game_id"])[0]["team"]


    """
    what i am trying to do:
    calculate the percentage of pitches the pitcher throws at each count.
    to do this i need to record the number of pitches the pitcher throws at each count
    the total number of pitches
    and the type of pitch at that count

    """




    global pitch_count
    pitch_count = ["0-0", "0-1", "0-2","1-0", "1-1","1-2","2-0","2-1","2-2","3-0","3-1","3-2"]

    for pitch in pitches:

        global percentages
        percentages=[]

        for i in pitch_count:

            #records the name of the pitch and the and number of pitches thrown in each count for that specific pitch type from the pitches table."
            total = db.execute("SELECT name, COUNT(pitch_count) as total FROM pitches WHERE pitch_count=? AND user_id = ? AND pitcher_id = ? AND name = ?", i, session["user_id"], session["pitcher_id"], pitch["name"])

            #Next, I selected the number of pitches thrown in each distinct count REGARDLESS OF THE PITCH TYPE into a dictionary called total_count.
            total_count = db.execute("SELECT COUNT(pitch_count) as total_count FROM pitches WHERE pitch_count = ? AND user_id = ? AND pitcher_id = ?" , i ,session["user_id"],session["pitcher_id"])[0]["total_count"]


            if int(total_count)==0:
                percentages.append(0)
            else:
                #adds percentage of pitches throw in that count that were that specific type to the percentages list
                percentages.append(int((total[0]['total']/ total_count)*100))
                pitch["percentages"] = percentages


    return render_template("index.html", pitches=pitches, first_name=first_name, last_name=last_name, team=team)






@app.route("/new_pitch", methods=["GET", "POST"])
@login_required
def new_pitch():
    if request.method == "GET":
        return render_template("new_pitch.html")
    """insert what pitch the pitcher is throwing"""
    if request.method == "POST":
        pitch= request.form.get("pitch")
        pitch_count = request.form.get("count")


        #if the user does not enter a pitch or a pitch count a error will appear"
        if not pitch:
            return apology("Enter a pitch",400)

        if not pitch_count:
            return apology("Enter a count",400)

        else:
            #inserts values into the pitches database
            db.execute("INSERT INTO pitches (pitcher_id,user_id,name,pitch_count) VALUES (?,?,?,?)", session["pitcher_id"],session["user_id"], pitch, pitch_count)
            return redirect("/")


@app.route("/new_game", methods=["GET", "POST"])
@login_required
def new_game():
    if request.method == "GET":
        return render_template("new_game.html")
    """ make a new game """
    if request.method == "POST":
        team= request.form.get("team").upper()
        #user_id = session["user_id"]
        #time = date.today()


        #if the user does not type in a team name this error message will appear
        if not team:
            return apology("Enter a TEAM",400)

        #inserts the user id, team, and date that the game data was inserted into the games database
        else:
            game_id=db.execute("INSERT INTO games (user_id,team,Date) VALUES (?,?,?)", session["user_id"], team, date.today())

            #The game is then stored into session[“game id”] so  that the game id can be remembered and used in other python functions.
            session["game_id"]= game_id
            return redirect("/new_pitcher")


@app.route("/new_pitcher", methods=["GET", "POST"])
@login_required
def new_pitcher():
    if request.method == "GET":
        return render_template("new_pitcher.html")
    """ insert a new pitcher per game since there can be multiple pitchers in one game """
    if request.method == "POST":
        first_name = request.form.get("first_name").upper()
        last_name = request.form.get("last_name").upper()



        #if user does not type anything into the pitcher field an error message will appear
        if not first_name:
            return apology("Enter a pitcher first name",400)

        #if user does not type anything into the las name field and error message will appear
        if not last_name:
            return apology("Enter a pitcher last name",400)


        else:
            pitcher_id = db.execute("INSERT INTO pitchers (game_id,user_id,first_name,last_name) VALUES (?,?,?,?)",session["game_id"], session["user_id"], first_name,last_name)
            session["pitcher_id"]= pitcher_id
            return redirect("/new_pitch")




@app.route("/past_games")
@login_required
def past_games():
    """Show the opposing team name and the date for previous games"""
    rows = db.execute("SELECT team, Date FROM games WHERE user_id = ?", session["user_id"])
    if rows =="":
        return render_template("new_game.html")
    else:
        return render_template("past_games.html", rows = rows)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/past_games")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/search_pitchers", methods=["GET", "POST"])
@login_required
def search_pitchers():
    if request.method == "GET":
        return render_template("search_pitchers.html")
    team= request.form.get("team").upper()
    date= request.form.get("date")
    first_name= request.form.get("pitcher_first").upper()
    last_name= request.form.get("pitcher_last").upper()

    #gets id of the pitcher that the user is searching for
    pitcher_id = db.execute("SELECT id FROM pitchers WHERE user_id = ? AND first_name = ? AND last_name = ?", session["user_id"], first_name, last_name)[0]["id"]




    # Query database for pitches for that specific pitcher
    pitches = db.execute("SELECT DISTINCT pitches.name, pitch_count FROM pitches JOIN pitchers ON pitches.pitcher_id = pitchers.id JOIN games ON pitchers.game_id = games.id WHERE pitches.user_id =? AND team =? AND Date =? AND pitchers.first_name =? AND pitchers.last_name = ?", session["user_id"], team, date, first_name,last_name)

    if len(pitches) == 0:
        return apology("No such team and pitcher and date. try inserting date as yyyy-mm-dd", 403)


    global pitch_count
    pitch_count = ["0-0", "0-1", "0-2","1-0", "1-1","1-2","2-0","2-1","2-2","3-0","3-1","3-2"]

    for pitch in pitches:

        global percentages
        percentages=[]

        for i in pitch_count:

            #records the name of the pitch and the and number of pitches thrown in each count for that specific pitch type from the pitches table."
            total = db.execute("SELECT name, COUNT(pitch_count) as total FROM pitches WHERE pitch_count=? AND user_id = ? AND pitcher_id = ? AND name = ?", i, session["user_id"], pitcher_id, pitch["name"])

            #Next, I selected the number of pitches thrown in each distinct count REGARDLESS OF THE PITCH TYPE into a dictionary called total_count.
            total_count = db.execute("SELECT COUNT(pitch_count) as total_count FROM pitches WHERE pitch_count = ? AND user_id = ? AND pitcher_id = ?" , i ,session["user_id"],pitcher_id)[0]["total_count"]


            if int(total_count)==0:
                percentages.append(0)
            else:
                #adds percentage of pitches throw in that count that were that specific type to the percentages list
                percentages.append(int((total[0]['total']/ total_count)*100))
                pitch["percentages"] = percentages


    return render_template("past_pitches.html", pitches=pitches, first_name=first_name, last_name=last_name, team=team, date=date)
"""
    global pitch_count
    pitch_count = ["0-0", "0-1", "0-2","1-0", "1-1","1-2","2-0","2-1","2-2","3-0","3-1","3-2"]
     # Ensure pitcher for that game
    if len(pitches) == 0:
        return apology("No such team and pitcher and date. try inserting date as yyyy-mm-dd", 403)
    for pitch in pitches:

        global percentages
        percentages=[]

        for i in pitch_count:

            total = db.execute("SELECT name, COUNT(pitch_count) as total FROM pitches WHERE pitch_count=? AND user_id = ? AND pitcher_id = ? AND name = ?", i, session["user_id"], pitcher_id, pitch["name"])

            #Next, I selected the number of pitches thrown in each distinct count REGARDLESS OF THE PITCH TYPE into a dictionary called total_count.
            total_count = db.execute("SELECT COUNT(pitch_count) as total_count FROM pitches WHERE pitch_count = ? AND user_id = ? AND pitcher_id = ?" , i ,session["user_id"],pitcher_id)[0]["total_count"]


            if int(total_count)==0:
                percentages.append(0)
            else:
                percentages.append(int((total[0]['total']/ total_count)*100))
                print(percentages)
                pitch["percentages"] = percentages
    return render_template("past_pitches.html", first_name = first_name, last_name= last_name, team = team, date = date, pitches = pitches) ##left is html right is python name
"""

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # MY PERSONAL TOUCH WAS THAT THE PASSWORD NEEDED TO BE LONGER THAN 5 CHARACTERS
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":

      username= request.form.get("username")
      password = request.form.get("password")
      confirmation = request.form.get("confirmation")

      if len(db.execute('SELECT username FROM users WHERE username = ?', username)) > 0:

         return apology("You are already registered",400)

      elif username == "":
        return apology("Insert a username",400)

      elif password == "":
        return apology("Insert a password",400)

      elif password != confirmation:
        return apology("Passwords do not match",400)
      # MY PERSONAL TOUCH WAS THAT THE PASSWORD NEEDED TO BE LONGER THAN 5 CHARACTERS
      elif len(password) < 5:
        return apology("Insert a password longer than 5 characters")
      else:
          db.execute("INSERT INTO users (username,hash) VALUES(?,?)", username,generate_password_hash(password))
           # Query database for username
          rows = db.execute("SELECT * FROM users WHERE username = ?", username)
            # Log user in, i.e. Remember that this user has logged in
          session["user_id"] = rows[0]["id"]
          return redirect("/login")



