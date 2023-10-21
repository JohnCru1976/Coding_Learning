# Breakout Game #

## General Data ##
- Author: Juan Cru
- Mail: juanbcru@hotmail.com
- Start Date: 2023-10-21
- Platform: Android
- Resolution: 480x720
- Engine: Godot with GDScript
## Introducction ##
This project is a breakout type game. It consist in 10 simple levels where the player must break the tiles on the upper part of the screen.
## General mechanics ##
- One player
- Player is a horizontal stick that try to catch a ball
- The ball bounces and brake a tale if exists collision
- Tale dissapear when is touched by a ball
- The level finish when every tale has disappeared
- There are 10 leves with many tiles distributed by the upper part of the scenario
## Things I should take into account ##
- How design ir order to add more features in the future **(IMPORTANT)**:
	- Dropping boosters or limiters
	- Letting transform player **(ANIMATIONS)**
	- Multiball
	- etc
- How distribute the tiles in every scenerio
	- As first idea I've thougth in a matrix that will let instantiate the tiles under a determinated parameters: type, color, etc
		- I could create a method that generate it
	- It could be at random too, but it doesn't permits a progressive difficulty	 
## Planning ##
- Design a draft with the game components 
- Create assests
	- Player asset
	- Tile asset
		- Can I modify color, shape, etc., from the code?
	- Ball asset
	- Backgrounds
- Create componentes
## Game components ##