from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector


class ConnectorDB:

    def __init__(self, root):
        self.root = root
        titlespace = " "
        self.root.title(202 * titlespace + "Title")
        self.root.geometry("1360x700+300+0")
        self.root.resizable(width = False, height = False)

        MainFrame = Frame(self.root, bd=10, width=1360, height=700, relief=RIDGE, bg='cadet blue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=1360, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=1360, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=1360, height=400, padx=2, bg='cadet blue', relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=1360, height=180, padx=12, pady=9, relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        RightFrame1 = Frame(TopFrame3, bd=5, width=176, height=400, padx=2, bg='cadet blue', relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=150, height=500, padx=2, pady=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)

#======================================================================================================================

        Purchase_Order_ID =StringVar()
        Date =StringVar()
        Customer_ID =StringVar()
        Bill_to_Name =StringVar()
        Bill_to_Company_Name =StringVar()
        Bill_to_Address =StringVar()
        Bill_to_Phone =StringVar()
        Ship_to_Name =StringVar()
        Ship_to_Company_Name =StringVar()
        Ship_to_Address =StringVar()
        Ship_to_Phone =StringVar()
        Requisitioner =StringVar()
        Ship_Via =StringVar()
        FOB =StringVar()
        Shipping_Terms =StringVar()
        Item_NO =StringVar()
        Description =StringVar()
        Unit_Price =StringVar()
        Qty =StringVar()
        Item_Total =StringVar()

#======================================================================================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Title", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            self.entOrderID.delete(0, END)
            self.entDate.delete(0, END)
            self.entCustID.delete(0, END)
            self.entBillToName.delete(0, END)
            self.entBillToCompany.delete(0, END)
            self.entBillToAddress.delete(0, END)
            self.entBillToPhone.delete(0, END)
            self.entShipToName.delete(0, END)
            self.entShipToCompany.delete(0, END)
            self.entShipToAddress.delete(0, END)
            self.entShipToPhone.delete(0, END)
            self.entRequisitioner.delete(0, END)
            self.entVia.delete(0, END)
            FOB.set("")
            self.entTerms.delete(0, END)
            self.entItemNO.delete(0, END)
            self.entItemDesc.delete(0, END)
            self.entPrice.delete(0, END)
            self.entQty.delete(0, END)
            self.entTotal.delete(0, END)

        def addData():
            if Purchase_Order_ID.get() =="" or Date.get() =="" or Customer_ID.get() =="":
                tkinter.messagebox.showerror("MySQL Connection", "Enter Correct Details")
            else:
                sqlCon = mysql.connector.connect(host="localhost", user="root", password="PassOfYourMYSQL", database="NamOfDB")
                cur = sqlCon.cursor()
                cur.execute("insert into final values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                Purchase_Order_ID.get(),
                Date.get(),
                Customer_ID.get(),
                Bill_to_Name.get(),
                Bill_to_Company_Name.get(),
                Bill_to_Address.get(),
                Bill_to_Phone.get(),
                Ship_to_Name.get(),
                Ship_to_Company_Name.get(),
                Ship_to_Address.get(),
                Ship_to_Phone.get(),
                Requisitioner.get(),
                Ship_Via.get(),
                FOB.get(),
                Shipping_Terms.get(),
                Item_NO.get(),
                Description.get(),
                Unit_Price.get(),
                Qty.get(),
                Item_Total.get()

                ))
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("MySQL Connection", "Record Entered Successfuly")

        def displayData():
            sqlCon = mysql.connector.connect(host="localhost", user="root", password="PassOfYourMYSQL", database="NameOfDB")
            cur = sqlCon.cursor()
            cur.execute("select * from final")
            result = cur.fetchall()
            if len(result) !=0:
                self.Order_Records.delete(*self.Order_Records.get_children())
                for row in result:
                    self.Order_Records.insert('', END, values=row)
                sqlCon.commit()
            sqlCon.close()

        def RecordInfo(ev):
            viewinfo = self.Order_Records.focus()
            learnerData = self.Order_Records.item(viewinfo)
            row = learnerData['values']
            Purchase_Order_ID.set(row[0])
            Date.set(row[1])
            Customer_ID.set(row[2])
            Bill_to_Name.set(row[3])
            Bill_to_Company_Name.set(row[4])
            Bill_to_Address.set(row[5])
            Bill_to_Phone.set(row[6])
            Ship_to_Name.set(row[7])
            Ship_to_Company_Name.set(row[8])
            Ship_to_Address.set(row[9])
            Ship_to_Phone.set(row[10])
            Requisitioner.set(row[11])
            Ship_Via.set(row[12])
            FOB.set(row[13])
            Shipping_Terms.set(row[14])
            Item_NO.set(row[15])
            Description.set(row[16])
            Unit_Price.set(row[17])
            Qty.set(row[18])
            Item_Total.set(row[19])


        def deleteDB():
            sqlCon = mysql.connector.connect(host="localhost", user="root", password="PassOfYourMYSQL", database="NameOfDB")
            cur = sqlCon.cursor()
            cur.execute("delete from final where Purchase_Order_ID='%s'"%Purchase_Order_ID.get())
                
            sqlCon.commit()
            displayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Deleted Successfuly")
            Reset()

        def searchDB():
            try:
                sqlCon = mysql.connector.connect(host="localhost", user="root", password="PassOfYourMYSQL", database="NameOfDB")
                cur = sqlCon.cursor()
                cur.execute("select * from final where Purchase_Order_ID='%s'" %Purchase_Order_ID.get())

                row = cur.fetchone()

                Purchase_Order_ID.set(row[0])
                Date.set(row[1])
                Customer_ID.set(row[2])
                Bill_to_Name.set(row[3])
                Bill_to_Company_Name.set(row[4])
                Bill_to_Address.set(row[5])
                Bill_to_Phone.set(row[6])
                Ship_to_Name.set(row[7])
                Ship_to_Company_Name.set(row[8])
                Ship_to_Address.set(row[9])
                Ship_to_Phone.set(row[10])
                Requisitioner.set(row[11])
                Ship_Via.set(row[12])
                FOB.set(row[13])
                Shipping_Terms.set(row[14])
                Item_NO.set(row[15])
                Description.set(row[16])
                Unit_Price.set(row[17])
                Qty.set(row[18])
                Item_Total.set(row[19])
                    
                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Data Entry Form", "No Such Record Found")
                Reset()
            sqlCon.close()
            
            

#======================================================================================================================

        self.lbltitle=Label(TitleFrame, font=('arial', 40, 'bold'), text="SamSan Data Base",bd=7)
        self.lbltitle.grid(row=0,column=0, padx=10)

        self.lblOrderID = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Purchase Order ID", bd=7)
        self.lblOrderID.grid(row=1, column=0, sticky=W, padx=10)
        self.entOrderID = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                                textvariable=Purchase_Order_ID)
        self.entOrderID.grid(row=1, column=1, sticky=W, padx=5)

        self.lblDate = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Date", bd=7)
        self.lblDate.grid(row=1, column=3, sticky=W, padx=5)
        self.entDate = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                             textvariable=Date)
        self.entDate.grid(row=1, column=4, sticky=W, padx=5)

        self.lblCustID = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Customer ID", bd=7)
        self.lblCustID.grid(row=1, column=5, sticky=W, padx=5)
        self.entCustID = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                               textvariable=Customer_ID)
        self.entCustID.grid(row=1, column=6, sticky=W, padx=5)

        self.lblBillToName = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Bill To", bd=7)
        self.lblBillToName.grid(row=2, column=0, sticky=W, padx=5)
        self.entBillToName = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                                   textvariable=Bill_to_Name)
        self.entBillToName.grid(row=2, column=1, sticky=W, padx=5)

        self.lblBillToCompany = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Bill To Company Name", bd=7)
        self.lblBillToCompany.grid(row=2, column=3, sticky=W, padx=5)
        self.entBillToCompany = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                                      textvariable=Bill_to_Company_Name)
        self.entBillToCompany.grid(row=2, column=4, sticky=W, padx=5)

        self.lblBillToAddress = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Bill To Address", bd=7)
        self.lblBillToAddress.grid(row=2, column=5, sticky=W, padx=5)
        self.entBillToAddress = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                                      textvariable=Bill_to_Address)
        self.entBillToAddress.grid(row=2, column=6, sticky=W, padx=5)

        self.lblBillToPhone = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Bill Phone Number", bd=7)
        self.lblBillToPhone.grid(row=3, column=0, sticky=W, padx=5)
        self.entBillToPhone = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                                    textvariable=Bill_to_Phone)
        self.entBillToPhone.grid(row=3, column=1, sticky=W, padx=5)

        self.lblShipToName = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Ship To", bd=7)
        self.lblShipToName.grid(row=3, column=3, sticky=W, padx=5)
        self.entShipToName = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                                   textvariable=Ship_to_Name)
        self.entShipToName.grid(row=3, column=4, sticky=W, padx=5)

        self.lblShipToCompany = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Ship To Company Name", bd=7)
        self.lblShipToCompany.grid(row=3, column=5, sticky=W, padx=5)
        self.entShipToCompany = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                                      textvariable=Ship_to_Company_Name)
        self.entShipToCompany.grid(row=3, column=6, sticky=W, padx=5)

        self.lblShipToAddress = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Ship To Address", bd=7)
        self.lblShipToAddress.grid(row=4, column=0, sticky=W, padx=5)
        self.entShipToAddress = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                                      textvariable=Ship_to_Address)
        self.entShipToAddress.grid(row=4, column=1, sticky=W, padx=5)

        self.lblShipToPhone = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Phone Number", bd=7)
        self.lblShipToPhone.grid(row=4, column=3, sticky=W, padx=5)
        self.entShipToPhone = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                                    textvariable=Ship_to_Phone)
        self.entShipToPhone.grid(row=4, column=4, sticky=W, padx=5)

        self.lblRequisitioner = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Requisitioner", bd=7)
        self.lblRequisitioner.grid(row=4, column=5, sticky=W, padx=5)
        self.entRequisitioner = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                                      textvariable=Requisitioner)
        self.entRequisitioner.grid(row=4, column=6, sticky=W, padx=5)

        self.lblVia = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Ship Via", bd=7)
        self.lblVia.grid(row=5, column=0, sticky=W, padx=5)
        self.entVia = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                            textvariable=Ship_Via)
        self.entVia.grid(row=5, column=1, sticky=W, padx=5)

        self.lblFOB = Label(LeftFrame1, font=('arial', 10, 'bold'), text="FOB", bd=7)
        self.lblFOB.grid(row=5, column=3, sticky=W, padx=5)
        self.cboFOB = ttk.Combobox(LeftFrame1, font=('arial', 10, 'bold'), width=23, state='readonly',
                                   textvariable=FOB)
        self.cboFOB['values'] = (
        '', 'Samsan Tech Luzon Branch', 'Samsan Tech Visayas Branch', 'Samsan Tech Mindanao Branch')
        self.cboFOB.current(0)
        self.cboFOB.grid(row=5, column=4)

        self.lblTerms = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Shipping Terms", bd=7)
        self.lblTerms.grid(row=5, column=5, sticky=W, padx=5)
        self.entTerms = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                              textvariable=Shipping_Terms)
        self.entTerms.grid(row=5, column=6, sticky=W, padx=5)

        self.lblItemNO = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Item Number", bd=7)
        self.lblItemNO.grid(row=6, column=0, sticky=W, padx=5)
        self.entItemNO = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                               textvariable=Item_NO)
        self.entItemNO.grid(row=6, column=1, sticky=W, padx=5)

        self.lblItemDesc = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Item Description", bd=7)
        self.lblItemDesc.grid(row=6, column=3, sticky=W, padx=5)
        self.entItemDesc = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                                 textvariable=Description)
        self.entItemDesc.grid(row=6, column=4, sticky=W, padx=5)

        self.lblPrice = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Unit Price", bd=7)
        self.lblPrice.grid(row=6, column=5, sticky=W, padx=5)
        self.entPrice = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                              textvariable=Unit_Price)
        self.entPrice.grid(row=6, column=6, sticky=W, padx=5)

        self.lblQty = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Quantity", bd=7)
        self.lblQty.grid(row=7, column=0, sticky=W, padx=5)
        self.entQty = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                            textvariable=Qty)
        self.entQty.grid(row=7, column=1, sticky=W, padx=5)

        self.lblTotal = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Item Total", bd=7)
        self.lblTotal.grid(row=7, column=3, sticky=W, padx=5)
        self.entTotal = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=5, width=25, justify='left',
                              textvariable=Item_Total)
        self.entTotal.grid(row=7, column=4, sticky=W, padx=5)

#======================================================================================================================

        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)

        self.Order_Records = ttk.Treeview(LeftFrame, height=12, columns=("Purchase_Order_ID", "Date", "Customer_ID",
                                                                         "Bill_to_Name", "Bill_to_Company_Name",
                                                                         "Bill_to_Address", "Bill_to_Phone",
                                                                         "Ship_to_Name", "Ship_to_Company_Name",
                                                                         "Ship_to_Address", "Ship_to_Phone",
                                                                         "Requisitioner", "Ship_Via", "FOB",
                                                                         "Shipping_Terms", "Item_NO", "Description",
                                                                         "Unit_Price", "Qty", "Item_Total"),
                                          yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = Scrollbar(LeftFrame, orient=HORIZONTAL)

        self.Order_Records = ttk.Treeview(LeftFrame, height=12, columns=("Purchase_Order_ID", "Date", "Customer_ID",
                                                                         "Bill_to_Name", "Bill_to_Company_Name",
                                                                         "Bill_to_Address", "Bill_to_Phone",
                                                                         "Ship_to_Name", "Ship_to_Company_Name",
                                                                         "Ship_to_Address", "Ship_to_Phone",
                                                                         "Requisitioner", "Ship_Via", "FOB",
                                                                         "Shipping_Terms", "Item_NO", "Description",
                                                                         "Unit_Price", "Qty", "Item_Total"),
                                          xscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM, fill=X)

        self.Order_Records.heading("Purchase_Order_ID", text="OrderID")
        self.Order_Records.heading("Date", text="Date")
        self.Order_Records.heading("Customer_ID", text="CustID")
        self.Order_Records.heading("Bill_to_Name", text="Bill Name")
        self.Order_Records.heading("Bill_to_Company_Name", text="Bill Company")
        self.Order_Records.heading("Bill_to_Address", text="Bill Address")
        self.Order_Records.heading("Bill_to_Phone", text="Bill Phone")
        self.Order_Records.heading("Ship_to_Name", text="Ship Name")
        self.Order_Records.heading("Ship_to_Company_Name", text="Ship Company")
        self.Order_Records.heading("Ship_to_Address", text="Ship Address")
        self.Order_Records.heading("Ship_to_Phone", text="Ship Phone")
        self.Order_Records.heading("Requisitioner", text="Requisitioner")
        self.Order_Records.heading("Ship_Via", text="Via")
        self.Order_Records.heading("FOB", text="FOB")
        self.Order_Records.heading("Shipping_Terms", text="Terms")
        self.Order_Records.heading("Item_NO", text="ItemNO")
        self.Order_Records.heading("Description", text="Description")
        self.Order_Records.heading("Unit_Price", text="Price")
        self.Order_Records.heading("Qty", text="Qty")
        self.Order_Records.heading("Item_Total", text="Total")

        self.Order_Records['show'] = 'headings'

        self.Order_Records.column("Purchase_Order_ID", width=60)
        self.Order_Records.column("Date", width=40)
        self.Order_Records.column("Customer_ID", width=40)
        self.Order_Records.column("Bill_to_Name", width=60)
        self.Order_Records.column("Bill_to_Company_Name", width=60)
        self.Order_Records.column("Bill_to_Address", width=70)
        self.Order_Records.column("Bill_to_Phone", width=40)
        self.Order_Records.column("Ship_to_Name", width=60)
        self.Order_Records.column("Ship_to_Company_Name", width=60)
        self.Order_Records.column("Ship_to_Address", width=70)
        self.Order_Records.column("Ship_to_Phone", width=40)
        self.Order_Records.column("Requisitioner", width=60)
        self.Order_Records.column("Ship_Via", width=40)
        self.Order_Records.column("FOB", width=70)
        self.Order_Records.column("Shipping_Terms", width=40)
        self.Order_Records.column("Item_NO", width=40)
        self.Order_Records.column("Description", width=70)
        self.Order_Records.column("Unit_Price", width=40)
        self.Order_Records.column("Qty", width=25)
        self.Order_Records.column("Item_Total", width=60)
        

        self.Order_Records.pack(fill=BOTH, expand=1)
        self.Order_Records.bind("<ButtonRelease-1>",RecordInfo)
        #displayData()
        

#======================================================================================================================

        self.btnAddNew=Button(RightFrame1a, font=('arial', 16, 'bold'), text="Add New", bd=4, pady=1, padx=20,
                                                  width =8, height=2, command=addData).grid(row=0, column=0, padx=1)

        self.btnDisplay=Button(RightFrame1a, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=20,
                                                  width =8, height=2, command=displayData).grid(row=1, column=0, padx=1)


        self.btnDelete=Button(RightFrame1a, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=20,
                                                  width =8, height=2, command=deleteDB).grid(row=3, column=0, padx=1)

        self.btnSearch=Button(RightFrame1a, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=20,
                                                  width =8, height=2, command=searchDB).grid(row=4, column=0, padx=1)

        self.btnReset=Button(RightFrame1a, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=20,
                                                  width =8, height=2, command=Reset).grid(row=5, column=0, padx=1)

        self.btnExit=Button(RightFrame1a, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=20,
                                                  width =8, height=2, command=iExit).grid(row=6, column=0, padx=1)

#======================================================================================================================


if __name__=='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
