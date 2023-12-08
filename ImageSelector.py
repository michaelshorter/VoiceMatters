import RPi.GPIO as GPIO
import os
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins connected to the switches
switch_pins = [6, 13, 19, 26]

# Set up the GPIO pins as inputs with internal pull-up resistors
for pin in switch_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variable to store the previous switch state and last switch state change time
prev_switch_state = None
last_state_change_time = time.time()

# Dictionary to store the image file associated with each switch state
switch_images = {
    (0, 1, 1, 1): "image.png",
    (1, 0, 1, 1): "haiku.png",
    (1, 1, 0, 1): "summary.png",
    (1, 1, 1, 0): "main_topics.png"
}

# Function to determine the position of the switch
def get_switch_position():
    position = [GPIO.input(pin) for pin in switch_pins]
    return tuple(position)

# Function to print the switch position and reload image if needed
def print_switch_position(position):
    global last_state_change_time

    if position in switch_images:
        print(f"Mode {switch_images[position]}")
        os.system(f"python3 dither-image-what.py --colour 'black' --image '{switch_images[position]}'")
        print(f"Mode {switch_images[position]} process completed")
    else:
        print("Unknown Position")

    # Update the last switch state change time
    last_state_change_time = time.time()

# Main program
if __name__ == "__main__":
    try:
        while True:
            # Get the current position of the switch
            switch_position = get_switch_position()

            # Check if the switch state has changed
            if switch_position != prev_switch_state:
                # Introduce a 1-second delay
                time.sleep(1)

                # Print the switch position and reload the image if needed
                print_switch_position(switch_position)

                # Update the previous switch state
                prev_switch_state = switch_position
            
            # Check if 1 minutes have passed since the last switch state change
            if time.time() - last_state_change_time >= 60:
                # Perform image reload for the current switch state
                if prev_switch_state in switch_images:
                    os.system(f"python3 dither-image-what.py --colour 'black' --image '{switch_images[prev_switch_state]}'")
                last_state_change_time = time.time()  # Reset the timer

    except KeyboardInterrupt:
        # Clean up GPIO on keyboard interrupt
        GPIO.cleanup()
