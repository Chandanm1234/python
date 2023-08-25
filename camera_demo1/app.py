from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3
from werkzeug.utils import secure_filename
import cv2
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DATABASE'] = 'dresses.db'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def initialize_database():
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS dresses
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     color TEXT,
                     filename TEXT)''')
    conn.commit()
    conn.close()

def extract_dress_color(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define the range of colors for detecting dresses (for example, red color)
    lower_color = np.array([0, 100, 100])
    upper_color = np.array([10, 255, 255])
    
    mask = cv2.inRange(hsv_image, lower_color, upper_color)
    
    # Calculate the percentage of pixels matching the dress color
    dress_color_percentage = np.sum(mask == 255) / mask.size * 100
    
    return dress_color_percentage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    photo = request.files['photo']

    if photo and allowed_file(photo.filename):
        filename = secure_filename(photo.filename)
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        photo.save(photo_path)

        color_percentage = extract_dress_color(photo_path)

        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute('INSERT INTO dresses (color, filename) VALUES (?, ?)', (color_percentage, filename))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return 'Invalid file format'

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
