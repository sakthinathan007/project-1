import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def performance_model():

    print("Performance prediction running...")

    # Load dataset
    data = pd.read_csv("student_performance.csv")

    # Create Result column automatically (PASS if avg >= 50)
    data["Result"] = ((data["Internal_Marks"] + data["Assignment_Marks"]) / 2 >= 50).astype(int)

    # Features and target
    X = data[['Attendance','Internal_Marks','Assignment_Marks']]
    y = data['Result']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    print("\nEnter Student Details")

    attendance = int(input("Attendance (%): "))
    internal = int(input("Internal Marks: "))
    assignment = int(input("Assignment Marks: "))

    sample = pd.DataFrame(
        [[attendance, internal, assignment]],
        columns=['Attendance','Internal_Marks','Assignment_Marks']
    )

    prediction = model.predict(sample)

    if prediction[0] == 1:
        print("Prediction: Student will PASS")
    else:
        print("Prediction: Student will FAIL")