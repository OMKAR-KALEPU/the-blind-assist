# The Blind Assist: Currency Detection For the Visually Impaired
The "Currency Detection for the Visually Impaired" project aims to assist visually impaired individuals in identifying different banknotes accurately. The system leverages Convolutional Neural Networks (CNN) to recognize and classify various currencies in real-time through a live camera feed.

## How to Use the Currency Detection for the Visually Impaired App
- Firstly clone the repository. <br>
`git clone https://github.com/OMKAR-KALEPU/the-blind-assist.git`

- Download the [Dataset](https://www.kaggle.com/datasets/vishalmane109/indian-currency-note-images-dataset-2020).

- Rename the denomination folders to:
```
  1Hundrednote 
  2Hundrednote 
  2Thousandnote
  5Hundrednote 
  Fiftynote
  Tennote 
  Twentynote 
```

- Create a virtual environment. <br>
`python -m venv .venv`

- Activate the virtual environment. Open the terminal or command prompt and give the following command. <br>
`.venv\Scripts\Activate`

- Now that the virtual environment is activated, install the necessary libraries as specified in requirements.txt <br>
`pip install -r requirements.txt`

- You can create you own classifier by executing the [models](/models) <br>
  (OR) You can feel free to download the already trained DenseNet Classifier [here](https://drive.google.com/drive/folders/1zK5chPExxLR-qSp1TAu-uVd6TZXSg-l2?usp=sharing).

- Now you can start the django server. <br>
`python manage.py runserver`

- Now the project is live at
  ```
  http://127.0.0.1:8000/
  ```

- The user interface looks something like this: <br>
[interface](/media/interface/currency_detector.png) 
You can click on the User link in the navbar and register yourself and then you'll be able to predict your notes using live camera with voice output. <br>

## Note
- The path to the classifier should be changed accordingly in user/views.py file.
- The integrated web cam might not be able to detect the note properly if the quality of camera is not good. So I recommend using an external cam to be added to it.
  If external cam is added, the a line of code in user/views.py should be modified to:
  
  ```
  cv.videoCapture(1)
  ```

**Thank you :)**