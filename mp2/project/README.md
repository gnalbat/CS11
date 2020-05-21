# PhotoPy

PhotoPy is a simple application written in Python 3.7 that uses the Pyglet library to display a user interface and OpenCV to take pictures using a camera interface.

## Usage

Create a new virtual environment by following instructions located here https://docs.python.org/3/library/venv.html, run the virtualenv and install dependencies using `pip install -r requirements.txt`.

## Configuration

Settings for the app are located within a dictionary inside `config.py`.
There, you can change the video device to be used by changing `source` to the device id.
You can also change the template and create your own.
