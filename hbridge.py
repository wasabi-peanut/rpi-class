from gpiozero import PWMOutputDevice, DigitalOutputDevice
from time import sleep

#///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_DRIVE_LEFT = 14             # ENA - H-Bridge enable pin
FORWARD_LEFT_PIN = 15   # IN1 - Forward Drive
REVERSE_LEFT_PIN = 18   # IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_DRIVE_RIGHT = 25            # ENB - H-Bridge enable pin
FORWARD_RIGHT_PIN = 8   # IN1 - Forward Drive
REVERSE_RIGHT_PIN = 7   # IN2 - Reverse Drive

# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)

# Initialise objects for H-Bridge digital GPIO pins
forwardLeft = DigitalOutputDevice(FORWARD_LEFT_PIN)
reverseLeft = DigitalOutputDevice(REVERSE_LEFT_PIN)
forwardRight = DigitalOutputDevice(FORWARD_RIGHT_PIN)
reverseRight = DigitalOutputDevice(REVERSE_RIGHT_PIN)

forwardLeft.value = 1.0
reverseLeft.value = 0
forwardRight.value = 1.0
reverseLeft.value = 0
