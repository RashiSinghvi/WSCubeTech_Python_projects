import pickle as p
from prettytable import PrettyTable
import time
import os
###################### Dealer Registration############################
def deareg():
	print(" \t\t\t\t\t\t\t\t\t@ WELCOME TO DEALER REGISTRATION MODULE @")
	print("\n\n\n\n")
	file=open("Dealer.txt",'rb')
	c=p.load(file)
	file.close()
	if(len(c)==0):
		de_id=1
	else:
		de_id=list(c.keys())[-1]+1	
	name=input("Enter Name of Dealer: ")
	de_mail=input("Enter E-mail of Dealer: ")
	flag=0
	for i in c:
		if c[i][1]==de_mail:
			flag=1
			break
	if flag==0:
		de_psswd=input("Enter Password: ")
		de_cno=int(input("Enter Contact Number: "))
		de_addr=input("Enter Address of Dealer: ")
		file=open("Dealer.txt",'wb')
		c[de_id]=[name,de_mail,de_psswd,de_cno,de_addr]
		p.dump(c,file)
		file.close()
		print("Your Data is stored successfully")
		time.sleep(5)
		os.system('cls')
		init()
	elif flag==1:
		print("This Mail ID already exist.")
		time.sleep(3)
		os.system('cls')
		init()
###################### Dealer MENU############################
def d_menu(b):
		print('''
			WELCOME TO DEALER OPTIONS :)
			1)Add Cab
			2)View Cab
			3)Delete Cab
			4)View Request
			5)Change Password
			6)Logout''')
		n=input("Enter Your Choice(1-5): ")
		if n=='1':
			add_cab(b)
		elif n=='2':
			view_cab(b)
		elif n=='3':
			del_cab(b)
		elif n=='4':
			vd_req(b)
		elif n=='5':
			ch_passwd(b)
		elif n=='6':
			time.sleep(3)
			os.system('cls')
			init()			
		else:
			print("You Enter Invalid Choice!!")
			time.sleep(3)
			os.system('cls')
			d_menu(b)

###################### Dealer LOGIN ############################
def dea_login():	
	print(" \t\t\t\t\t\t\t\t\t@ WELCOME TO DEALER LOGIN MODULE @")
	print("\n\n\n\n")
	file=open("Dealer.txt",'rb')
	d=p.load(file)
	file.close()
	de_mail=input("Enter mail: ")
	de_psswd=input("Enter Password: ")
	c=0
	for a in d:
		if((d[a][2]==de_psswd) and (d[a][1]==de_mail)):
			a=d[a][0]
			b=de_mail
			c=1
			break
	if c==1:
		print('''
			CONGRATS :)
			Login succesfully
			Hello''',a)
		time.sleep(5)
		os.system('cls')
		d_menu(b)
	else:
		print("Invalid Username or Password")
		time.sleep(3)
		os.system('cls')
		init()		
###################### ADD CAB:-DEALER ############################
def add_cab(b):
	file=open("Cab.txt",'rb')
	di=p.load(file)
	
	if(len(di)==0):
		cab_id=1
	else:	
		cab_id=list(di.keys())[-1]+1
	
	file.close()
	ID=input("Enter Cab ID: ")
	flag=0
	for j in di:
		if di[j][0]==ID:
			flag=1
	if flag==1:
		print("This Cab ID Already exists!")
		d_menu(b)
	else:
		name=input("Enter Cab name: ")
		c_type=input("Enter Cab type: ")
		c_pk=input("Enter Pickup point: ")
		c_des=input("Enter Destination: ")
		c_status=input("Enter Status of cab(0- cab not available,1-cab available): ")
		if (c_status=='1'or c_status=='0'):
			file=open("Dealer.txt",'rb')
			d=p.load(file)
			file.close()
			for i in d:
				if d[i][1]==b:
					c=d[i][3]
					break
			file=open("Cab.txt",'wb')
			di[cab_id]=[ID,name,c_type,c_pk,c_des,c_status,b,c]
			p.dump(di,file)
			file.close()
			print("Your Data is recorded in file succesfully :)")
			time.sleep(3)
			os.system('cls')
			d_menu(b)
		else:
			print("OOPS YOU ENTER INVALID STATUS SYMBOL !!!")
			time.sleep(3)
			os.system('cls')
			print("\t\t\t\t\t\t\tAGAIN ENTER THE CAB DETAILS ")
			add_cab(b)

###################### VIEW CAB:- DEALER ############################
def view_cab(b):
	file=open("Cab.txt",'rb')
	d=p.load(file)
	file.close()
	x=PrettyTable()
	x.field_names=["Cab ID","Name","Type","From","To","Status"]
	#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Cab ID","Name","Type","From","To","Status"))
	for j in d:
		if  b==d[j][-2]:
			x.add_row([d[j][0],d[j][1],d[j][2],d[j][3],d[j][4],d[j][5]])
			#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} ".format(d[j][0],d[j][1],d[j][2],d[j][3],d[j][4],d[j][5]))		
	print(x)
	d_menu(b)
###################### DELETE CAB :- DEALER ############################
def del_cab(b):
	file=open("Cab.txt",'rb')
	d=p.load(file)
	file.close()
	ID=input("Enter Cab ID whose data to be delete: ")
	count=0
	for i in d:
		if ID==d[i][0]:
			a=i
			count=1
			break
	if count==1:
		n=input("Are You sure to delete cab(yes/no): ")
		if n=='yes'or n=='Yes':
			d.pop(a)
			print("Cab Data is Deleted Successfully..")
		file=open("Cab.txt",'wb')
		p.dump(d,file)
		file.close()
		view_cab(b)
		d_menu(b)
	else:
		print("This Cab-ID not found in file!!")
		d_menu(b)
###################### VIEW REQUEST : DEALER ############################
def vd_req(b):
	file=open("Request.txt",'rb')
	d=p.load(file)
	file.close()
	x=PrettyTable()
	x.field_names=["Serial No","Name of User","Contact Number","E-mail of user","Cab_id"]
	#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format("Serial No","Name of User","Contact Number","E-mail of user","Cab_id"))
	for i in d:
		if b==d[i][-1]:
			x.add_row([i,d[i][0],d[i][1],d[i][2],d[i][3]])
			#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format(i,d[i][0],d[i][1],d[i][2],d[i][3]))
	print(x)
	d_menu(b)
####################### MODIFY CAB DETAILS ############################
# def up_cab(b):
# 	file=open("Cab.txt",'rb')
# 	d=p.load(file)
# 	file.close()
# 	n=int(input("Enter the poistion of Cab-data where you want modification: "))
# 	count=0
# 	flag=0
# 	for i in d:
# 		if b==d[i][-2]:
# 			if n==i:
# 				count=1
# 				flag=1
# 				break
# 	print(i)
# 	if flag==1:
# 		if count==1:
# 			ID=input("Enter Cab ID: ")
# 			name=input("Enter Cab name: ")
# 			c_type=input("Enter Cab type: ")
# 			c_pk=input("Enter Pickup point: ")
# 			c_des=input("Enter Destination: ")
# 			c_status=input("Enter Status of cab(0- cab not available,1-cab available): ")
# 			file=open("Dealer.txt",'rb')
# 			di=p.load(file)
# 			file.close()
# 			for i in d:
# 				if di[i][1]==b:
# 					c=di[i][3]
# 					break
# 			file=open("Cab.txt",'wb')
# 			d[n]=[ID,name,c_type,c_pk,c_des,c_status,b,c]
# 			p.dump(d,file)
# 			file.close()
# 			d_menu(b)
# 		else:
# 			print("Poistion not found in cab details!!!")
# 			d_menu(b)
# 	else:
# 		print("This Dealer not enter the data previous...")
# 		d_menu(b)


###################### CHANGE PASSWORD OF DEALER############################
def ch_passwd(b):
	file=open("Dealer.txt",'rb')
	d=p.load(file)
	file.close()
	c=0
	pswd=input("Enter your old Password: ")
	for i in d:
		if((b==d[i][1]) and (pswd==d[i][2])):
			new_pswd=input("Enter New Password: ")
			conf_pswd=input("Confirm Your Password: ")
			if new_pswd==conf_pswd:
				file=open("Dealer.txt",'wb')
				d[i][2]=conf_pswd
				p.dump(d,file)
				print("Your Password Changes Successfully :)")
			else:
				print("you enter wrong password..")
	d_menu(b)

###################### USER REGISTRATION ############################
def user_reg():
	file=open("User.txt",'rb')
	d=p.load(file)
	if(len(d)==0):
		user_id=1
	else:
		user_id=list(d.keys())[-1]+1
	file.close()   
	print("\t\tWELCOME TO USER REGISTRATION MODULE :)") 
	name=input("Enter Name: ")
	user_email=input("Enter E-mail of user: ")
	flag=0
	for i in d:
		if d[i][1]==user_email:
			print("This Mail ID Already exist")
			flag=1
	if flag==0:
		user_psswd=input("Enter Password: ")
		user_cno=int(input("Enter Contact Number:"))
		file=open("User.txt",'wb')
		d[user_id]=[name,user_email,user_psswd,user_cno]
		p.dump(d,file)
		print("Your Data is stored succesfully")
		file.close()
		time.sleep(3)
		os.system('cls')
		init()
	elif flag==1:
		os.system('cls')
		init()
###################### USER LOGIN ############################
def user_login():
	file=open("User.txt",'rb')
	d=p.load(file)
	file.close()
	print("\t\t\t\tWELCOME TO USER LOGIN MODULE :)")
	u_mail=input("Enter Username or E-mail: ")
	u_pswd=input("Enter Password: ")
	c=0
	for i in d:
		if((u_mail==d[i][1]) and (u_pswd==d[i][2])):
			a=d[i][0]
			x=u_mail
			c=1
			break
	if c==1:
		os.system('cls')
		print('''
               Login Sucessfully...
               Hello''',a)
		u_menu(x)
	else:
		print("Invalid Username or Password...")
		os.system('cls')
		init()
###################### USER MENU ############################
def u_menu(x):
	print("""
			WELCOME TO USER OPTIONS :)
			1) View Cab
			2) Search Cab
			3) Request Cab
			4) Logout""")
	n=input("Enter Your Choice(1-4): ")
	if n=='1':
		os.system('cls')
		ucab_view(x)
	elif n=='2':
		os.system('cls')
		ucab_serch(x)
	elif n=='3':
		os.system('cls')
		u_req(x)
	elif n=='4':
		os.system('cls')
		init()
	else:
		print("You Enter Invalid Choice!!")
		os.system('cls')
		u_menu(x)

###################### VIEW CAB:- USER ############################
def ucab_view(x):
	file=open("Cab.txt",'rb')
	d=p.load(file)
	file.close()
	y=PrettyTable()
	print("\t\t\t\t\tUSER CAB DETAILS ")
	y.field_names=["ID","Name","Type","From","To","Status","E-mail of Dealer","Dealer contact number"]
	#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format("ID","Name","Type","From","To","Status","E-mail of Dealer","Dealer contact number"))
	for j in d:
		if d[j][-3]=='1':
			y.add_row([d[j][0],d[j][1],d[j][2],d[j][3],d[j][4],d[j][5],d[j][6],d[j][7]])
		#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format(d[j][0],d[j][1],d[j][2],d[j][3],d[j][4],d[j][5],d[j][6],d[j][7]))
	print(y)
	u_menu(x)
###################### SEARCH CAB:- USER ############################
def ucab_serch(x):
	file=open("Cab.txt",'rb')
	d=p.load(file)
	file.close()
	y=PrettyTable()
	npk=input("Enter Pickup point: ")
	ndes=input("Enter Destination point: ")
	y.field_names=["ID","Name","Type","From","To","Status","E-mail of Dealer","Dealer contact number"]
	#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format("ID","Name","Type","From","To","Status","E-mail of Dealer","Dealer contact number"))
	for i in d:
		if((d[i][3]==npk) and (d[i][4]==ndes)):
			y.add_row([d[i][0],d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7]])
			#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format(d[i][0],d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7]))
	print(y)
	u_menu(x)
###################### REQUEST CAB:- USER ############################
def u_req(x):
	file=open("Request.txt",'rb')
	d=p.load(file)
	file.close()
	req_id=len(d)+1
	file=open("User.txt",'rb')
	do=p.load(file)
	file.close()
	for j in do:
		if do[j][1]==x:
			name=do[j][0]
			c_no=do[j][-1] 
			break
	print("\t\t\t\t\t\t\t\tRequest module require Specific Cab id for Booking the Cab")
	cab_id=input("Enter Cab Id : ")
	file=open("Cab.txt",'rb')
	di=p.load(file)
	file.close()
	c=0
	for i in di:
		if(di[i][0]==cab_id) and(di[i][-3]=='1'):
			c=1
			a=di[i][-2]
	if c==1:
		d[req_id]=[name,c_no,x,cab_id,a]
		print("Your Request is Accepted :)")
	else:
		print("Specific Cab Id not found or Cab is not active")
	file=open("Request.txt",'wb')
	p.dump(d,file)
	file.close()
	u_menu(x)

###################### ADMIN LOGIN ############################
def admin_login():
	file=open("Admin.txt",'rb')
	d=p.load(file)
	file.close()
	print(" \t\t\t\t\t\t\t\t\t@ WELCOME TO ADMIN LOGIN MODULE @")
	print("\n\n\n\n")
	a_mail=input("Enter Usernmae/E-mail: ")
	pwsd=input("Enter Password: ")
	if ((d[1]==a_mail) and (d[2]==pwsd)):
		os.system('cls')
		print("""
				YOU LOGIN SUCCESSFULLY:)
				HELLO ADMIN""")
		time.sleep(3)
		os.system('cls')
		a_menu()
	else:
		print("Invalid Username or Password....")
		time.sleep(5)
		os.system('cls')
		init()

###################### ADMIN MENU ############################
def a_menu():
	print("""
			WELCOME TO ADMIN MENU :)

			1) View User
			2) Delete User
			3) View Cab
			4) Delete Cab
			5) Disable Cab
			6) View Dealer
			7) Delete Dealer
			8) View All Request
			9) Change Password
			10) Logout
		""")
	n=input("Enter your Choice(1-10): ")
	if n=='1':
		v_user()
	elif n=='2':
		del_user()
	elif n=='3':
		v_cab()
	elif n=='4':
		a_del_cab()
	elif n=='5':
		a_dis_status()
	elif n=='6':
		v_dealer()
	elif n=='7':
		del_dea()
	elif n=='8':
		v_req()
	elif n=='9':
		a_ch_passwd()
	elif n=='10':
		os.system('cls')
		init()
	else:
		print("You Enter Invalid Choice!!")
		a_menu()

###################### VIEW USER:- ADMIN ############################
def v_user():
	file=open("User.txt",'rb')
	d=p.load(file)
	file.close()
	x=PrettyTable()
	x.field_names=["Serial no","Name","E-mail","Password","Contact Number"]
	#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format("Serial no","Name","E-mail","Password","Contact Number"))
	for i in d:
		x.add_row([i,d[i][0],d[i][1],d[i][2],d[i][3]])
		#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format(i,d[i][0],d[i][1],d[i][2],d[i][3]))
	print(x)
	a_menu()

###################### VIEW DEALER:- ADMIN ############################
def v_dealer():
	file=open("Dealer.txt",'rb')
	d=p.load(file)
	file.close()
	x=PrettyTable()
	x.field_names=["Serial no","Name","E-mail","Password","Contact Number","Address"]
	#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Serial no","Name","E-mail","Password","Contact Number","Address"))
	for i in d:
		x.add_row([i,d[i][0],d[i][1],d[i][2],d[i][3],d[i][4]])
		#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(i,d[i][0],d[i][1],d[i][2],d[i][3],d[i][4]))
	print(x)
	a_menu()
###################### VIEW CAB:- ADMIN ############################
def v_cab():
	file=open("Cab.txt",'rb')
	d=p.load(file)
	file.close()
	x=PrettyTable()
	x.field_names=["Serial no","ID","Name","Type","From","To","Status","Dealer-mail","Dealer contact number"]
	#print("{0:<18} {1:<18} {2:<18} {3:<18} {4:<18} {5:<18} {6:<12} {7:<18} {8:<18}".format("Serial no","ID","Name","Type","From","To","Status","Dealer-mail","Dealer contact number"))
	for i in d:
		x.add_row([i,d[i][0],d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7]])
		#print("{0:<18} {1:<18} {2:<18} {3:<18} {4:<18} {5:<18} {6:<12} {7:<18} {8:<18}".format(i,d[i][0],d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7]))
	print(x)
	a_menu()
###################### DELETE USER:- ADMIN ############################
def del_user():
	file=open("User.txt",'rb')
	d=p.load(file)
	file.close()
	u_mail=input("Enter Username/mail whose data to be deleted: ")
	count=0
	for i in d:
		if d[i][1]==u_mail:
			a=i
			count=1
			break
	if count==1:
		n=input("Are You sure to delete userdata(yes/no): ")
		file=open("Request.txt",'rb')
		di=p.load(file)
		file.close()
		do={}
		if n=='yes'or n=='Yes':
			for j in di:
				if di[j][2]==u_mail:
					do[j]=di.get(j)
			for key in do.keys():
				del di[key]
			d.pop(a)
			print("User Data is Deleted Successfully..")
		file=open("Request.txt",'wb')
		p.dump(di,file)
		file.close()
		file=open("User.txt",'wb')
		p.dump(d,file)
		file.close()
		a_menu()
	else:
		print("This username not found in file!")
		a_menu()
###################### DELETE DEALER:- ADMIN ############################
def del_dea():
	file=open("Dealer.txt",'rb')
	d=p.load(file)
	file.close()
	u_mail=input("Enter Username/mail whose data to be deleted: ")
	count=0
	for i in d:
		if d[i][1]==u_mail:
			a=i
			count=1
			break
	if count==1:
		n=input("Are You sure to delete Dealer data(yes/no): ")
		file=open("Cab.txt",'rb')
		di=p.load(file)
		file.close()
		file=open("Request.txt",'rb')
		dy=p.load(file)
		file.close()
		do={}
		dm={}
		if n=='yes'or n=='Yes':
			for j in di:
				if di[j][-2]==u_mail:
					do[j]=di.get(j)
			for key in do.keys():
				del di[key]
			for k in dy:
				if dy[k][-1]==u_mail:
					dm[k]=dy.get(k)
			for ky in dm.keys():
				del dy[ky]
			for  l in d:
				if d[l][1]==u_mail:
					d.pop(a)
					break
			print("Dealer Data is Deleted Successfully..")
		file=open("Cab.txt",'wb')
		p.dump(di,file)
		file.close()
		file=open("Request.txt",'wb')
		p.dump(dy,file)
		file.close()
		file=open("Dealer.txt",'wb')
		p.dump(d,file)
		file.close()
		a_menu()
	else:
		print("This username not found in file!")
		a_menu()
###################### DELETE CAB:- ADMIN ############################
def a_del_cab():
	file=open("Cab.txt",'rb')
	d=p.load(file)
	file.close()
	ID=input("Enter Cab ID whose data to be delete: ")
	count=0
	for i in d:
		if ID==d[i][0]:
			a=i
			count=1
			break
	if count==1:
		n=input("Are You sure to delete cab(yes/no): ")
		file=open("Request.txt",'rb')
		di=p.load(file)
		file.close()
		do={}
		if n=='yes'or n=='Yes':
			for j in di:
				if di[j][-2]==ID:
					do[j]=di.get(j)
			for key in do.keys():
				del di[key]
			d.pop(a)
			print("Cab Data is Deleted Successfully..")
		file=open("Request.txt",'wb')
		p.dump(di,file)
		file.close()
		file=open("Cab.txt",'wb')
		p.dump(d,file)
		file.close()
		a_menu()
	else:
		print("This Cab-ID not found in file!!")
		a_menu()

###################### DISABLE CAB:- ADMIN ############################
def a_dis_status():
	file=open("Cab.txt",'rb')
	d=p.load(file)
	file.close()
	ID=input("Enter Cab Id whose Status you want to disable: ")
	c=0
	for i in d:
		if(d[i][0]==ID):
			a=d[i][-3]
			c=1
			break
	if c==1:
		if a=='1':
			a='0'
		else:
			print("Status is already Zero!")
	else:
		print("Match not found!!")
	for j in d:
		if(d[i][0]==ID):
			d[i][-3]=a
			print("Cab Status Disable..")
			break
	file=open("Cab.txt",'wb')
	p.dump(d,file)
	file.close()
	a_menu()
###################### CHANGE PASSWORD:- ADMIN ############################
def a_ch_passwd():
	file=open("Admin.txt",'rb')
	d=p.load(file)
	file.close()
	pswd=input("Enter your old Password: ")
	if pswd==d[2]:
		new_pswd=input("Enter New Password: ")
		conf_pswd=input("Confirm Your Password: ")
		if new_pswd==conf_pswd:
			file=open("Admin.txt",'wb')
			d[2]=conf_pswd
			p.dump(d,file)
			print("Your Password Changes Successfully :)")
		else:
			print("you enter wrong password..")
	a_menu()
###################### VIEW ALL REQUEST:- ADMIN ############################
def v_req():
	file=open("Request.txt",'rb')
	d=p.load(file)
	file.close()
	x=PrettyTable()
	x.field_names=["Serial No","Name of user","Contact Number","E-mail of user","Cab-ID","Dealer-ID"]
	#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("Serial No","Name of user","Contact Number","E-mail of user","Cab-ID","Dealer-ID"))
	for i in d:
		x.add_row([i,d[i][0],d[i][1],d[i][2],d[i][3],d[i][4]])
		#print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(i,d[i][0],d[i][1],d[i][2],d[i][3],d[i][4]))
	print(x)
	a_menu()
###################### MAIN MENU ############################
def init():
	print('''   
				WELCOME TO MAIN MENU :)

				1) Admin Login
				2) User Register
				3) User Login
				4) Dealer Register
				5) Dealer Login
				6) Exit''')
	n=input("Enter Your Choice(1-6): ")
	if n=='1':
		os.system('cls')
		admin_login()
	elif n=='2':
		os.system('cls')
		user_reg()
	elif n=='3':
		os.system('cls')
		user_login()
	elif n=='4':
		os.system('cls')
		deareg()
	elif n=='5':
		os.system('cls')
		dea_login()
	elif n=='6':
		exit() 
	else:
		print("You Enter Invalid Choice!!")
		time.sleep(3)
		os.system('cls')
		init()
init()
