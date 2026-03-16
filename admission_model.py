import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def admission_model():

    print("Admission model running...")

    data = pd.read_csv("admission_dataset.csv")

    X = data[['EntranceScore','Marks','Distance','Scholarship']]
    y = data['Joined']

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train,y_train)

    print("\nEnter Student Details")

    entrance = int(input("Entrance Exam Score: "))
    marks = int(input("School Marks: "))
    distance = int(input("Distance from School (km): "))
    scholarship = int(input("Scholarship (1=Yes, 0=No): "))

    result = model.predict([[entrance,marks,distance,scholarship]])

    if result[0] == 1:
        print("Prediction: Student will JOIN the school")
    else:
        print("Prediction: Student will NOT JOIN the school")