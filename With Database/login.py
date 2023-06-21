""""
Login Page 
Run this script to start the application


Default Credentials : ***** Username = user@123 *******
                      ***** Password = user@123 *******

"""


from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox       
import mysql.connector  
from main import Face_Recognition_System

def main():
    win=Tk()
    obj=login_window(win)
    win.mainloop()



class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1536x816+0+0") 
        #self.root.configure(bg="light blue")

        title_lbl = Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("poppins", 40, "bold"), bg="black",fg="yellow")
        title_lbl.pack(fill=X)
        
        # Background Image
        img_1=Image.open("Images//iit.png")
        img_1=img_1.resize((1536,800),Image.ANTIALIAS)
        self.lfimg=ImageTk.PhotoImage(img_1)

        f_lbl=Label(root,image=self.lfimg)
        f_lbl.place(x=0,y=55,width=1536,height=800)
        

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)


        img_1=Image.open("Images//12.png")
        img_1=img_1.resize((80,80),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img_1)

        lb1=Label(image=self.img1,bg="black",borderwidth=0)
        lb1.place(x=730,y=175,width=100,height=100)

        
        get_startLabel=Label(frame,text="Get Started", font=('poppins',20, 'bold'), background='black', foreground ='yellow')
        get_startLabel.place(x=95, y=100)

        # Labels for username, password

        username=Label(frame,text="Username", font=('poppins',15, 'bold'), background='black', foreground ='white')
        username.place(x=70, y=155)

        self.txtuser=Entry(frame,font=("poppins",15,"bold"))
        self.txtuser.place(x=40,y=185,width=270)

        password=Label(frame,text="Password", font=('poppins',15, 'bold'), background='black', foreground ='white')
        password.place(x=70, y=225)

        self.txtpass=Entry(frame,font=("poppins",15,"bold"))
        self.txtpass.place(x=40,y=255,width=270)


        #**********Icon Images for username & password*******
        img_11=Image.open("Images//11.png")
        img_11=img_11.resize((25,25),Image.ANTIALIAS)
        self.img11=ImageTk.PhotoImage(img_11)

        lblimg1=Label(image=self.img11,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)


        img_12=Image.open("Images//10.png")
        img_12=img_12.resize((25,25),Image.ANTIALIAS)
        self.img12=ImageTk.PhotoImage(img_12)

        lblimg2=Label(image=self.img12,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=395,width=25,height=25)

        # Login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("poppins",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="maroon",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # Register button
        registerbtn=Button(frame,text="New User Register",command=self.register_win,font=("poppins",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=85,y=350,width=160)

        # Forgot password button
        forgotpassbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("poppins",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=85,y=380,width=160)

    def register_win(self):
        self.new_window=Toplevel(self.root)
        self.obj=register_window(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required !",parent=self.root)
        elif self.txtuser.get()=="user@123" and self.txtpass.get()=="user@123":
            messagebox.showinfo("Success","Welcome to Face Recognition Attendance System",parent=self.root)
            self.new_window=Toplevel(self.root)
            self.obj=Face_Recognition_System(self.new_window)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="538810",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                       ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
            else:
                open_main=messagebox.showinfo("Success","Welcome to Face Recognition Attendance System!")
                self.new_window=Toplevel(self.root)
                self.obj=Face_Recognition_System(self.new_window)

            conn.commit()
            conn.close()   


    #**********************************Reset password******************************
    def reset_pass(self):
        if self.combo_security_Ques.get()=="Select":
            messagebox.showerror("Error","Select Security Quetion",parent=self.root2) 
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Plase enter Security answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root", password="538810", database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Ques.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct security answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset.",parent=self.root2)    
                self.root2.destroy()


    #*************************************** Forget password window********************************
    
    def forgot_password_window(self): 
        if self.txtuser.get()=="":
            messagebox.showerror("Error", "Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="538810", database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()                 
            
            # print(row)

            if row==None:
                messagebox.showerror("My Error", "Plaese enter a valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                fp=Label(self.root2, text="Forget Password", font=("poppins", 28, "bold"), fg="red", bg="white") 
                fp.place(x=0,y=10, relwidth=1)

                security_Ques=Label(self.root2, text="Select Security Question", font=("poppins", 15,"bold"), bg="white",fg="black")
                security_Ques.place(x=50, y=80)

                self.combo_security_Ques=ttk.Combobox (self.root2 ,font=("poppins", 15, "bold"), state="readonly")
                self.combo_security_Ques["values"]=("Select", "Your Birth Place", "Your Favorite Game", "Your Pet Name")
                self.combo_security_Ques.place(x=50,y=120,width=300)
                self.combo_security_Ques.current(0)


                security_A=Label(self.root2, text="Security Answer", font=("poppins", 15,"bold"), bg="white", fg="black") 
                security_A.place(x=50,y=160)

                self.txt_security=ttk.Entry(self.root2,font=("poppins", 15)) 
                self.txt_security.place(x=50,y=200,width=300)

                new_password=Label(self.root2, text="New Password", font=("poppins", 15,"bold"), bg="white", fg="black") 
                new_password.place(x=50,y=230)

                self.txt_new_password=ttk.Entry(self.root2,font=("poppins", 15)) 
                self.txt_new_password.place(x=50,y=270,width=300)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("poppins",15,"bold"),fg="white",bg="green")
                btn.place(x=150,y=320)



class register_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1536x816+0+0") 

        #**********variables********
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar() 
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        title_lbl = Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("poppins", 40, "bold"), bg="black", fg="yellow")
        title_lbl.pack(fill=X, pady=(0, 10))
        
        # Background Image
        img_1 = Image.open("Images//iit.png")
        img_1 = img_1.resize((1536,800), Image.ANTIALIAS)
        self.lfimg = ImageTk.PhotoImage(img_1)

        f_lbl = Label(root, image=self.lfimg)
        f_lbl.place(x=0, y=55, width=1536, height=800)

        img_1 = Image.open("Images//12.png")
        img_1 = img_1.resize((80,80), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(img_1)

        lb1 = Label(image=self.img1, bg="black", borderwidth=0)
        lb1.place(x=730, y=175, width=100, height=100)

        #**********Main frame**************
        frame = Frame(self.root, bg="black")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=800, height=550)
        
        img_1 = Image.open("Images//12.png")
        img_1 = img_1.resize((80,80), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(img_1)

        register_lbl = Label(frame, text="REGISTER USER", font=("poppins", 20, "bold"), bg="black", fg="yellow")
        register_lbl.place(relx=0.5, rely=0.1, anchor=CENTER)


        #************************Label and entry*******************
        #******For Row 1*********
        fname = Label(frame, text="First Name", font=("poppins", 15, "bold"), bg="black", fg="white") 
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("poppins", 15, "bold")) 
        self.fname_entry.place(x=50, y=130, width=300)

        l_name = Label(frame, text="Last Name", font=("poppins", 15, "bold"), bg="black", fg="white")
        l_name.place(x=450, y=100)
        
        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("poppins", 15, "bold"))
        self.txt_lname.place(x=450, y=130, width=300)

        #******For Row 2*********
        contact = Label(frame, text="Contact No", font=("poppins",15,"bold"), bg="black", fg="white") 
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("poppins",15, "bold"))
        self.txt_contact.place(x=50, y=200, width=300)

        email = Label(frame, text="Email", font=("poppins", 15, "bold"), bg="black", fg="white") 
        email.place(x=450, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("poppins", 15, "bold"))
        self.txt_email.place(x=450, y=200, width=300)

        #***********For Row 3*************
        security_Ques = Label(frame, text="Select Security Question", font=("poppins", 15, "bold"), bg="black", fg="white")
        security_Ques.place(x=50, y=240)

        self.combo_securiy_Ques = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("poppins", 15, "bold"), state="readonly")
        self.combo_securiy_Ques["values"] = ("Select", "Your Birth Place", "Your Favorite Game", "Your Pet Name")
        self.combo_securiy_Ques.place(x=50, y=270, width=300)
        self.combo_securiy_Ques.current(0)

        security_A = Label(frame, text="Security Answer", font=("poppins", 15, "bold"), bg="black", fg="white") 
        security_A.place(x=450, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_SecurityA, font=("poppins", 15)) 
        self.txt_security.place(x=450, y=270, width=300)

        #***********For Row 4*********
        passwd = Label(frame, text="Password", font=("poppins",15, "bold"), bg="black", fg="white") 
        passwd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("poppins", 15, "bold")) 
        self.txt_pswd.place(x=50, y=340, width=300)

        confirm_pswd = Label(frame, text="Confirm Password", font=("poppins", 15, "bold"), bg="black", fg="white")
        confirm_pswd.place(x=450, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("poppins", 15))
        self.txt_confirm_pswd.place(x=450, y=340, width=300)

        #**********For checkbutton********
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=("poppins", 12, "bold"), bg="black", fg="yellow", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        #**********For buttons***********
        # Register Button
        registerbtn = Button(frame, text="Register", command=self.register_data, font=("poppins", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="maroon", activeforeground="white", activebackground="red")
        registerbtn.place(relx=0.5, rely=0.8, anchor=CENTER, width=120, height=35)

        # Login Button
        loginbtn = Button(frame, text="Login Now", command=self.return_login, font=("poppins", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="red")
        loginbtn.place(relx=0.5, rely=0.9, anchor=CENTER, width=120, height=35)
        
        
        #***************For registering data *************

    def register_data(self):

            if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error", "All fields are required",parent=self.root) 
            elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error", "Password & confirm password must be sane",parent=self.root)
            elif self.var_check.get()==0:
                messagebox.showerror("Error","Plaese agree our term and conditions",parent=self.root)
            else: 
                conn=mysql.connector.connect(host="localhost",username="root",password="538810",database="mydata")
                my_cursor=conn.cursor()
                query=("select * from register where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist, please try another email",parent=self.root)
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                            self.var_fname.get(),
                                                                                            self.var_lname.get(),
                                                                                            self.var_contact.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_securityQ.get(),
                                                                                            self.var_SecurityA.get(),
                                                                                            self.var_pass.get()

                                                                                          )) 

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registered successfully",parent=self.root)

    #************Return to Login Page***************

    def return_login(self):
        self.root.destroy()



if __name__ == "__main__":
    main()  