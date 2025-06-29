import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
#declare header files

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings # To suppress some warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('augmented_dataset1.csv') 
df.info()

df.head(10)

df['Level'].unique() 

df.describe().T

# Convert the "Level" column to string type first
df["Level"] = df["Level"].astype(str)

# Map cancer levels from Objective(str) to numeric values
mapping = {'High': 2, 'Medium': 1, 'Low': 0}
df["Level"].replace(mapping, inplace=True)

# Display the unique cancer levels after mapping
print(df['Level'].unique())

#check risk level
plt.figure(figsize=(10, 6))
explode = (0, 0, 0.15)
plt.pie(df['Level'].value_counts(), 
        labels=mapping.keys(), 
        explode=explode, autopct='%1.1f%%', 
        shadow=False, startangle=90, 
        colors=['#75ff33', '#fdff30', '#ff3333'],
        textprops={'fontsize': 18})
plt.title('Level Distribution')
plt.gca().set_facecolor('white')
plt.show()

def occ_cht(col, df=df):
    return df.groupby(col)['Level'].value_counts(normalize=True).unstack().plot(kind='bar', title = (f'Lungs Disease Based on {col}'), figsize=(12,5))

occ_cht('Age')

occ_cht('Gender')

occ_cht('Air Pollution')

occ_cht('Alcohol use')

occ_cht('OccuPational Hazards')

occ_cht('Genetic Risk')

occ_cht('Balanced Diet')

occ_cht('Obesity')

occ_cht('Smoking')

occ_cht('Passive Smoker')

occ_cht('Shortness of Breath')

occ_cht('Wheezing')

occ_cht('Frequent Cold')

#declaration of header files

from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, roc_curve, RocCurveDisplay
from sklearn.metrics import r2_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn import metrics

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier 
from sklearn.svm import SVC 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.tree import DecisionTreeClassifier

#declare independent variables in 'x' & dependent variable in 'y'

X = df.drop('Level', axis=1) 
y = df['Level']

#spliting 80% datas as train data(X_train, y_train) & 20% datas as test data(X_test, y_test)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f'Shape of Independent variables - X Training: {X_train.shape} and X Testing {X_test.shape}')
print(f'Shape of dependent variable - Y Training: {y_train.shape} and Y Testing {y_test.shape}')

print(f'\nTraining output counts\n{y_train.value_counts()}')
print(f'\nTesting output counts\n{y_test.value_counts()}')

#Data preprocesing 
scaler = StandardScaler()
X_train_stdscr = scaler.fit_transform(X_train)
X_test_stdscr = scaler.transform(X_test)

# Model Accuracies
mdl_accuracies = dict()
# Convert the target variable 'y' to integers

models = { 

    "Logistic Regression": (LogisticRegression(), { 
        'C': [0.01, 0.1, 1, 10], 
        'solver': ['lbfgs', 'liblinear'] 
    }), 

    "kNN":  (KNeighborsClassifier(), { 
        'n_neighbors': [3, 5, 7, 9], 
        'weights': ['uniform', 'distance'], 
        'metric': ['euclidean', 'manhattan'] 
    }), 

    
    "SVM": (SVC(probability=True), { 
        'C': [0.1, 1, 10], 
        'kernel': ['linear', 'rbf'], 
        'gamma': ['scale', 'auto'] 
    }),

     "Decision Tree": (DecisionTreeClassifier(), { 
        'max_depth': [None, 10, 20, 30], 
        'min_samples_split': [2, 5, 10] 
    }), 

    "Random Forest": (RandomForestClassifier(), { 
        'n_estimators': [100, 200, 300], 
        'max_depth': [None, 10, 20, 30], 
        'min_samples_split': [2, 5, 10] 
    }), 

 
     "XGBoost":(XGBClassifier(use_label_encoder=False, eval_metric='logloss'), { 
        'n_estimators': [100, 200, 300], 
        'learning_rate': [0.01, 0.1, 0.2], 
        'max_depth': [3, 6, 9] 
    })
}

#Function to evaluate the model
def evaluate_model_1(name, model, param_grid, X_train, X_test, y_train, y_test): 
    mdl = model.fit(X_train, y_train)
    y_pred  = mdl.predict(X_test)
    y_prob = mdl.predict_proba(X_test)[:, 1]
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred,  average='micro')
    f1 = f1_score(y_test, y_pred, average='micro')
    recall = recall_score(y_test, y_pred, average='micro')
    
    roc_scr = roc_auc_score(y_test, mdl.predict_proba(X_test), multi_class='ovr')
    fpr, tpr, thresholds = roc_curve(y_test, y_prob, pos_label=2)
    auc = metrics.auc(fpr, tpr)
    r2 = r2_score(y_test, y_pred)
    
    mdl_accuracies[name] = accuracy_score(y_test, y_pred)

    print(f"\nModel Name : {name}\n")
    print(f"\t Accuracy : {accuracy}\t ROC_AUC_Score : {roc_scr}\t AUC: {auc}\t  R2_Score : {r2}\n")
    print(f"\t Precision : {precision}\t F1 Score : {f1}\t Recall: {recall}\n")

    
    print(classification_report(y_test, y_pred))
    
    disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred))
    disp.plot()
    plt.show()
    print("__________________________________________________________________")


for name, (model, param_grid) in models.items(): 
    evaluate_model_1(name, model, param_grid, X_train, X_test, y_train, y_test)

