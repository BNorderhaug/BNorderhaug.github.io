import random 
from flask import Flask, render_template, url_for, redirect, request 
from app import app

#Initialize app
app = Flask(__name__)
app.debug = True
#Open words file and split it apart
file = open('words.txt', "r")
word = filename.read().split()
#Get rid of all ' characters
words = [z.replace("'", "") for z in word]


#Create Passwords function
def createPasswords():
	
	possible = []
	used = []
	#Get userSelections from XKCD page
	userSelection = request.form.getlist('answer')
	#Possible implementation of longer words later
	while len(possible) < 4:
		#Get random word
		randomindex = random.randrange(0,len(words))
		if randomindex not in used:
			possible.append(words[randomindex])
			used.append(randomindex)
	
	#Go through and change each of the selected userSelections.
	for i in range(len(userSelection)):
		if userSelection[i] == "3":
			possible = [z.replace("e", "3") for z in possible]
		if userSelection[i] == "4":
			possible =[z.replace("a", "4") for z in possible]
		if userSelection[i] == "1":
			possible = [z.replace("i", "1") for z in possible]
		if userSelection[i] == "0":
			possible =[z.replace("o", "0") for z in possible]
		if userSelection[i] == "5":
			possible =[z.replace("s", "5") for z in possible]

		if userSelection[i] == "firstcap":
			possible = [possible[0][1].upper() + possible[0][2:]] + possible[1:]
		if userSelection[i] == "secondcap":
			possible = [possible[0]] + [possible[1][1].upper() + possible[1][2:]] + [possible[2]] + [possible[3]]
		if userSelection[i] == "thirdcap":
			possible = [possible[0]] + [possible[1]] + [possible[2][1].upper() + possible[2][2:]] + [possible[3]]		
		if userSelection[i] == "fourthcap":
			possible = [possible[0]] + [possible[1]] + [possible[2]] + [possible[3][1].upper() + possible[3][2:]]
	

	possiblefinal = " ".join(possible)
	return possiblefinal


#Initial Template
@app.route('/create', methods=['GET','POST'])
def genwords():
	return render_template('XKCDPassword.html') 

#Return results
@app.route('/results', methods=['GET','POST'])
def results():
	newwords = []
	for i in range(10):
		newwords.append(createPasswords())
	return render_template('Results.html', passwords = newwords)

#Run app
if __name__ == "__main__":
	app.run()