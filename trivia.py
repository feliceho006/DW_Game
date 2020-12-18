import json
import random
import time
from libdw import sm


# print(data['results'][3]['incorrect_answers'])

class Point(sm.SM):
    start_state = 0

    def __init__(self):
        self.balance = 0

    def get_next_values(self, state, inp):
        state = self.balance
        self.balance = state + inp
        return self.balance, self.balance


def show_question(questionDB, i):
    print(chr(27) + "[2J")
    print("question "+str(i)+" of "+" 10")
    r = random.randint(0, 49)
    print(questionDB['results'][r]['question'])
    ansList = []
    for ans in questionDB['results'][r]['incorrect_answers']:
        ansList.append(ans)
    correct_ans = questionDB['results'][r]['correct_answer']
    ansList.append(correct_ans)

    random.shuffle(ansList)

    for i in range(len(ansList)):
        print(str(i)+":"+ansList[i])

    player_ans = int(input("Your answer: "))
    if player_ans > 3:
        print("Wrong!")
        time.sleep(2)
        return 0
    if ansList[player_ans] == correct_ans:
        print("Correct!")
        time.sleep(2)
        return 1
    else:
        print("Wrong!")
        time.sleep(2)
        return 0


def main():
    username = str(input("Hi! Please enter your username: "))
    total_points = Point()
    json_file = './quizdb.json'
    with open(json_file) as json_data:
        data = json.load(json_data)
    total_points.start()
    for i in range(10):
        total_points.step(show_question(data, i))
    print("Congrats "+username+"! Your total score is: "+str(total_points.balance))


main()
