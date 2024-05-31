# dr. MARTHA
dr. (doctor) MARTHA stands for Modular AI for Robust Telemedicine and Health Analysis. It is an app that uses Computer Vision to identify key health issues and problems from the patient's photo of eyes, teeth, tongue, and face. It also recommends the treatment, medical procedure, and suggest professional doctors for further diagnosis.

![Dr_Martha (online-video-cutter com)](https://github.com/yohanesnuwara/dr_martha/assets/51282928/35e0a5d9-24e1-443f-badc-2e1f33c46d9e)

See our YouTube video of demo --> [LINK]()

## Eye health

|Normal|Blepharitis|Conjunctivitis|
|---|---|---|
|![normal-eye](https://github.com/yohanesnuwara/dr_martha/assets/51282928/a02ecbcf-ce4b-4c30-8642-d6607ffba0dd)|![blepharitis](https://github.com/yohanesnuwara/dr_martha/assets/51282928/cb4f498a-846b-44f6-b6be-4f25b25c67c0)|![conjunctivitis](https://github.com/yohanesnuwara/dr_martha/assets/51282928/63117643-a093-48fc-a17a-0d20698b1f51)|
| **Iridocyclitis** | **Keratitis** | **Cataract** |
|![iridocyclitis](https://github.com/yohanesnuwara/dr_martha/assets/51282928/9df25768-5b03-4b2b-b96f-62bcd723ac85)|![keratitis](https://github.com/yohanesnuwara/dr_martha/assets/51282928/6517e017-0c76-4d93-94d4-976d3322eebe)|![cataract](https://github.com/yohanesnuwara/dr_martha/assets/51282928/60ae29a0-88b7-44e4-8a23-bd548a4337d5)|

## Facial skin health

Multiple face problems: acne, acne scars, blackhead, whitehead, pimples, crystalline, cystic, milium, papular, purulent, and dermatitis

<img src="https://github.com/yohanesnuwara/dr_martha/assets/51282928/1a2538f6-bc46-419b-b170-13b39cce2cf3" width="400">

## Requirements
* Python==3.11.8
* Tensorflow==2.15.0
* Keras==2.15.0
* NLTK==3.8.1
* Flask==3.0.3

## How to run the app in VS Code (Desktop version)

In your PC:

1. Download this repository as [ZIP file](https://github.com/yohanesnuwara/dr_martha/archive/refs/heads/main.zip)
2. Extract the ZIP file into preferred directory
3. Download the model weights from [this link](https://zenodo.org/api/records/11402284/files-archive)
4. Put the downloaded weights inside folder ```/flask_yolo_app/weights/```

In your VS Code:

4. Install the above requirements with ```pip install```
5. Open terminal and go to the directory ```cd flask_yolo_app```
6. Run the app ```python app.py```
7. Open the app in browser with URL localhost [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

> Note: dr. MARTHA has not been tested in any clinical trials. As a proof-of-concept application, it will need collaboration with medical doctors to check the accuracy of diagnosis and prescriptions for example.
