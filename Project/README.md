# Final Project

## Improvements

### Improvement 1: Decoupling Shooting and Moving (Working 100%)
- Use a button to shoot instead of tracking through the accelerometer in order to decouple the two actions.
- This button press is updated more often than movement in order to ensure all button clicks are registered properly.

### Improvement 2: Smoother Movement (Working 100%)
- Currently the movement is incredibly stiff. One needs to be exctly left or right in order to actually get movement.
- Instead of checking for absolute orientation, we calculate the tilt degree using math.

### Improvement 3: Removed the Need for Keyboard (Working 100%)
- Straight out of the box, the player must start the game by clicking a button on their keyboard and if they want to quit the game they must hit escape
- We have implemented a way to play the entire game without using the keyboard at all as soon as all the python files are ran
- In order to start game, the player must click the shoot button
- To exit the game, the player must tilt their controller with the buttons facing opposite of them (currently proof of concept which works fine but can be changed)


### Feature 1: Pause/Unpause (Working 100%)
- Placing finger on photodetector will pause the game
- Placing finger on photodetector again wil unpause the game
- One can hit escape while paused if they want to exit the game

### Feature 2: Changing sensitivity (Working 100%, can add oled screen component)
- Using a second button, the player can change the sensitivity of the tilt
- Sens option 1 is what we feel is the best, most comfortable sens
- Sens option 2 is the most sensitive we can make it feel
- Sens option 3 is the least sensitive we can make it feel, the player has to tilt their controller almost 90 degrees to the direction they want to go
- sens = np.array([[-10, 60],[0,40],[-200,200]])

### Feature 3: 