from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
from ultralytics import YOLO
import cv2
from doctor import dentist, suggest_medicine, diagnosis  # Import the dentist function
import csv

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Load YOLO models
teeth_model = YOLO('D:\\Tri Valley Hackathon\\flask_yolo_app\\weights\\yolo_teeth.pt')
tongue_model = YOLO('D:\\Tri Valley Hackathon\\flask_yolo_app\\weights\\yolo_tongue.pt')
eye_model = YOLO('D:\\Tri Valley Hackathon\\flask_yolo_app\\weights\\yolo_eye.pt')
face_model = YOLO('D:\\Tri Valley Hackathon\\flask_yolo_app\\weights\\yolo_face.pt')


# Load the medicine and doctor data
medicine_df = pd.read_csv('D:\\Tri Valley Hackathon\\flask_yolo_app\\data\\medicine.csv')
doctor_df = pd.read_csv('D:\\Tri Valley Hackathon\\flask_yolo_app\\data\\doctor.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'health_type' not in request.form:
        return redirect(request.url)

    file = request.files['file']
    health_type = request.form['health_type']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        if health_type == 'teeth':
            results = teeth_model.predict(filename)
            result_image_path = filename.replace('.jpg', '_result.jpg')
            result_image = results[0].plot()
            cv2.imwrite(result_image_path, result_image)
            detected_classes = [results[0].names[int(cls)] for cls in results[0].boxes.cls]
            output_sentence, treatment, need_dentist = dentist(detected_classes)
            return render_template('index.html', image=os.path.basename(result_image_path),
                                   output_sentence=output_sentence, treatment=treatment, need_dentist=need_dentist,
                                   detected_classes=detected_classes, health_type=health_type)

        elif health_type == 'tongue':
            results = tongue_model.predict(filename)
            result_image_path = filename.replace('.jpg', '_result.jpg')
            result_image = results[0].plot()
            cv2.imwrite(result_image_path, result_image)
            detected_classes = [results[0].names[int(cls)] for cls in results[0].boxes.cls]
            output_sentence = diagnosis(detected_classes)
            return render_template('index.html', image=os.path.basename(result_image_path),
                                   output_sentence=output_sentence,
                                   detected_classes=detected_classes, health_type=health_type)

        elif health_type == 'eye':
            results = eye_model.predict(filename)
            result_image_path = filename.replace('.jpg', '_result.jpg')
            result_image = results[0].plot()
            cv2.imwrite(result_image_path, result_image)
            detected_classes = [results[0].names[int(cls)] for cls in results[0].boxes.cls]
            output_sentence = diagnosis(detected_classes)
            return render_template('index.html', image=os.path.basename(result_image_path),
                                   output_sentence=output_sentence,
                                   detected_classes=detected_classes, health_type=health_type)
        
        elif health_type == 'face':
            results = face_model.predict(filename, classes=[0,1,2,4,5,6,7,8,9])
            result_image_path = filename.replace('.jpg', '_result.jpg')
            result_image = results[0].plot()
            cv2.imwrite(result_image_path, result_image)
            detected_classes = [results[0].names[int(cls)] for cls in results[0].boxes.cls]
            output_sentence = diagnosis(detected_classes)
            return render_template('index.html', image=os.path.basename(result_image_path),
                                   output_sentence=output_sentence,                                   
                                   detected_classes=detected_classes, health_type=health_type)        

        else:
            return "Invalid health type", 400

    return redirect(request.url)

@app.route('/medicine')
def medicine():
    detected_classes = request.args.get('detected_classes')
    if detected_classes:
        detected_classes = detected_classes.split(',')
        medicines = medicine_df[medicine_df['disease'].isin(detected_classes)].to_dict(orient='records')
    else:
        medicines = []

    if not medicines:
        return "No medicine found for the detected diseases."

    return render_template('medicine.html', medicines=medicines)

@app.route('/doctors')
def doctors():
    health_type = request.args.get('health_type')
    doctors = []
    with open('data/doctor.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Anatomy'].lower() == health_type.lower():
                doctors.append({
                    'Fullname': row['Fullname'],
                    'Degree': row['Degree'],
                    'Category': row['Category'],
                    'Hospital': row['Hospital'],
                    'Experience': row['Experience'],
                    'Expertise': row['Expertise'],
                    'Procedure': row['Procedure']
                })
    return render_template('doctor.html', doctors=doctors)

if __name__ == '__main__':
    app.run(debug=True)
