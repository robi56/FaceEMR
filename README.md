# FaceEMR
## Emotion Recognition from Facial Expression 

The project aims to train a model using tensorflow for facial emotion detection and used the trained model 
as predictor in android facial expression recogtion app.

The model is trained using  tensorflow python framework and used in java application. 
Basically tensorflow provides a c++ api, that can be used in android application. The trained model by python langauge can be integrated with android project 
after inclduing tensorflow c++ framework dependencies and using native interface the model can be loaded and called in java class. This is the whole thing 

The total work of this project is divided into two parts 
1) Devlop  a model in tensoflow using python langauge 
2) Devlop an android appication for facial expression recongtion 


### Part 1.  Facial Expression Recongition Model in Tensorflow 

In this work , I have used a simple Convolutional Neural Network Architecture to train a facial expression dataset.

**1. DataSet:** The dataset is collected from a challenge in kaggle . 
The challenge link https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/

The data consists of 48x48 pixel grayscale images of faces.The dataset contains facial expression  of seven categories (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral

**2. Model:** 
    In this work I have used the below CNN model 
    
      input_image->conv2d->pooling->conv2d->pooling->conv2d->pooling->dropout->softmax

**3. Result:** I have used 5000 iterations with batch size 100 and restore the model in protocal buffer file

### Part 2.  Facial Expression Recongition Application in Tensorflow

I have used Android Studio for this application. 

Integrating tensorflow dependency in android is really a tedious thing. the good news is that the latest news that android studio manages all dependencis related to tensorflow after adding the dependencies in build.gradle(Module:app) file 

```
dependencies {
    compile 'org.tensorflow:tensorflow-android:+' 
}

```
**1. Designing the UI Components** 
Home Screen 
![GitHub Logo](/images/home.png =500x700)

**2. Interacting with the Tensorflow Native Api**
The 'org.tensorflow.contrib.android.TensorFlowInferenceInterface' handles all necessary operation to interact with native api. See more details in https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/android

**3. Finalizing the work** 




