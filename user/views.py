from django.shortcuts import render
from user.models import *
from django.contrib import messages
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import ResNet50
from keras.layers import Dense,Flatten,Dropout
from keras.models import Model,load_model
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
import pyttsx3
import cv2
import random



# Create your views here.
def userregister(request):
    return render(request, 'user/userregister.html')

def usersignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        city = request.POST.get('city')
        state = request.POST.get('state')
        Details = UserModel(username=username, email=email, password=password, mobile=mobile, city=city, state=state)
        Details.save()
    return render(request, 'user/userlogin.html') 

def userloginaction(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            Details = UserModel.objects.get(email=email, password=password)
            print(Details)
            return render(request, "user/userhome.html")
        except:
            messages.success(request, "user not registred")
            return render(request, "user/userlogin.html")
    return render(request, "user/userlogin.html")

def userhome(request):
    return render(request, 'user/userhome.html')

def userlogout(request):
    return render(request, 'user/userlogin.html')

from collections import Counter

def find_repeating(arr):
    counts = Counter(arr)
    most_repeating = max(counts, key=counts.get)

    return most_repeating

def userpredict(request):
    model=load_model('currency_classifier.h5',compile=False)
    # Initialize webcam
    cam = cv2.VideoCapture(0)
    # cv2.imshow("Test", img)
    for a in range(0, 50):
        ret, img=cam.read()
        # img = cv2.resize(img, (224,224))
        if ret:
            file='media\images\img' + str(a) + '.jpg'   
            cv2.imwrite(file, img)
            img1=img
            cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_LINEAR)
            print("Image" + str(a) + " saved")
    cam.release()
    cv2.destroyAllWindows()
    import os
    import random 
    path=os.path.join('media\images')
    files=os.listdir(path)
    
    predictions = []
    for img in files:
        test_image = os.path.join(path, img)
        test_image = image.load_img(test_image, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255
        test_image = np.expand_dims(test_image, axis=0)
        frame = model.predict(test_image)
        a = np.argmax(frame)
        predictions.append(a)

    print(predictions)
    a = find_repeating(predictions)
    print(a)

    if a==0:
        k='100'
        print("100")
    elif(a==1):
        k='200'
        print("200")
    elif(a==2):
        k='2000'
        print("2000")
    elif(a==3):
        k='500'
        print("500")
    elif(a==4):
        k='50'
        print("50")
    elif(a==5):
        k='10'
        print("10")
    elif(a==6):
        k='20'
        print("20")

    import pyttsx3
    text = ('You had',k,'Note')

    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    speak(text)
    return render(request, 'user/userhome.html')
