REGISTER + LOGIN

I used the Register/Login design from the CS50 design pset, but I added an additional password restriction. I required that the password must be at least 5 characters long so that it is stronger and harder for bots to guess the password and hack the user’s account.

NEW GAME

The new game page requests that the user inserts a team name. If the user does not insert a team, an error message will appear. Since the site is intended to be used as the user is watching the game in real time ie not watching a game that has already happened.  The date of the game should be the date that the user inserted the data, so i imported the date from the datetime python package and recorded the date as date.today()

Once the team is inserted, an id for that game is created and stored under game_id. Also, the user id, team, and date is inserted into the games database that records these values for each game. The game is then stored into session[“game id”] so  that the game id can be remembered and used in other python functions.When the new_game function is posted it will redirect to the new pitchers html

NEW PITCHERS

I decided to make the form for a new pitcher to be on a separate page from the new game because there can be multiple pitchers put into play in one game. For example, if one pitcher is getting hit a lot, the coach might take that pitcher out of the game, and put in a new pitcher. Putting the form on separate pages makes it easier to keep the samegame id of the session as the new game form automatically redirects to the new pitcher page once the team is inserted. When inserting a new pitcher, the form asks for the pitchers last name and first name. Originally, I had only a single name request form, but I found that when the user inserted the first and last name Such as name: Billy Joel. The database sql would not read the space between billy and joel and there would be an error message. However, if the user inputed just Billy, the code would work.I thought that the last name of the pitcher is important as there could be two pitchers on the same team with the same first name. So I had first name and last name as two different data fields in the pitchers database. The schema for the pitchers database is as follows:

CREATE TABLE pitchers (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
user_id INTEGER NOT NULL,
game_id INTEGER NOT NULL,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
FOREIGN KEY (user_id) REFERENCES users(id)
FOREIGN KEY (game_id) REFERENCES games(id)
);

Like I mentioned before, there could be multiple pitchers per game and I wanted to keep track of who pitched in what game, so I had game_id reference games(id)

If the user did not insert any characters into the first and last name and error message would appear. The first and last names are also converted into all uppercase characters via the .upper() function so that type case is not a factor into the user’s input. Ie TaYLoR swIFT will read as TAYLOR SWIFT  and taylor swift will also be read by the code as TAYLOR SWIFT and it will process that they are the same person.

Similar to what I did in the new game, I inserted the pitcher’s first and last name, the user’s id, and the game id into the pitchers database. The db.execute of this returns the id of the entry, so I stored that as pitcher_id and stored that into the session so that pitcher_id can be used in other functions. Once all fields are inserted, it will redirect the user to the new pitch page.

NEW PITCH

Similar to the new pitcher page, I wanted there to be a separate page for the user to input the pitch type and count because a pitcher throws multiple pitches in a game.

However, since there are only 5 pitch types and 12 possible counts. I decided that it would be best if I had an option form instead of an open-ended response form. This way the user cannot enter a count that is not possible like a 4-0 count, and I would have to code less checks to see if the user inputted a plausible pitch count and pitch type. Also, there was no pre-selected pitch types or pitch count to ensure that the user doesnt accidentally insert a wrong value.

If the user does not enter a pitch or pitch count, they will receive an error message.

The code then inserts the pitcher id, user id, the pitch type, and pitch count into the pitches database. It then redirects to the index html page.

This is the schema for the pitches database.

CREATE TABLE pitches (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
user_id INTEGER NOT NULL,
pitcher_id INTEGER NOT NULL,
name text NOT NULL,
pitch_count text NOT NULL,
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (pitcher_id) REFERENCES pitchers(id)
);

Because I want to keep track of the pitcher that threw each pitch pitcher_id REFERENCES pitchers(id)

INDEX

THE INDEX IS WHERE THE MAGIC HAPPENS!

Firstly, I select the first and last names of the pitcher and the team that the pitcher is on with the pitcher id from the pitchers.

Next, I select the name and the pitch count of the pitches that the pitcher threw from the pitches table and store them into a global dictionary called pitches. I made it a global variable so it can be used in other functions.

IF the pitcher has not thrown a pitch an error message is displayed
Since there are only 12 possible pitch counts I made a list of all possible counts.

Then for each item/pitch in the pitches dictionary, there is an empty percentages list. I then used a nested for loop within the for pitch in pitches for loop to calculate the frequency that that pitch was thrown in a certain count. I did this as follows . For each count in the pitch_count list I selected the name(important to note that name is the name of the pitch ie CURVE. Not the name of the pitcher)  and number of pitches thrown in each count for that specific pitch type from the pitches table. I stored this information in a dictionary called total.

Next, I selected the number of pitches thrown in each distinct count REGARDLESS OF THE PITCH TYPE into a dictionary called total_count.

This can be confusing so let me exemplify. The pitcher can throw 20 pitches in a 0-0, but only 5 of those pitches were curve balls. Total_count[0][“total_count”] will store 20 while total[0][“total”] will store 5.

To calculate the frequency that the pitcher throws a specific pitch in a specific count. I divide total[0][“total”] by total count, and multiply it by 100, then use the integer wrapper class to store the value as an integer since the above operation would have stored it as a string. Next, I append that to the percentages list which adds a new percentage per count per pitch.

Since 5/20 * 100 is 25, the percentages list should contain [25,0,0,0,0,0,0…0]

To keep track of the percentage per pitch, I temporarily make a new field in pitch called percentages where I store the percentages list.

 If the number of pitches thrown in that count(total_count) is 0, 0 will append to the percentages list. I had to write that if statement because otherwise if total_count is zero, then you will get a divide by 0 error in the terminal.

I initialize percentages=[] as an empty list under the for pitch in pitches loop, so that the percentages list restarts for every pitch, and the percentages list do not append on top of each other for different pitches. This is a problem I was running into before.


The function then transfers pitches, first_name,last_name, and team into the index html so that the frequency chart is displayed along with the pitcher's name and what team they play for. This way you can be certain for what pitcher and team you are charting for.

PAST GAMES

The past games function is very simple; it just displays the opposing team of the game and the date at which the data for that game was entered based on another user’s id. I thought this was necessary to keep track of how many games were played and when. This data is useful when searching for pitchers.

SEARCH PITCHERS


To search for the pitch frequency chart of a pitcher in a certain game, the user inputs the opposing team’s name of that game, as well as the date they played, and the first and last name of the pitcher. When searching for a pitcher in a certain game the date is important because you can play the same team on a different day, so it is important to specify which day.

It then selects the id from pitchers where the pitcher’s first and last name match with the user’s input.

Then using the exact same process as the index function, it calculates the frequency of each pitch thrown per count as a percentage. The html then displays the percentage table, however this time it displays the date of the game, so you know which game day and which pitcher the data is for.

THATS ALL I HOPE YOU ENJOYED MY CODE.




