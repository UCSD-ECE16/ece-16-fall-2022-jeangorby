# Final Project

## Improvements

### Improvement 1: Decoupling Shooting and Moving
- Use a button to shoot instead of tracking through the accelerometer in order to decouple the two actions.
- Realize that its not quite decoupled just yet, often the shooting is very inconsistent despite getting the command correctly.

### Improvement 2: Smoother Movement
- Currently the movement is incredibly stiff. One needs to be exctly left or right in order to actually get movement.
- Instead of checking for absolute orientation, we check for whether the accelerometer steers closer to a certain direction using thresholding
- Could experiment with using other measurements like l2 norm to improve on it.

### Improvement 3: still need


### Feature 1: Pause/Unpause 
- Placing finger on photodetector will pause the game
- Jean Gorby will work on this

#### Updates:
- Pause feature is working after the player puts their finger on the photodetector. Unpausing is currently not working
- Pause screen is inconsistent, sometimes it shows up sometimes it doesnt.
- Currently while the game is paused, it seems like the enemies still move in the background or at least their movement is buffered so after unpausing they move more than they should
- Might need to work on some sort of debouncing.

### Feature 2: 

### Feature 3: 