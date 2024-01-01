HELLO AND WELCOME TO PITCH TRACKER

BACKGROUND INFORMATION
The purpose of this website is to track the pitch type the pitcher throws in certain counts to investigate if there is a pattern. This site will calculate and display the frequency of a pitch in a certain count as a percentage. For example, the pitcher throws a rise ball in a 1-0 count 70% of the time. If you are unfamiliar with the sport of baseball/softball a count is the number of balls-strikes, so a 1-0 count means that the pitcher has thrown 1 ball and 0 strikes to the batter. A ball is a pitch that the umpire deems the batter CAN’T HIT and a strike is a pitch that the umpire deems the batter CAN HIT. If the pitcher throws 4 balls, the batter WALKS to 1st base. If the pitcher throws 3 strikes before the batter hits the ball, the batter is OUT! Because of this, there are only 12 possible counts are 0-0,0-1,0-2, 1-0,1-1,1-2,1-0,1-1,1-2,2-0,2-1,2-2,3-0,3-1,3-2,
None of this is particularly relevant to how to use the site but some people do not know how softball works and what a count is :).  IMPORTANT: THIS SITE IS INTENDED FOR SOFTBALL PLAYERS ONLY AND INCLUDES ONLY THE DIFFERENT TYPES OF SOFTBALL PITCHES IE DROP,CHANGE-UP,RISE,CURVE,SCREW. IT DOES NOT INCLUDE THE DIFFERENT TYPES OF BASEBALL PITCHES LIKE SLIDER, FOUR-SEAM FASTBALL, SINKER, ETC.

Please note that in this explanation I use you and the user Interchangably because YOU ARE THE USER!

RUN THE CODE

In order to run the code, you are going to need to log into code.cs50.io. Type cd pitch_tracker in order to access the directory of the Pitch Tracker Code File.  Then type flask run into the terminal. A url should pop up. Click on it to bring you to the site. Note: if it does not work type /login at the end of the url.

REGISTER AND LOG IN
Once on the site, you want to register your account. Make a unique username and password that is more than 5 characters long. Once that password is confirmed, you can type that same username and password in order to log in.

When you log in, you will be directed to a  page that shows all of the previous games you have inserted data for and display the name of the opposing team of that game and the date of the game in yyyy-mm-dd format. Since you are a new user, there will not be any game data on the page.

NEW GAME AND NEW PITCHER
To create new game data, click on the new game tab and insert the name of the opposing team. You will be redirected to the new pitcher page in which case you will enter the pitcher’s first and last name. The user can find the pitcher’s name by looking at the pitcher’s jersey number and matching it with the player’s number on the opposing team’s roster.

NEW PITCH

After you insert the pitcher’s first and last name, you will be redirected to the new pitch page. Watch the pitcher throw a pitch and identify whether it is a curve, rise, screw, or drop ball, choose the pitch type and the count in which the pitch was thrown in. Once the data is inserted, you will be redirected to a page displaying the frequency chart for that pitch type in a certain count as a percentage. For instance, if the first pitch you inserted was a screw ball in a 0-0 count, you should see Screw: 100,0,0,0,0,0,0,0,0. Since the pitcher only threw one screw ball in a 0-0 count, she has thrown a screwball in a 0-0 count 100% of the time. The frequency depends on the pitch count. For instance, if you next inserted a rise ball in a 0-0 count, table will display Screw: 50,0,0,0,0… and Rise: 50,0,0,0,0… to show that the pitcher throws a screwball 50% of the time in a 0-0 count and a rise ball the other 50% of the time. If the pitcher throws a screwball in a 0-1 count, the frequency table for a screwball should be 50,100,0,0,0,0,0. This means that the pitcher throws a screwball in a 0-0 count 50% of the time and in a 0-1 count 100% of the time.

Note: this site is intended to be used in real time, so as the game is going on and the user is watching it, the user will insert the name of the pitcher, the pitch count, and the pitch type after the pitcher has thrown each pitch. It is also assumed that the user is knowledgeable about softball pitches and will be able to identify what type of pitch was thrown by its spin. In general, a change-up is a slow pitch, a curve spins away from a right handed batter, a screw spins toward a right handed batter, a drop ball spins down and is a low pitch, a rise ball spins up and is a high pitch.

The user can click on the New pitch tab to insert a new pitch and on the New Pitcher tab if they want to insert information on a new pitcher that has just entered the same game and record a pitch frequency chart for that pitcher. If the user wants to exit out of the game, they can select Past games.

Once past games are clicked, the opposing team and date of the game that you have just inserted data for will appear in the past games table.

SEARCH PITCHERS

If you want to see the pitch frequency chart for a pitcher in a previous game, you should click on the search pitchers tab and insert the opposing team, the date of the game in yyyy-mm-dd format, and the pitcher's first and last name. If you insert the information correctly, you will see the pitch frequency chart for that pitcher for that game. If you insert the date in the wrong format or that pitcher does not exist for that game, you will get an error message. If the user is unsure of the date that the game was played, they can look at the past games page.

 Note: The past game page does not display the pitchers that played in each game, so it is assumed that when searching for pitchers, the user will know the name of the pitcher that they are looking for and what team they play for. If not, they can search online for the opposing team’s roster, find the names of their pitchers, and use the search pitchers tab to see if they played in that specific game.


THAT’S IT.
That’s it! That is how you use the site! Now that you know how to navigate it, click log out to take you back to the login page.

Here is a quick youtube video of me showing you how website works! https://youtu.be/-NBmvyClWHc

If the link does not work, search Lael Ayala CS50 final project-Pitch tracker in youtube
