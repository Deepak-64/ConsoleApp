import re
import datetime
import mysql.connector
class Validate:
    def studentName(self,studName,regNO,dept,year,mailId,dob,batch,paswrd): 
        while 1:
            pattern=r"^[A-Z]+[A-Za-z]{4,29}$"
            if  not re.findall(pattern,studName):
                print("........INVALID STUDENT NAME..................")
                studName=input("Student Name\t\t\t:")
            else:
                break
        __flag__=True
        while 1:
            patternz=r'^[0-9]{7}$'
            if re.search(patternz,regNO):
                mydb= mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="Shiyam@17",
                                      auth_plugin="mysql_native_password",
                                      database="application")

                mycursor=mydb.cursor()
                mycursor.execute("SELECT Student_RollNo FROM Students_details")
                rollno=mycursor.fetchone()
                for row in rollno:
                    if regNO==row:
                        print("Student already registered................")
                        regNO=input("RegisterNO\t\t\t:")  
                        __flag__=False
                        break
                    else:
                        __flag__=True
                if __flag__==True:
                    break 
            else:
                print("........INVALID REGISTER NO..................")
                regNO=input("RegisterNO\t\t\t:")

        while 1:
            if dept=="Mech" or dept=="Civil" or dept=="Prod" or dept=="CS" or dept=="IT" or dept=="EEE" or dept=="EIE":
                    break
            else:
                print("........INVALID DEPARTMENT..................")
                dept=input("Department\t\t\t:")
        while 1:
            if year==1 or year==2 or year==3 or year==4:
                    break
            else:
                print("........INVALID YEAR..................")
                year=input("Year\t\t\t:")
        while 1:
            if re.match(r"^\S+@\S+\.\S+$",mailId):
                break
            else:
                print("........INVALID MAIL ID..................")
                mailId=input("EmailID\t\t\t:")
        while 1:
            try:
                date_format = '%Y-%m-%d'
                datetime.datetime.strptime(dob, date_format)
                break
            except ValueError:
                print("Incorrect data format, should be YYYY-MM-DD")
                dob=input("Date of birth\t\t:")
        mydb= mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="Shiyam@17",
                                      auth_plugin="mysql_native_password",
                                      database="application")

        mycursor=mydb.cursor()
        mycursor.execute("INSERT INTO students_details VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                         (studName,regNO,dept,year,mailId,dob,batch,paswrd))
        mydb.commit()