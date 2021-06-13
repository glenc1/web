import random
import time
import matplotlib.pyplot as plt

csvFile = open("randomwords.csv")
text = csvFile.read()
text = text.replace('\n', ' , ')

listFromString = text.split(',')
continuePlaying = 'y'
scores = []

while continuePlaying == 'y':

    counter = 0
    newList = []

    while counter < len(listFromString):
        counter += 1
        newList.append(random.choice(listFromString).strip())    
    print (newList)
    startingTime = time.time()
    userInput = input('Type Here:')

    endingTime = time.time()
    timePassed = endingTime - startingTime
    userList = userInput.split(' ')
    numberOfWordsTyped = 0

    for wordNumber in range(len(userList)):
        if wordNumber <= (len(newList) - 1):
            if userList[wordNumber] == newList[wordNumber]:
                numberOfWordsTyped += 1

    wordsPerMinute = round((60 * numberOfWordsTyped) / timePassed)
    scores.append(wordsPerMinute)
    print (str(wordsPerMinute ) + " is your score")
    continuePlaying = input('Do you want to try again? Type y for yes or n for no.')
    while continuePlaying != 'y' and continuePlaying != 'n':
         continuePlaying = input('Please enter a valid input. Type y for yes or n for no.')

scoreCounter = 1
numberOfGames = []
while scoreCounter <= len(scores):
    numberOfGames.append(scoreCounter)
    scoreCounter += 1    
plt.plot(numberOfGames, scores)
plt.xticks(numberOfGames)
plt.title('Your Results')
plt.xlabel('Number Of Tests')
plt.ylabel('WPM')
plt.show()