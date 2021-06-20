import sqlite3 as sq
from prettytable import PrettyTable
import random
import os
import time
import datetime
con=sq.connect("Bank1.db")
cas=con.cursor()
s='''CREATE table if not exists user(
user_id Integer primary key Autoincrement ,
u_name TEXT, 
u_fname TEXT,
u_dob TEXT,
u_mob TEXT,
u_accno TEXT,
Balance TEXT,
Ad_id Integer)'''
cas.execute(s)
a='''CREATE table if not exists admin(
admin_id Integer primary key Autoincrement,
ad_name TEXT,
ad_paswd TEXT)'''
cas.execute(a)
t='''CREATE table if not exists trans(
trans_id Integer primary key Autoincrement,
u_id Integer,
admin_id Integer,
Dt TEXT,
Balance TEXT,
Flag TEXT,
foreign key(u_id) references user(user_id)
foreign key(admin_id)references admin(admin_id))'''
cas.execute(t)
ins='''INSERT into admin(ad_name,ad_paswd)values('admin','admin')'''
ins1='''INSERT into admin(ad_name,ad_paswd)values('rashi','rashi')'''
cas.execute(ins)
cas.execute(ins1)
con.commit() 
# b="ALTER table trans add amount Integer"
# cas.execute(b)
##########################################################################################################
def ad_login():
	print("\t\t\t\t\t\tWELCOME TO ADMIN LOGIN MODULE  :) \n\n")
	name=input("Enter Name of admin: ")
	pswd=input("Enter Password: ")
	cas.execute("SELECT * from admin where ad_name=='"+name+"' and ad_paswd=='"+pswd+"'")
	record=cas.fetchall()
	if record==[]:
		print("Invalid username or password!!")
		time.sleep(3)
		os.system('cls')
		ad_login()
	else:
		a_id=record[0][0]
		print("\t\t\tCongrats ,You Login Sucessfully :)")
		time.sleep(3)
		os.system('cls')
		ad_menu(a_id)

def checkname(name):
	if(name==''or name.isspace()):
		return 0
	else:
		for a in name:
			if(a.isalpha() or a.isspace() or a=='.'):
				pass
			else:
				return 0
		return 1

def checkmob(mob):
	if(len(mob)==10):
		if mob.isdigit():
			return 1
		else:
			return 0
	else:
		return 0

def checkbal(balance):
	if balance==' ':
		return 0
	else:
		for a in balance:
			if(a.isdigit() or a=='.'):
				pass
			else:
				return 0
		return 1
def checkdob(dob):
	l=dob.split('/')
	if len(l)==3:
		try:
			datetime.datetime(int(l[2]),int(l[1]),int(l[0]))
			if(int(l[2])<=2020):
				return 1
			else:
				return 0
		except:
			return 0
	else:
		return 0

# def covamt(amt):
# 	from babel.numbers import format_currency
# 	d=format_currency(amt, 'INR', locale='en_IN')
# 	return d


def create_acc(a_id):
	print("\t\tENTER THE USER DATA WITH FULL CONCERNTRATION @:)")
	while True:
		name=input("Enter Name of customer: ")
		if checkname(name)==1:
			break
		else:
			print("You Enter Invalid Name!!")
	while True:
		f_name=input("Enter Father's name of customer: ")
		if checkname(f_name)==1:
			break
		else:
			print("You Enter Invalid Name!!")
	while True:
		dob=input("Enter Date of Birth(dd/mm/yyyy)")
		if checkdob(dob)==1:
			break
		else:
			print("You Enter Invalid DATE of Birth")
	while True:
		mob=input("Enter Mobile number of customer: ")
		if checkmob(mob)==1:
			break
		else:
			print("You Enter Invalid MOBILE NUMBER!!")
	while True:
		balance=input("Enter Minimum amount to account: ")
		if checkbal(balance)==1:
			break
		else:
			print("You Enter Invalid Amount!!")
	ifsc='SBIN'
	a=random.randrange(1000,9999)
	acc_no=ifsc+str(a)
	ins='''INSERT into user(u_name,u_fname,u_dob,u_mob,u_accno,Balance,Ad_id)values(?,?,?,?,?,?,?)'''
	t=(name,f_name,dob,mob,acc_no,balance,a_id)
	cas.execute (ins,t)
	con.commit()
	print("Your Data is recorded in Database Sucessfully :)")
	cas.execute("SELECT user_id from user where u_accno='"+acc_no+"'")
	record=cas.fetchall()
	if record==[]:
		print("Data is not recorded in database!!")
		time.sleep(5)
		os.system('cls')
		ad_menu(a_id)
	else:
		userid=record[0][0]
		x = datetime.datetime.now()
		dt=x.strftime("%d/%m/%y %H:%M:%S")
		ins1="INSERT into trans(u_id,admin_id,Dt,Balance,Flag)values(?,?,?,?,?)"
		u=(userid,a_id,dt,balance,'Inital')
		cas.execute(ins1,u)
		con.commit()
		time.sleep(5)
		os.system('cls')
		ad_menu(a_id)

def add_bal(a_id):
	print("\t\t $$$ USER WANTS TO DEPOSIT MONEY IN ACCOUNT $$$")
	nacc_no=input("Enter Your Account Number: ")
	cas.execute("SELECT * from user where u_accno=='"+nacc_no+"'")
	record=cas.fetchall()
	if record==[]:
		print("This Account Number Not Exist!!")
		time.sleep(5)
		os.system('cls')
		ad_menu(a_id)
	else:
		prv_amt=record[0][-2]
		upd="UPDATE user set Balance=? where u_accno=?"
		amt=input("Enter Amount: ")
		while True:
			if checkbal(amt)==1:
				break
			else:
				print("You Enter Invalid Amount!!")
		total_balance=float(prv_amt)+float(amt)
		u1=(total_balance,nacc_no)
		cas.execute(upd,u1)
		con.commit()
		userid=record[0][0]
		x = datetime.datetime.now()
		dt=x.strftime("%d/%m/%y %H:%M:%S")
		print("Money is Credited in your account:)")
		ins="INSERT into trans(u_id,admin_id,Dt,amount,Balance,Flag)values(?,?,?,?,?,?)"
		t=(userid,a_id,dt,amt,total_balance,'Credit')
		cas.execute(ins,t)
		con.commit()
		print("Your Available Balance is: ",total_balance)
		time.sleep(5)
		os.system('cls')
		ad_menu(a_id)


def withdraw_bal(a_id):
	print("\t\t $$$ USER WANTS TO WITHDRAWAL MONEY FROM ACCOUNT $$$")
	nacc_no=input("Enter Your Account Number: ")
	cas.execute("SELECT * from user where u_accno=='"+nacc_no+"'")
	record=cas.fetchall()
	if record==[]:
		print("This Account Number Not Exist!!")
		time.sleep(5)
		os.system('cls')
		ad_menu(a_id)
	else:
		prv_amt=record[0][-2]
		upd="UPDATE user set Balance=? where u_accno=?"
		amt=input("Enter Amount: ")
		while True:
			if checkbal(amt)==1:
				break
			else:
				print("You Enter Invalid Amount!!")
		if prv_amt>amt:
			total_balance=float(prv_amt)-float(amt)
			u1=(total_balance,nacc_no)
			cas.execute(upd,u1)
			con.commit()
			userid=record[0][0]
			x = datetime.datetime.now()
			dt=x.strftime("%d/%m/%y %H:%M:%S")
			print("YOU WITHDRAWAL MONEY FROM Your ACCOUNT :)")
			ins="INSERT into trans(u_id,admin_id,Dt,amount,Balance,Flag)values(?,?,?,?,?,?)"
			t=(userid,a_id,dt,amt,total_balance,'Debit')
			cas.execute(ins,t)
			con.commit()
			print("Your Available Balance is: ",total_balance)
			time.sleep(5)
			os.system('cls')
			ad_menu(a_id)
		else:
			print("You Have not much balance in your account!!!")
			time.sleep(5)
			os.system('cls')
			ad_menu(a_id)


def trans_list(a_id):
	print("\t\t *************** USER WANTS TO SEE ITS TRANSCATION HISTORY ***************")
	nacc_no=input("Enter Your Account Number: ")
	cas.execute("SELECT user.u_name,user.u_mob,user.u_accno,trans.amount,trans.Balance,trans.Flag,trans.Dt from user inner join trans on user.user_id=trans.u_id where u_accno=='"+nacc_no+"'")
	record=cas.fetchall()
	if record==[]:
		print("This Account Number Not Exist!!")
		time.sleep(5)
		os.system('cls')
		ad_menu(a_id)
	else:
		x=PrettyTable()
		Name=record[0][0]
		print("\t\t HELLO "+Name+" YOUR TRANSACTION HISTORY IS :-\n\n")
		x.field_names=["NAME OF USER","USER CONTACT NUMBER","ACCOUNT NUMBER","Amount","AVAILABLE BALANCE","STATUS","DATE AND TIME"]
		for i in record:
			x.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
		print(x)
		input("Press Enter to continue...")
		os.system('cls')
		ad_menu(a_id)
	
def log_table(a_id):
	cas.execute("SELECT trans.trans_id,trans.Dt,user.u_name,user.u_accno,admin.ad_name,admin.admin_id,trans.Flag from((trans inner join user on trans.u_id=user.user_id)inner join admin on trans.admin_id = admin.admin_id) ")	
	record=cas.fetchall()
	x=PrettyTable()
	x.field_names=["Transaction-Id","Date & Time","User Name","User Account Number","Admin Name","Admin-Id","STATUS"]
	for i in record:
		x.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
	print(x)
	input("Press Enter to continue...")
	os.system('cls')
	ad_menu(a_id)
def ad_menu(a_id):
	ch=input('''
				\t\t\t\t\tWELCOME TO ADMIN MENU :) :)
				1) CREATE ACCOUNT
				2) ADD BALANCE
				3) WITHDRAWAL BALANCE
				4) TRANSACTION LIST
				5) LOG RECORDS
				6) Logout
				Enter your choice(1-6): ''')
	if ch=='1':
		os.system('cls')
		create_acc(a_id)
	elif ch=='2':
		os.system('cls')
		add_bal(a_id)
	elif ch=='3':
		os.system('cls')
		withdraw_bal(a_id)
	elif ch=='4':
		os.system('cls')
		trans_list(a_id)
	elif ch=='5':
		os.system('cls')
		log_table(a_id)
	elif ch=='6':
		os.system('cls')
		init()
	else:
		print("You Enter Invalid Choice!!!")
		time.sleep(3)
		os.system('cls')
		ad_menu(a_id)


def init():
	ch=input('''
				WELCOME TO MAIN MENU OPTIONS
				1) ADMIN
				2) EXIT
				Enter your choice(1-2)''')
	if ch=='1':
		os.system('cls')
		ad_login()
	elif ch=='2':
		os.system('cls')
		exit()
	else:
		print("You Enter Invalid Choice!!!")
		time.sleep(3)
		os.system('cls')
		init()
init()

# x=PrettyTable()
# x.field_names=["ID","NAME","AGE","FNAME","DOB","MOBILE NUMBER","ACCOUNT NUMBER","BALANCE"]
# for i in record:
# 	x.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
# print(x)