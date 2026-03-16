import pandas as pd
import random

def generate_timetable():

    print("Timetable generation running...")

    classes = ["10A","10B"]
    times = ["9:00-10:00","10:00-11:00","11:00-12:00"]

    subjects = ["Math","Science","English"]
    teachers = ["Mr Kumar","Ms Priya","Mr Raj"]

    rooms = ["101","102","103"]

    timetable = []

    for class_name in classes:
        for time in times:

            subject = random.choice(subjects)
            teacher = random.choice(teachers)
            room = random.choice(rooms)

            timetable.append({
                "Time": time,
                "Class": class_name,
                "Subject": subject,
                "Teacher": teacher,
                "Room": room
            })

    df = pd.DataFrame(timetable)

    print("\nGenerated Timetable\n")
    print(df)

    df.to_csv("generated_timetable.csv",index=False)