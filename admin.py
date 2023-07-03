import mysql.connector
from validate import Validate
import re

class Admin:

    @staticmethod
    def admin():
        print(">>>>>>>>>>>>>>>WELCOME ADMIN<<<<<<<<<<<<<<<<<<")
        ad_name=input("Enter Admin Name:")
        ad_pass=input("Enter Password:")
        flag=True
        mydb= mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="Shiyam@17",
                                      auth_plugin="mysql_native_password",
                                      database="application")

        mycursor=mydb.cursor()
        mycursor.execute("SELECT AdminName FROM admin")
        login=mycursor.fetchone()
        mycursor.execute("SELECT Password FROM admin")
        login_pass=mycursor.fetchone()

        for x in login:
            if x==ad_name:
                for y in login_pass:
                    if y==ad_pass:
                        print("\n--------------------------------Admin Login Successful----------------------------------")
                        while 1:
                            choice1=input("\n1.Register New Student\n2.Change password\n3.LogOut\nEnter your choice=")
                            if choice1=="1":
                                l.nameReg()
                            elif choice1=="2":
                                l.chanpass()
                            elif choice1=="3":
                                print("------------------------------------BACK  TO MAIN MENU----------------------------------------------\n")
                                flag=False
                                break
                            else:
                                print(".........INVALID CHOICE...............\n")
                    if flag==True:
                        print("\n..................Invalid Password...............")
                        flag=False
            if flag==True:
                print("\n...........................Invalid Username..................")

    #Student Registration
    @staticmethod       
    def nameReg():
        print("----------------------------------REGISTRATION-------------------------------")
        paswrd="1234"
        studName=input("Student Name\t\t\t:")
        regNO=input("RegisterNO\t\t\t:")
        dept=input("Department\t\t\t:")
        year=int(input("Year\t\t\t\t:"))
        mailId=input("EmailID\t\t\t\t:")
        dob=input("Date of birth(YY/MM/DD)\t\t:")
        batch=input("Batch(YYYY-YYYY)\t\t:")
        c=Validate()
        c.studentName(studName,regNO,dept,year,mailId,dob,batch,paswrd)

    #Admin Password Change
    @staticmethod
    def chanpass():
        fl=True
        mydb= mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="Shiyam@17",
                                      auth_plugin="mysql_native_password",
                                      database="application")

        mycursor=mydb.cursor()
        print("-----------------------CHANGE PASSWORD-------------------------")
        newPasswd=input("Enter your current password=")
        mycursor.execute("SELECT Password FROM admin")
        record=mycursor.fetchone()
        for x in record:
            if x==newPasswd:
                while 1:
                    nxtpasswd=input("Enter new password :")
                    nxt_passwd=input("Renter Password   :")
                    pattern=r"^[A-Z]+[A-Za-z]{6,29}$"
                    if nxtpasswd==nxt_passwd and re.search(pattern,nxtpasswd):
                        one=(nxt_passwd,)
                        two=("UPDATE admin SET Password=%s")
                        mycursor.execute(two,one)
                        mydb.commit()
                        mydb.close()
                        print("******************Password Changed Succesfully*******************")
                        fl=False
                        break
                    else:
                        print("---------------Password Doesnot Match/Incorret Form---------------------")
        if fl==True:
            print("-------------------------Incorrect Password----------------------")
            
c=Validate()
l=Admin()

