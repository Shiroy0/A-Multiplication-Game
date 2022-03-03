import random, time
numberOfQuestions = 10
correctAnswers = 0
numberofGuesses = 3
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (questionNumber + 1, num1, num2)
    print(prompt)
    for guessNumber in range(numberofGuesses):
        while True:
            try:
                guess = int(input())
                break
            except ValueError:
                print('Plz enter a number:')
                continue
        if(guess == num1*num2):
            print('Correct!')
            correctAnswers += 1
            time.sleep(1)
            break
        else:
            print('Incorrect!')
        if(guessNumber == numberofGuesses - 1):
            print("You're out of tries, next question!")
print('you got %s questions right!' % correctAnswers)
