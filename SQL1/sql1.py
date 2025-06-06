# sql1.py
"""
Volume 1: SQL 1 (Introduction).
MTH420
06/02/2025
"""

import csv
import numpy as np
import sqlite3 as sql
from matplotlib import pyplot as plt

# Problems 1, 2, and 4
def student_db(db_file="students.db", student_info="student_info.csv",
                                      student_grades="student_grades.csv"):
    """Connect to the database db_file (or create it if it doesn’t exist).
    Drop the tables MajorInfo, CourseInfo, StudentInfo, and StudentGrades from
    the database (if they exist). Recreate the following (empty) tables in the
    database with the specified columns.

        - MajorInfo: MajorID (integers) and MajorName (strings).
        - CourseInfo: CourseID (integers) and CourseName (strings).
        - StudentInfo: StudentID (integers), StudentName (strings), and
            MajorID (integers).
        - StudentGrades: StudentID (integers), CourseID (integers), and
            Grade (strings).

    Next, populate the new tables with the following data and the data in
    the specified 'student_info' 'student_grades' files.

                MajorInfo                         CourseInfo
            MajorID | MajorName               CourseID | CourseName
            -------------------               ---------------------
                1   | Math                        1    | Calculus
                2   | Science                     2    | English
                3   | Writing                     3    | Pottery
                4   | Art                         4    | History

    Finally, in the StudentInfo table, replace values of −1 in the MajorID
    column with NULL values.

    Parameters:
        db_file (str): The name of the database file.
        student_info (str): The name of a csv file containing data for the
            StudentInfo table.
        student_grades (str): The name of a csv file containing data for the
            StudentGrades table.
    """
    conn = sql.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS MajorInfo")
    cursor.execute("DROP TABLE IF EXISTS CourseInfo")
    cursor.execute("DROP TABLE IF EXISTS StudentInfo")
    cursor.execute("DROP TABLE IF EXISTS StudentGrades")

    cursor.execute("""
    CREATE TABLE MajorInfo (
        MajorID INTEGER PRIMARY KEY,
        MajorName TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE CourseInfo (
        CourseID INTEGER PRIMARY KEY,
        CourseName TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE StudentInfo (
        StudentID INTEGER PRIMARY KEY,
        StudentName TEXT,
        MajorID INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE StudentGrades (
        StudentID INTEGER,
        CourseID INTEGER,
        Grade TEXT,
        PRIMARY KEY (StudentID, CourseID)
    )
    """)

    cursor.executemany("""
    INSERT INTO MajorInfo (MajorID, MajorName)
    VALUES (?, ?)
    """, [
        (1, 'Math'),
        (2, 'Science'),
        (3, 'Writing'),
        (4, 'Art')
    ])

    cursor.executemany("""
    INSERT INTO CourseInfo (CourseID, CourseName)
    VALUES (?, ?)
    """, [
        (1, 'Calculus'),
        (2, 'English'),
        (3, 'Pottery'),
        (4, 'History')
    ])

    with open(student_info, newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            student_id = int(row[0])
            student_name = row[1]
            major_id = int(row[2]) if row[2] != '-1' else None
            cursor.execute("""
            INSERT INTO StudentInfo (StudentID, StudentName, MajorID)
            VALUES (?, ?, ?)
            """, (student_id, student_name, major_id))

    with open(student_grades, newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            student_id = int(row[0])
            course_id = int(row[1])
            grade = row[2]
            cursor.execute("""
            INSERT INTO StudentGrades (StudentID, CourseID, Grade)
            VALUES (?, ?, ?)
            """, (student_id, course_id, grade))

    conn.commit()
    conn.close()


# Problems 3 and 4
def earthquakes_db(db_file="earthquakes.db", data_file="us_earthquakes.csv"):
    """Connect to the database db_file (or create it if it doesn’t exist).
    Drop the USEarthquakes table if it already exists, then create a new
    USEarthquakes table with schema
    (Year, Month, Day, Hour, Minute, Second, Latitude, Longitude, Magnitude).
    Populate the table with the data from 'data_file'.

    For the Minute, Hour, Second, and Day columns in the USEarthquakes table,
    change all zero values to NULL. These are values where the data originally
    was not provided.

    Parameters:
        db_file (str): The name of the database file.
        data_file (str): The name of a csv file containing data for the
            USEarthquakes table.
    """
    conn = sql.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS USEarthquakes")

    cursor.execute("""
    CREATE TABLE USEarthquakes (
        Year INTEGER,
        Month INTEGER,
        Day INTEGER,
        Hour INTEGER,
        Minute INTEGER,
        Second INTEGER,
        Latitude REAL,
        Longitude REAL,
        Magnitude REAL
    )
    """)
    
    with open(data_file, newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)

        for row in reader:
            year = int(row[0])
            month = int(row[1])
            day = int(row[2]) if int(row[2]) != 0 else None
            hour = int(row[3]) if int(row[3]) != 0 else None
            minute = int(row[4]) if int(row[4]) != 0 else None
            second = int(row[5]) if int(row[5]) != 0 else None
            latitude = float(row[6])
            longitude = float(row[7])
            magnitude = float(row[8])

            cursor.execute("""
            INSERT INTO USEarthquakes (
                Year, Month, Day, Hour, Minute, Second, Latitude, Longitude, Magnitude
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (year, month, day, hour, minute, second, latitude, longitude, magnitude))

    conn.commit()
    conn.close()


# Problem 5
def prob5(db_file="students.db"):
    """Query the database for all tuples of the form (StudentName, CourseName)
    where that student has an 'A' or 'A+'' grade in that course. Return the
    list of tuples.

    Parameters:
        db_file (str): the name of the database to connect to.

    Returns:
        (list): the complete result set for the query.
    """
    conn = sql.connect(db_file)
    cursor = conn.cursor()

    query = """
    SELECT StudentInfo.StudentName, CourseInfo.CourseName
    FROM StudentGrades
    JOIN StudentInfo ON StudentGrades.StudentID = StudentInfo.StudentID
    JOIN CourseInfo ON StudentGrades.CourseID = CourseInfo.CourseID
    WHERE StudentGrades.Grade IN ('A', 'A+')
    """

    cursor.execute(query)
    results = cursor.fetchall()

    conn.close()
    return results


# Problem 6
def prob6(db_file="earthquakes.db"):
    """Create a single figure with two subplots: a histogram of the magnitudes
    of the earthquakes from 1800-1900, and a histogram of the magnitudes of the
    earthquakes from 1900-2000. Also calculate and return the average magnitude
    of all of the earthquakes in the database.

    Parameters:
        db_file (str): the name of the database to connect to.

    Returns:
        (float): The average magnitude of all earthquakes in the database.
    """
    conn = sql.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("SELECT Magnitude FROM USEarthquakes WHERE Year >= 1800 AND Year < 1900")
    mags_1800s = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT Magnitude FROM USEarthquakes WHERE Year >= 1900 AND Year < 2000")
    mags_1900s = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT AVG(Magnitude) FROM USEarthquakes")
    avg_magnitude = cursor.fetchone()[0]

    conn.close()

    fig, axs = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

    axs[0].hist(mags_1800s, bins=20, color='skyblue', edgecolor='black')
    axs[0].set_title("Earthquake Magnitudes (1800–1900)")
    axs[0].set_xlabel("Magnitude")
    axs[0].set_ylabel("Frequency")

    axs[1].hist(mags_1900s, bins=20, color='lightgreen', edgecolor='black')
    axs[1].set_title("Earthquake Magnitudes (1900–2000)")
    axs[1].set_xlabel("Magnitude")

    plt.tight_layout()
    plt.show()

    return avg_magnitude
