import eventlet
import socketio
import flask
import numpy as np
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import cv2 as cv

# Initialize SocketIO server and Flask app
sio = socketio.Server()
app = flask.Flask(__name__)

# Define speed limit
speed_limit = 12

def preprocess_img(image):
    # Crop the image to focus on the area of interest
    image = image[50:140, :, :]
    # Convert to YUV color space
    image = cv.cvtColor(image, cv.COLOR_RGB2YUV)
    # Apply Gaussian Blur
    image = cv.GaussianBlur(image, (3, 3), 0)
    # Resize to the input shape of the model
    image = cv.resize(image, (200, 66))
    # Normalize pixel values
    image = image / 255.0
    return image

@sio.on('connect')
def connect(sid, environ):
    print('Client connected:', sid)
    send_control(0, 0)

def send_control(steering_angle, throttle):
    sio.emit('steer', data={
        'steering_angle': str(steering_angle),
        'throttle': str(throttle)
    })

@sio.on('telemetry')
def telemetry(sid, data):
    speed = float(data['speed'])
    img = Image.open(BytesIO(base64.b64decode(data['image'])))
    img = np.asarray(img)

    # Preprocess image for model input
    img = preprocess_img(img)
    img = np.array([img])
    
    # Predict steering angle
    steering_angle = float(model.predict(img)[0])
    throttle = 1.0 - speed / speed_limit
    print('Steering angle: {:.2f}, Throttle: {:.2f}, Speed: {:.2f}'.format(steering_angle, throttle, speed))

    send_control(steering_angle, throttle)

if __name__ == '__main__':
    model = load_model('car_model.h5')  # Load the model once
    app = socketio.Middleware(sio, app)  # Wrap app with middleware
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)  # Start server
