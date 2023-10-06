# importing libraries
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
from sklearn import datasets,metrics
from sklearn.model_selection import KFold,cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler



#raed the csv dataset file
data_frame=pd.read_csv(r'NAVERIS\AiModel\dataset\atlantic.csv')

#Prediction Model
x=np.array(data_frame.drop(['ID','Name','Date','Time','Event','Status','Latitude','Longitude'],axis=1))
y=np.array(data_frame['Status'])

x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,test_size=0.2)

model=RandomForestClassifier(random_state=42)

train_model=model.fit(x_train,y_train)

#[[Maximum Wind ,  Minimum Pressure ,  Low Wind NE ,   Low Wind SE ,   Low Wind SW ,   Low Wind NW ,   Moderate Wind NE,  Moderate Wind SE,  Moderate Wind SW  , Moderate Wind NW  , High Wind NE    ,  High Wind SE ,      High Wind SW   ,   High Wind NW ]]

 
y=model.predict([[43,1008,0,0,0,0,0,0,0,0,0,0,0,0]])
y=y[0].replace(' ','')
if y=='TS':
    y='Tropical Storm'
elif y=='HU':
    y="Hurricane"
elif y=='TD':
    y="Tropical Depression"
elif y=='LO':
    y="Low"
elif y=='DB':
    y="Disturbance"
elif y=='SD':
    y="Subtropical Depression"
elif y=='SS':
    y="Subtropical Storm"
elif y=='WV':
    y="Tropical Wave"
elif y=='EX':
    y="Extratropical"

warning_disaster=y



