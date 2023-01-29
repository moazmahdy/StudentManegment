# استدعي كل شئ tkinter من مكتبة ال
#from _typeshed import Self
from tkinter import *
from tkinter import ttk
# (pymysql)استدعاء 
import pymysql
# student اسميه class انشئ 
class Student:
    #انشئ دالة تعمل تلقائيا (constractor)
    def __init__(self, root):  
        self.root = root
        #انشئ الابعاد و اتحكم في مكان ظهور الشاشة
        self.root.geometry('1400x700+60+40')
        #اكتب عنوان للبرنامج
        self.root.title('برنامج ادارة المدارس')
        #التحكم بلون الخلفيه(الconfigure لتغير خلفية البرنامج )
        self.root.configure(background="silver")
        #اضافة عنوان (master=مكان ظهوره)(option=خصائصه)
        titel = Label(self.root , 
        text='[نظام تسجيل الطلاب]',
        background='blue',
        font=('monospace',16,'bold'),
        foreground='white'
        )
        #امر الاظهار
        titel.pack(fill=X)
        #انشاء متغيرات
        self.id_stu=StringVar()
        self.name_stu=StringVar()
        self.email_stu=StringVar()
        self.phone_stu=StringVar()
        self.age_stu=StringVar()
        self.gender_stu=StringVar()
        self.address_stu=StringVar()
        self.delete_stu=StringVar()
        self.search_stu=StringVar()
        #انشاء frame1 
        # للطالب ع اليمين في الاعلي frame نعمل 
        Manage_frame = Frame(self.root , background='white')
        #مكان و امر الاظهار
        Manage_frame.place(x=1140,y=30,width=250,height=398)
        #frame1 عنوان ل
        titel1 = Label(Manage_frame, 
        text='[بيانات الطالب]',
        background='yellow',
        font=('monospace',16,'bold'),
        foreground='red'
        )
        #امر الاظهار
        titel1.pack()
        #(text 1)اضافة         
        stu_id = Label(Manage_frame,text='الرقم التسلسلي',background='white')
        stu_id.pack() 
        #اضافة مكان للمستخدم ليدخل فيه الرقم(ال bd لتفعيل تواجد حافة يمني وفي الاسفل)
        id_enter = Entry(Manage_frame,textvariable=self.id_stu,bd=2)
        id_enter.pack()
        #(text 2)اضافة         
        stu_name = Label(Manage_frame,text='اسم الطالب',background='white')
        stu_name.pack() 
        #اضافة مكان للمستخدم ليدخل فيه الاسم
        name_enter = Entry(Manage_frame,textvariable=self.name_stu,bd=2)
        name_enter.pack()
        #(text 3)اضافة         
        stu_email = Label(Manage_frame,text='البريد الاكتروني الطالب ',background='white')
        stu_email.pack() 
        #اضافة مكان للمستخدم ليدخل فيه الايميل
        email_enter = Entry(Manage_frame,textvariable=self.email_stu,bd=2)
        email_enter.pack()
        #(text 4)اضافة         
        stu_phonenumber = Label(Manage_frame,text='رقم هاتف الطالب',background='white')
        stu_phonenumber.pack() 
        #اضافة مكان للمستخدم ليدخل فيه رقم الهاتف
        phonenumber_enter = Entry(Manage_frame,textvariable=self.phone_stu,bd=2)
        phonenumber_enter.pack()
        #(text 5)اضافة         
        stu_age = Label(Manage_frame,text='عمر الطالب',background='white')
        stu_age.pack() 
        #اضافة مكان للمستخدم ليدخل فيه عمره
        age_enter = Entry(Manage_frame,textvariable=self.age_stu,bd=2)
        age_enter.pack()
        #(text 6)اضافة         
        stu_gender = Label(Manage_frame,text=' جنس الطالب',background='white')
        stu_gender.pack() 
        #اضافة اختايريين ليختار منهم
        gender_enter = ttk.Combobox(Manage_frame,textvariable=self.gender_stu)
        gender_enter['value']=('meal','female')
        gender_enter.pack()
        #(text 7)اضافة         
        stu_address = Label(Manage_frame,text='عنوان الطالب',background='white')
        stu_address.pack() 
        #اضافة مكان للمستخدم ليدخل فيه عمره
        address_enter = Entry(Manage_frame,textvariable=self.address_stu,bd=2)
        address_enter.pack()
        #(text 8)اضافة 
        stu_delete = Label(Manage_frame ,text='حذف الطالب',foreground='red' ,background='white')
        stu_delete.pack()
        #اضافة مكان للمستخدم ليدخل فيه الاسم المراد حذفه
        delete_enter = Entry(Manage_frame,textvariable=self.delete_stu,bd=2)
        delete_enter.pack()
        #انشاء frame2 
        # للازرار ع اليمين في الاسفل frame نعمل 
        button_frame = Frame(self.root ,background= 'white')
        #مكان و امر الاظهار
        button_frame.place(x=1140,y=435,width=250,height=250)
        #frame2 عنوان ل
        titel2 = Label(button_frame , 
        text='[لوحة التحكم]',
        background='yellow',
        font=('monospace',16,'bold'),
        foreground='red'
        )
        #امر الاظهار
        titel2.pack()
        #(button1)اضافة
        button_add = Button(button_frame ,text='اضافة طالب',background='#99A799',foreground='black',command=self.add_student)
        button_add.place(x=53,y=45,width=150,height=30)
        #(button2)اضافة
        button_delete = Button(button_frame ,text='احذف طالب',background='#99A799',foreground='black',command=self.delete)
        button_delete.place(x=53,y=80,width=150,height=30)
        #(button3)اضافة
        button_update = Button(button_frame ,text='تعديل',background='#99A799',foreground='black',command=self.updatee)
        button_update.place(x=53,y=115,width=150,height=30)
        #(button4)اضافة
        button_clear = Button(button_frame ,text='افراغ',background='#99A799',foreground='black')
        button_clear.place(x=53,y=150,width=150,height=30)
        #(button5)اضافة
        button_exite = Button(button_frame ,text='اغلاق البرنامج',background='#99A799',foreground='black')
        button_exite.place(x=53,y=185,width=150,height=30)
        #انشاء frame3
        # للبحث في الاعلي frame نعمل
        search_frame = Frame(self.root ,background= 'white')
        #مكان و امر الاظهار
        search_frame.place(x=10,y=30,width=1120,height=80)
        #frame3 عنوان ل
        titel3 = Label(search_frame , 
        text='[مربع البحث]',
        background='yellow',
        font=('monospace',16,'bold'),
        foreground='red'
        )
        #امر الاظهار
        titel3.pack()
        #(text1)اضافة
        stu_search=Label(search_frame,text='البحث عن طالب',background='white')
        stu_search.place(x=1020,y=40)
        #اضافة اختايارات ليختار منهم
        search_by = ttk.Combobox(search_frame)
        search_by['value']=('id','name','address')
        search_by.place(x=866,y=40)
        #اضافة مكان للمستخدم ليدخل فيه الاسم المراد البحث عنه
        search_enter = Entry(search_frame,textvariable=self.search_stu,bd=2)
        search_enter.place(x=726,y=40)
        #انشاء زر
        search_button =Button(search_frame,text='بحث',background='#99A799',foreground='black')
        search_button.place(x=615,y=40,width=100,height=20)
        #انشاء frame4
        #لعرض النتائج  frame نعمل
        result_frame = Frame(self.root ,background= 'white')
        #مكان و امر الاظهار
        result_frame.place(x=10,y=115,width=1120,height=570)
        #frame4 عنوان ل
        titel4 = Label(result_frame , 
        text='[الطلاب]',
        background='yellow',
        font=('monospace',16,'bold'),
        foreground='red'
        )
        #امر الاظهار
        titel4.pack()
        # x للافقي scroolbar انشئ
        scroll_x=Scrollbar(result_frame , orient=HORIZONTAL) 
        # y للراسي scroolbar انشئ
        scroll_y=Scrollbar(result_frame , orient=VERTICAL)
        #(tkinter) ال الموجود في مكتبة(treeviwe) انشئ متغير استدعي به ال
        self.student_table=ttk.Treeview(result_frame,
        columns=('id','name','email','phone','age','gender','address'),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
        )
        self.student_table.place(x=18,y=1,width=1130,height=550)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        #لتتحرك الشاشة مع الشريط
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        #لاظهار العناوين
        self.student_table['show']='headings'
        self.student_table.heading('id',text='الرقم التسلسلي ')
        self.student_table.heading('name',text='اسم الطالب')
        self.student_table.heading('email',text='البريد الالكتروني')
        self.student_table.heading('phone',text='رقم هاتف الطالب')
        self.student_table.heading('age',text='عمر الطالب')
        self.student_table.heading('gender',text='جنس الطالب')
        self.student_table.heading('address',text='عنوان الطالب')
    
        #لتغيير الحجم
        self.student_table.column('address',width=80)
        self.student_table.column('gender',width=10)
        self.student_table.column('age',width=10)
        self.student_table.column('phone',width=15)
        self.student_table.column('email',width=60)
        self.student_table.column('name',width=60)
        self.student_table.column('id',width=10)
        self.student_table.bind("<ButtonRelease-1>",self.cursors)

        #الاتصال مع قاعدة البيانات واضافة البيانات
        #انشئ دالة للاضافة واضع فيها متغير
        #ادخل الاسم والباسوردو و اوصله بالسيرفر وقواعد البيانات pymysql انشئ متغيير من مكتبة ال
        self.fetch_all()# <==== امر جلب البيانات

    def add_student(self):
            con = pymysql.connect(host = 'localhost',user= 'root',password= '',database= 'stud')
            #للتعامل مع قواعد البيانات واجراء العمليات pymysql موجودة داخل مكتبة  curso دالة ال 
            cur = con.cursor()
            #لتنفيذ العمليات pymysql موجودة داخل مكتبة  execure دالة ال
            #string تعني استقبال %s
            cur.execute("insert into studentt values (%s,%s,%s,%s,%s,%s,%s)",(
                        #استدعي قيمة المتغيرات
                        #self.search_stu.get(),
                        self.id_stu.get(),
                        self.name_stu.get(),
                        self.email_stu.get(),
                        self.phone_stu.get(),
                        self.age_stu.get(),
                        self.gender_stu.get(),
                        self.address_stu.get()
                        
                             ))                                           
            #تنفيذ
            con.commit()
            #اعرض البيانات قبل غلق الاتصال مع قاعدة البيانات
            self.fetch_all()
            #اغلاق الاتصال بقاعدة البيانات
            con.close()
    #لجلب البيانات من قاعدة البيانات للواجهة
    def fetch_all(Self):
            #ادخل الاسم والباسوردو و اوصله بالسيرفر وقواعد البيانات pymysql انشئ متغيير من مكتبة ال
            con = pymysql.connect(host = 'localhost',user= 'root',password= '',database='stud')
            #اجراء العملية
            cur = con.cursor()
            cur.execute('select * from studentt')
            #تنفيذ عملية جلب الكل
            rowe = cur.fetchall()
            if len (rowe) != 0:
                Self.student_table.delete(*Self.student_table.get_children())
                for row in rowe:
                   #اجلب كل القيم في النهاية
                   Self.student_table.insert("",END,value=row)
                #تنفيذ
                con.commit()
            #اغلاق الاتصال بقاعدة البيانات
            con.close()
    

    #انشئ دالة للحذف واضع فيها متغير

    def delete(self):
            #ادخل الاسم والباسوردو و اوصله بالسيرفر وقواعد البيانات pymysql انشئ متغيير من مكتبة ال
            con = pymysql.connect(host = 'localhost',user= 'root',password= '',database='stud')
            #اجراء العملية
            cur = con.cursor()
            cur.execute('delete from studentt where name=%s',self.delete_stu.get())
            #تنفيذ
            con.commit()
            #احذف البيانات قبل غلق الاتصال مع قاعدة البيانات
            self.fetch_all()
            #اغلاق الاتصال بقاعدة البيانات
            con.close()

    #انشئ دالة للافراغ واضع فيها متغير
    def clear(self):
       #set = ضع
        self.id_stu.set('')
        self.name_stu.set('')
        self.email_stu.set('')
        self.phone_stu.set('')
        self.age_stu.set('')
        self.gender_stu.set('')
        self.address_stu.set('')

    #انشئ دالة لتحديد البيانات  
    def cursors(self,up):
        #تحديد البيانات من جدول الطلاب
        cursors_rows = self.student_table.focus()
        #اضع البيانات اللتي حددتها داخل متغير
        contents = self.student_table.item(cursors_rows) 
        #انشئ متغير للحصول علي القيم
        rowss = contents['values']
        self.id_stu.set(rowss[0])
        self.name_stu.set(rowss[1])
        self.email_stu.set(rowss[2])
        self.phone_stu.set(rowss[3])
        self.age_stu.set(rowss[4])
        self.gender_stu.set(rowss[5])
        self.address_stu.set(rowss[6])
    #انشئ دالة للتعديل
    def updatee(self):
            con = pymysql.connect(host = 'localhost',user= 'root',password= '',database= 'stud')
            #للتعامل مع قواعد البيانات واجراء العمليات pymysql موجودة داخل مكتبة  curso دالة ال 
            cur = con.cursor()
            #لتنفيذ العمليات pymysql موجودة داخل مكتبة  execure دالة ال
            #string تعني استقبال %s
            cur.execute("update studentt set id=%s , name=%s , email=%s , phone=%s , age=%s , gender=%s , address=%s",(
                                            #استدعي قيمة المتغيرات
                                            #self.search_stu.get(),
                                            self.id_stu.get(),
                                            self.name_stu.get(),
                                            self.email_stu.get(),
                                            self.phone_stu.get(),
                                            self.age_stu.get(),
                                            self.gender_stu.get(),
                                            self.address_stu.get()
                                            
                                                    ))                                           
            #تنفيذ
            con.commit()
            #اعرض البيانات قبل غلق الاتصال مع قاعدة البيانات
            self.fetch_all()
            #اغلاق الاتصال بقاعدة البيانات
            con.close()

#tkinterالموجود في مكتبة الclass استدعي به ال object انشئ
root = Tk()
#root اللي انشاتها واضعه داخل ال class  ستدعي به ال object انشئ
obj = Student(root)
#اعمل امر التشغيل وده هيكون اخر حاجه عشان تظهر عليه كل الاوامر اللي هكتبها
root.mainloop()