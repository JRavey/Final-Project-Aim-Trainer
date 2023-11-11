# Final Project: Aim Trainer || [Repository Link](https://github.com/JRavey/Final-Project-Aim-Trainer/tree/main)

## Description

I will be creating an aim trainer using Python. I am focusing on user-program interactions.

## Features

- Mouse interactions: The player will use the mouse and the left mouse button to interact with the aim trainer.
- Countdown: A countdown of the time the user has left to play.
- Average time: An average time, in milliseconds, of the time between accurate clicks.
- Score: The score of the user.
- Local Highscores: The high scores recorded on a local machine.
- Main Menu: A main menu played before the main game, gives the user time and does not jump into the game immediately.
- Possibly User Settings: Possible settings for the user that can be adjusted, e.g. volume and mouse sensitivity.

## Challenges

The core gameplay will be the user clicking on an object which will spawn another object randomly somewhere else on the display. For this, I will need to be able to add mouse functionality and have a class object for the target.

What I am most worried about is implementing a main menu. This will be a separate scene that will act as a hub for user settings, quitting, and accessing the main game. I will need to do some research on how this will be possible. 

Another thing I need to be able to do is create a file that holds the high scores that the users have generated. These high scores will be displayed and stored so when the program is run again, these high scores will still be present on the local machine.

User settings seem like the most difficult to deal with. I have no idea how I will be able to change possible settings the changes volume and mouse sensitivity, I will need to do research for this.

## Outcomes

**Ideal Outcome:**

I want to be able to make a fully functional game. This means a main menu that is able to transition to the game, quit the game, display high scores, and provide user settings. I want to be able to store the high scores so that when the program is run again, they will be there as well. With the core gameplay loop, when the player clicks on the target, the player is rewarded points, a clock will start, and another target is spawned. When the player clicks on the new target the clock stops, this time is the amount of time that it took for the user to accurately click on the target after clicking a previous target.

**Minimal Viable Outcome:**

If my ideal outcome proves to be too much due to poor planning and over-scoping, a minimal viable outcome that I will achieve will be the core gameplay loop as well as the high scores. 

## Milestones

I Will have 3 weeks to complete this project. Each week I will set a goal that I want to achieve.

1. Implement core gameplay Add high scores
2. Make the main menu
3. Add adjustable user settings
