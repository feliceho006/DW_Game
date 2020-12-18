Your game
It is a survival game where the player chooses his/her actions for 5 weeks.
There are 5 endings:
1)Win
2)Lose, Virus Infection
3)Lose, Asymptomatic
4)Lose, Starvation
The goal is to get the highest points and survive.

How to play your game
1. If you reach ≤ 0 food, you will starve to death
2. If you are infected for 2 consecutive times, you will die
3. Going to the doctor will cure you of the virus but it costs 2pts
4. When infected, there is a 20% chance of being asymptomatic
5. Your goal is to reach the highest points and survive
6. Each day you go out, you have 20% chance of being infected.

Every week the player will have to choose if they want to go out to get food, stay home or go see a doctor, they will then either gain 1pt, lose 2pts or gain 0 pts respectively. At the end, if you are virus free and you dd not starve to death, you win.
Describe your code
The code uses the kv file to create the design of the game.
The checkbox allows for the actions to be appended into a list called self.dates. This list is the passed through the state machine.
 
This diagram depicts how the state machine works. There are 4 states and 3 inputs.
![[Pasted image 20201218104320.png]]
State 0 : Not Sick
State 1: Sick without Symptoms
State 2: Sick with Symptoms
State 3: Death
Input 0: Stay home
Input 1: Go get food
Input 2: See a doctor

If state is not 3, player is not dead yet:
For staying at home,input 0, state = state
For seeing a doctor, input 2, state = 0
For going to get food, input 1, there is 20% chance of being infected and when infected there is 20% chance of not showing symptoms.
This state machine will the return the state as well as the points as the output.

At the end of the game, when Quit is selected, the app will close. When restart is selected the game will restart.