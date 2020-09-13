from tkinter import *
import math,random
from tkinter import messagebox
import os
class Bill_app:
    def __init__(self,root):
        self.root=root
        self.root.title("Billing softwere")
        self.root.geometry("1350x700+0+0")
        bg_color="#00FF7F"
        title=Label(self.root,text="Billing software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)



        #====== variables ========\
        #======fruits =========
        self.mango=IntVar()
        self.apple=IntVar()
        self.banana=IntVar()
        self.lychee=IntVar()
        self.orange=IntVar()
        self.coconut=IntVar()
        
        #====== flower ===========
        self.rose=IntVar()
        self.lotus=IntVar()
        self.sunflower=IntVar()
        self.lily=IntVar()
        self.jasmine=IntVar()
        self.dhalia=IntVar()

        #====== vegetables ==========
        self.cabbage=IntVar()
        self.carrot=IntVar()
        self.tomato=IntVar()
        self.pea=IntVar()
        self.green_bean=IntVar()
        self.broccoli=IntVar()

        #===== total product price & tax variables =====
        self.fruit_price=StringVar()
        self.flower_price=StringVar()
        self.vegetale_price=StringVar()

        
        self.fruti_tax=StringVar()
        self.flower_tax=StringVar()
        self.vegetable_tex=StringVar()


        #======== customer =========
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()


        #==== customer detail frame =====

        f1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",18,"bold"),fg="red",bg=bg_color)
        f1.place(x=0,y=80,relwidth=1)
        cname_lb1=Label(f1,text="Customer Name",bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=0,padx=0,pady=5)
        cname_txt=Entry(f1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lb1=Label(f1,text="Phone No.",bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=2,padx=0,pady=5)
        cphn_txt=Entry(f1,width=15,font="arial 15",textvariable=self.c_phone,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        cbill_lb1=Label(f1,text="Bill Number",bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=4,padx=0,pady=5)
        cbill_txt=Entry(f1,width=15,font="arial 15",bd=7,textvariable=self.search_bill,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)


        bill_btn=Button(f1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=7,padx=15,pady=10)


        #=====  Fruits Trees =======
        f2=LabelFrame(self.root,text="Fruits Tree",bd=10,relief=GROOVE,font=("times new roman",18,"bold"),fg="red",bg=bg_color)
        f2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(f2,text="Mango(120/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(f2,width=7,font=("times new roman",16,"bold"),bd=5,textvariable=self.mango,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky="w")

        face_lbl=Label(f2,text="Banana(100/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_txt=Entry(f2,width=7,font=("times new roman",16,"bold"),bd=5,textvariable=self.banana,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky="w")

        face_w_lbl=Label(f2,text="Apple(210/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(f2,width=7,font=("times new roman",16,"bold"),bd=5,textvariable=self.apple,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky="w")

        hair_s_lbl=Label(f2,text="Lychee(180/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        bath_s_txt=Entry(f2,width=7,font=("times new roman",16,"bold"),bd=5,textvariable=self.lychee,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky="w")

        hair_g_lbl=Label(f2,text="Orange(140/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(f2,width=7,font=("times new roman",16,"bold"),bd=5,textvariable=self.orange,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky="w")
        
        body_lbl=Label(f2,text="Coconut(180/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(f2,width=7,font=("times new roman",16,"bold"),bd=5,textvariable=self.coconut,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky="w")


        #=====  Flower Trees =======
        f3=LabelFrame(self.root,text="Flower Trees",bd=10,relief=GROOVE,font=("times new roman",18,"bold"),fg="red",bg=bg_color)
        f3.place(x=340,y=180,width=325,height=380)

        bath_lbl=Label(f3,text="Rose(250/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(f3,width=7,font=("times new roman",16,"bold"),bd=5,textvariable=self.rose,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky="w")

        face_lbl=Label(f3,text="Lotus(210/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_txt=Entry(f3,width=7,font=("times new roman",16,"bold"),textvariable=self.lotus,bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky="w")

        face_w_lbl=Label(f3,text="Sunflower(220/ps)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(f3,width=7,font=("times new roman",16,"bold"),bd=5,textvariable=self.sunflower,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky="w")

        hair_s_lbl=Label(f3,text="Lily(150/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        bath_s_txt=Entry(f3,width=7,font=("times new roman",16,"bold"),textvariable=self.lily,bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky="w")

        hair_g_lbl=Label(f3,text="Jasmine(180/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(f3,width=7,font=("times new roman",16,"bold"),bd=5,textvariable=self.jasmine,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky="w")
        
        body_lbl=Label(f3,text="Dhalia(120/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(f3,width=7,font=("times new roman",16,"bold"),bd=5,textvariable=self.dhalia,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky="w")

        #=====  Vegetable Trees =======
        f4=LabelFrame(self.root,text="Vegetable Trees",bd=10,relief=GROOVE,font=("times new roman",18,"bold"),fg="red",bg=bg_color)
        f4.place(x=675,y=180,width=325,height=380)

        bath_lbl=Label(f4,text="cabbage(80/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(f4,width=7,font=("times new roman",16,"bold"),bd=5,textvariable=self.cabbage,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky="w")

        face_lbl=Label(f4,text="Tomato(60/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_txt=Entry(f4,width=7,font=("times new roman",16,"bold"),bd=5,textvariable=self.tomato,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky="w")

        face_w_lbl=Label(f4,text="Carrot(80/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(f4,width=7,font=("times new roman",16,"bold"),bd=5,textvariable=self.carrot,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky="w")

        hair_s_lbl=Label(f4,text="Green bean(50/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        bath_s_txt=Entry(f4,width=7,font=("times new roman",16,"bold"),textvariable=self.green_bean,bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky="w")

        hair_g_lbl=Label(f4,text="broccoli(40/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(f4,width=7,font=("times new roman",16,"bold"),textvariable=self.broccoli,bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky="w")
        
        body_lbl=Label(f4,text="Pea(40/pis)",font=("times new roman",15,"bold"),bg=bg_color,fg="sienna").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(f4,width=7,font=("times new roman",16,"bold"),textvariable=self.pea,bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky="w")


        #==== Bill Area====
        f5=Frame(self.root,bd=10,relief=GROOVE)
        f5.place(x=1000,y=180,width=350,height=380)
        bill_title=Label(f5,text="Bill Aera",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(f5,orient=VERTICAL)
        self.textarea=Text(f5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)



        #=== Button frame ====
        f6=LabelFrame(self.root,text="Bill Area",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="red",bg=bg_color)
        f6.place(x=0,y=560,relwidth=1,height=140)


        m1_lbl=Label(f6,text="Total Fruit Price",bg=bg_color,fg="sienna",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(f6,width=18,font="arial 10 bold",bd=7,textvariable=self.fruit_price,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2_lbl=Label(f6,text="Total Flower Price",bg=bg_color,fg="sienna",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(f6,width=18,font="arial 10 bold",textvariable=self.flower_price,bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        
        m3_lbl=Label(f6,text="Total Vegetable Price",bg=bg_color,fg="sienna",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(f6,width=18,font="arial 10 bold",bd=7,textvariable=self.vegetale_price,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
    

        c1_lbl=Label(f6,text="Total Fruit Tax(5%)",bg=bg_color,fg="sienna",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(f6,width=18,font="arial 10 bold",textvariable=self.fruti_tax,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2_lbl=Label(f6,text="Total Flower Tax(10%)",bg=bg_color,fg="sienna",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(f6,width=18,font="arial 10 bold",textvariable=self.flower_tax,bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
        
        c3_lbl=Label(f6,text="Total Vegetable Tax(8%)",bg=bg_color,fg="sienna",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(f6,width=18,font="arial 10 bold",textvariable=self.vegetable_tex,bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
    

        btn_f=Frame(f6,bd=7,relief=GROOVE)
        btn_f.place(x=800,width=530,height=105)

        total_btn=Button(btn_f,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,bd=2,width=11,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
        Bill_btn=Button(btn_f,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,bd=2,width=11,font="arial 12 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="clear",command=self.clear_data,bg="cadetblue",fg="white",pady=15,bd=2,width=11,font="arial 12 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_f,text="Exit",command=self.exit_app,bg="cadetblue",fg="white",pady=15,bd=2,width=11,font="arial 12 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()


    def total(self):
        self.c_mango_p=self.mango.get()*120
        self.c_fc_p=self.banana.get()*100
        self.c_fw_p=self.apple.get()*210
        self.c_s_p=self.lychee.get()*180
        self.c_g_p=self.orange.get()*140
        self.c_l_p=self.coconut.get()*180


        self.total_fruit_price=(float
                                        (self.c_mango_p)+
                                        (self.c_fc_p)+
                                        (self.c_fw_p)+
                                        (self.c_s_p)+
                                        (self.c_g_p)+
                                        (self.c_l_p)
                                        )

        self.fruit_price.set("Rs. "+str(self.total_fruit_price))
        self.c_tax=round((self.total_fruit_price*0.05),2)
        self.fruti_tax.set("Rs. "+str(self.c_tax))



        self.g_r_p=self.rose.get()*250
        self.g_f_p=self.lotus.get()*210
        self.g_d_p=self.sunflower.get()*220
        self.g_w_p=self.lily.get()*150
        self.g_s_p=self.jasmine.get()*180
        self.g_t_p=self.dhalia.get()*120



        self.total_flower_price=(float
                                        (self.g_r_p)+
                                        (self.g_f_p)+
                                        (self.g_d_p)+
                                        (self.g_w_p)+
                                        (self.g_s_p)+
                                        (self.g_t_p)
                                        )

        self.flower_price.set("Rs. "+str(self.total_flower_price))
        self.g_tax=round((self.total_flower_price*0.1),2)
        self.flower_tax.set("Rs. "+str(self.g_tax))


        self.cd_m_p=self.cabbage.get()*80
        self.cd_c_p=self.carrot.get()*60
        self.cd_f_p=self.tomato.get()*80
        self.cd_t_p=self.pea.get()*50
        self.cd_l_p=self.green_bean.get()*40
        self.cd_s_p=self.broccoli.get()*40
        
        self.total_vegetable_price=(float
                                        (self.cd_m_p)+
                                        (self.cd_c_p)+
                                        (self.cd_f_p)+
                                        (self.cd_t_p)+
                                        (self.cd_l_p)+
                                        (self.cd_s_p)
                                        )

        self.vegetale_price.set("Rs. "+str(self.total_vegetable_price))
        self.cd_tax=round((self.total_vegetable_price*0.08),2)
        self.vegetable_tex.set("Rs. "+str(self.cd_tax))


        self.Total_bill=float(  self.total_fruit_price+
                                self.total_flower_price+
                                self.total_vegetable_price+
                                self.c_tax+
                                self.g_tax+
                                self.cd_tax
                            )
            
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome to Mycode")
        self.textarea.insert(END,f"\nBill Number : {self.bill_no.get()}")
        self.textarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\nPhone number : {self.c_phone.get()}")
        self.textarea.insert(END,f"\n======================================")
        self.textarea.insert(END,f"\nProducts\t\t QTY\t\t Price")
        self.textarea.insert(END,f"\n======================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customter Detail are must")
        elif self.fruit_price.get()=="Rs. 0.0" and self.flower_price.get()=="Rs. 0.0" and self.vegetale_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No product selectd Please Choose any")
        else:

            self.welcome_bill()
            #==== fruits ========
            if self.mango.get()!=0:
                self.textarea.insert(END,f"\n Mango\t\t{self.mango.get()}\t\t{self.c_mango_p}")
            if self.banana.get()!=0:
                self.textarea.insert(END,f"\n Banana\t\t{self.banana.get()}\t\t{self.c_fc_p}")
            if self.apple.get()!=0:
                self.textarea.insert(END,f"\n Apple\t\t{self.apple.get()}\t\t{self.c_fw_p}")
            if self.lychee.get()!=0:
                self.textarea.insert(END,f"\n lychee\t\t{self.lychee.get()}\t\t{self.c_s_p}")
            if self.orange.get()!=0:
                self.textarea.insert(END,f"\n Orange\t\t{self.orange.get()}\t\t{self.c_g_p}")
            if self.coconut.get()!=0:
                self.textarea.insert(END,f"\n Cocon\t\t{self.coconut.get()}\t\t{self.c_l_p}")   


            #==== flower ========
            if self.rose.get()!=0:
                self.textarea.insert(END,f"\n Rice \t\t{self.rose.get()}\t\t{self.g_r_p}")
            if self.lotus.get()!=0:
                self.textarea.insert(END,f"\n Food Oil\t\t{self.lotus.get()}\t\t{self.g_f_p}")
            if self.sunflower.get()!=0:
                self.textarea.insert(END,f"\n Daal\t\t{self.sunflower.get()}\t\t{self.g_d_p}")
            if self.lily.get()!=0:
                self.textarea.insert(END,f"\n Wheat\t\t{self.lily.get()}\t\t{self.g_w_p}")
            if self.jasmine.get()!=0:
                self.textarea.insert(END,f"\n Suger\t\t{self.jasmine.get()}\t\t{self.g_s_p}")
            if self.dhalia.get()!=0:
                self.textarea.insert(END,f"\n Tea\t\t{self.dhalia.get()}\t\t{self.g_t_p}") 



            #==== vegetables ========
            if self.cabbage.get()!=0:
                self.textarea.insert(END,f"\n cabbage\t\t{self.cabbage.get()}\t\t{self.cd_m_p}")
            if self.carrot.get()!=0:
                self.textarea.insert(END,f"\n Cock\t\t{self.carrot.get()}\t\t{self.cd_c_p}")
            if self.tomato.get()!=0:
                self.textarea.insert(END,f"\n tomato\t\t{self.tomato.get()}\t\t{self.cd_f_p}")
            if self.pea.get()!=0:
                self.textarea.insert(END,f"\n Thumbs Up\t\t{self.pea.get()}\t\t{self.cd_t_p}")
            if self.green_bean.get()!=0:
                self.textarea.insert(END,f"\n Limca\t\t{self.green_bean.get()}\t\t{self.cd_l_p}")
            if self.broccoli.get()!=0:
                self.textarea.insert(END,f"\n broccoli\t\t{self.broccoli.get()}\t\t{self.cd_s_p}") 
            
            self.textarea.insert(END,f"\n-------------------------------------")
            if self.fruti_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\ncosmatic Tax\t\t\t{self.fruti_tax.get()}")
            if self.flower_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\ncosmatic Tax\t\t\t{self.flower_tax.get()}")
            if self.vegetable_tex.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\ncosmatic Tax\t\t\t{self.vegetable_tex.get()}")

            self.textarea.insert(END,f"\nTotal Bill\t\t\tRs. {str(self.Total_bill)}")

            
            self.textarea.insert(END,f"\n-------------------------------------")
            self.save_bill()
        
    def save_bill(self):
        op=messagebox.askyesno("save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("bill_d/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no :{self.bill_no.get()} Saved sucessfully")
        else:
            return
        
    def find_bill(self):
        present="no"
        for i in os.listdir("bill_d/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bill_d/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill no")


    def clear_data(self):

        op=messagebox.askyesno("Exit","Do you really want to claer data?")
        if op>0:
                    #======cosmatics =========
            self.mango.set(0)
            self.apple.set(0)
            self.banana.set(0)
            self.lychee.set(0)
            self.orange.set(0)
            self.coconut.set(0)
            
            #====== grocery ===========
            self.rose.set(0)
            self.lotus.set(0)
            self.sunflower.set(0)
            self.lily.set(0)
            self.jasmine.set(0)
            self.dhalia.set(0)

            #====== cold drinks ==========
            self.cabbage.set(0)
            self.carrot.set(0)
            self.tomato.set(0)
            self.pea.set(0)
            self.green_bean.set(0)
            self.broccoli.set(0)

            #===== total product price & tax variables =====
            self.fruit_price.set("")
            self.flower_price.set("")
            self.vegetale_price.set("")

            
            self.fruti_tax.set("")
            self.flower_tax.set("")
            self.vegetable_tex.set("")


            #======== customer =========
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            
            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()


root=Tk()
obj=Bill_app(root)
root.mainloop()
