
# Create your views here.
from django.http import HttpResponse #
from django.shortcuts import render
import joblib
import pandas as pd
import xgboost
def index(request): #
    #'''
    html = '''
    <center>물보라를 일으켜 따따따따 따따따따따상</center>
    <br>
    <br>

    <center>
        <form action=/myapp/predict>
    경쟁률: <input type=text name='경쟁률'><br>
    공모가: <input type=text name='공모가'><br>
    종목명: <input type=text name='종목명'><br>
    <input type='submit' value='예측하기'>
    </form>
    </center>
    '''    
    return HttpResponse(html)
    #'''    
    '''
    return render(request, 'index.html', {})
    '''

def predict(request): #
    try:
        x1 = request.GET['경쟁률']
    except:
        x1 = '0'
    #x1 = int(x1)

    try:
        x2 = request.GET['공모가']
    except:
        x2 = '0'
    #x2 = int(x2)
    try:
        x3 = request.GET['종목명']
    except:
        x3 = ''

    #from sklearn.linear_model import LinearRegression

    #estimator = LinearRegression()


    estimator = joblib.load('C:/Users/inwook/Desktop/toy/myproject/xgb_model.model') 

    #x_test = [[0.13047393, 0.32338637],
    #          [0.83383158, 0.17852872]]
    #x_test = [[x1, x2]]
    x_test=pd.DataFrame([[x1, x2]])

    y_predict = estimator.predict(x_test) 

    return render(request, 'predict.html', {'y_predict':y_predict,'종목명':x3})    