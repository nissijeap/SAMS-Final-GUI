# Face Recognition Attendance System

The objective of this project is to process live video-stream of students entering their classroom and generate the list of students attending the class. The system is coded in Python using OpenCv , Tkinter and MySQL.

### Installation

## Python

- Download Python from https://www.python.org/downloads/

## MySQL

- Download MySQL from https://dev.mysql.com/downloads/installer/


## Required steps

- Clone the repo:
```$ git clone https://github.com/guptaishika128/Face_Recognition_Attendance_System.git```

**Then you need to connect to database.** 
- To do that install MySQL with **username = root** and **password = 538810** and port 3306 (By default)

- Now open MySQL Workbench and click on default connection
![1 MySQL](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/d392f2ef-34bf-424c-b4e9-49e40b268ad3)

- Enter password stated above in the window
![2 MySQL access](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/fd008c74-cabc-4909-8b67-2aa96a5496a5)

- Now create two schemas one with name **face_recognizer** 
![6 db schema1](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/ea5fcb75-b483-446b-b4fd-352474fb2984)

- Other schema with name **mydata**
![7 db schema2](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/ab3e5d93-132d-42f2-a37d-39a1e9620ff8)

- Now as shown below click on Data Import
![3 data import](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/e4a4a63a-52d6-44bb-ac94-8a80857c86b9)

- Clicking on Import from Dump Project Folder find the location where you cloned this project under that click on **Database** folder 
![4 db import](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/145efca7-ef7e-42de-a5cd-754cd4b33800)

- You will see two files select both and click on Start Import
![5 db folder locate](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/f9f654be-9d6e-4f6d-9d28-4468c3e4ab59)

- **You have connected**. Refreshing you will be able to see student and register sql files under schemas
![8 db connection](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/126cbe7f-cba9-49a4-9934-3ca48a331005)

- Now run **login.py** 


## ⚙️ HOW THE SYSTEM WORKS?

This system works accordingly with a series of step explained below:

1. **LOGIN PAGE**:

First the admin will login using either default credentials **username=user@123** and **password=user@123** or can create a new account.
![login](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/0d96bb52-ef79-45d3-a010-3ac2d174899b)

2. After entering right credentials welcome message appears.
![welcome message](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/f5e07e37-8441-4c2d-a687-b229b69705bf)

3. Now the main page of face recognition attendance system appears
![main](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/59b37645-1526-478a-a467-7c22fa9e6275)

4. First Clicking on **Student Details** opens the page to register students and see their details. Students must have unique ID 
![student details](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/e4119f75-278f-418a-b741-9a6d841c075b)

5. After saving details click on Take Image option to capture student's face . 100 samples will be taken.
![trained photos](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/9ee75fad-f3f1-4449-b27a-9d3d21f0d792)

6. Next on the main page click on **Train Image** after that cick on Train Data to train samples for detection and recognition.
![train dataset](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/45dfe361-9d6e-4a7c-b844-1d6632c12788)

7. Now click on **Take Attendance** to recognize face . If the computer recognizes the face details are shown otherwise 'Unknown Image' message is shown
![take attendance](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/8812e0b7-a0ff-4fd3-94df-ebf926e96dfe)

8. Simultaneously, a csv file **attendance.csv** will be updated with the ID,Roll No, Name of the student ,Department, Date and Time at which his/her face was recognized.
![attendance csv](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/30e987fe-bd14-4a43-90ce-0b7c1cfdf942)

9. On the main page click on **Attendance Report** and then import attendance.csv to view attendance report of students. Attendance can also be exported .
![attendance report](https://github.com/nissijeap/SAMS-Final-GUI/assets/115227551/11b0770c-995f-4eda-a547-724c00a8fb17)


## Built With

* [OpenCV](http://docs.opencv.org/3.1.0/) - Implementation of Algorithms
* [Tkinter](https://docs.python.org/2/library/tkinter.html) - GUI Implementation
* [MySQL](https://docs.oracle.com/en-us/iaas/mysql-database/doc/getting-started.html) - Database
* [HAAR-CASCADE CLASSIFIER](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
* [LocalBinaryPatternHistogram (LBPH) recognizer](https://docs.opencv.org/master/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html)
* [PIL](https://pillow.readthedocs.io/en/stable/)


**Following functionalities can be performed: <br>**
• Login <br>
• New User Account can also be created. <br>
• If forgotten the login credentials password can be changed <br>
• Register new students to the system. Students can be filtered by Name or Department<br>
• Take photo sample of them <br>
• Train the model <br>
• Take attendance by scanning face <br>
• View attendance report of all students by importing csv. Also attendance can be exported too. <br>

