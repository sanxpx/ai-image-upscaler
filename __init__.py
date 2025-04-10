from flask import Flask, request, jsonify, send_file
import os
from PIL import Image
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "Real-ESRGAN Upscaler API Running"

@app.route('/upscale', methods=['POST'])
def upscale():
    scale = int(request.form.get('scale', 2))
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'No image uploaded'}), 400

    filename = str(uuid.uuid4()) + '.png'
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Dummy upscale logic (replace with Real-ESRGAN actual command in real deployment)
    img = Image.open(filepath)
    new_size = (img.width * scale, img.height * scale)
    upscaled = img.resize(new_size, Image.LANCZOS)
    result_path = os.path.join(RESULT_FOLDER, filename)
    upscaled.save(result_path)

    return send_file(result_path, mimetype='image/png')
