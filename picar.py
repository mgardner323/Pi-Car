#!/usr/bin/env python
from flask import Flask, render_template, request, jsonify, url_for, redirect# Import necessary modules
import RPi.GPIO as GPIO
import video_dir
import car_dir
import motor
from time import ctime

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'read cpu_temp', 'home', 'distance', 'x+', 'x-', 'y+', 'y-', 'xy_home']

video_dir.setup()
car_dir.setup()
motor.setup()     # Initialize the Raspberry Pi GPIO connected to the DC motor.
video_dir.home_x_y()
car_dir.home()

app = Flask(__name__)

# Load the main form template on webrequest for the root page
@app.route("/")
def main():
# Create a template data dictionary to send any data to the template
 templateData = {
        'title' : 'PiCam'
        }

# Pass the template data into the template index.html and return it to the user
 return render_template('index.html', **templateData)

# The function below is executed when someone requests a URL with a move camera direction
@app.route("/<direction>")
def move(direction):
    # Choose the direction of the request
    if direction == 'camleft':
        video_dir.move_decrease_x()
    elif direction == 'camright':
        video_dir.move_increase_x()
    elif direction == 'up':
        video_dir.move_increase_y()
    elif direction == 'down':
        video_dir.move_decrease_y()
    elif direction == 'camhome':
        video_dir.home_x_y()
    elif direction == 'forward':
        motor.forward()
    elif direction == 'reverse':
        motor.backward()
    elif direction == 'left':
        car_dir.turn_left()
    elif direction == 'right':
        car_dir.turn_right()
    elif direction == 'stop':
        motor.ctrl(0)
    elif direction == 'home':
        car_dir.home()
# The function below is executed when someone requests a URL with a move car direction

# # Function to manually set a motor to a specific pluse width
# @app.route("/<motor>/<pulsewidth>")
# def manual(motor,pulsewidth):
#     if motor == "pan":
#         servoPan.set_servo(23, int(pulsewidth))
#     elif motor == "tilt":
#         servoTilt.set_servo(22, int(pulsewidth))
#     return "Moved"

# Clean everything up when the app exits
# atexit.register(cleanup)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0') #so that can access it by any host IP
