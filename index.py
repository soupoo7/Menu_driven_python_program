# Imporing OS for executing the Linux Commands 
import os
#importing getpass for echo back less authentication
import getpass

print("\n")

#-------------------------------------------Functions--------------------------------------------------

# Heading Display function
def Head(): 
	os.system("tput setaf 3")
	print("\t\t\tHey, Welcome! This is my TUI that makes Life Simple without memorizing the commands for RHEL8")
	os.system("tput setaf 3")
	print("\t\t\t---------------------------------------------------------------------------------------------")
	
#Username Password Auth Function
def Auth():
	passwd = getpass.getpass("Enter your Password :")
	apass = "redhat"
	if passwd != apass:
		print("\n")
		os.system("tput setaf 1")
		print("Incorrect Password! Try Again.....")
		Credits()
		exit()
  
  # Display the Options
def Task():
	os.system("tput setaf 4")
	print("""
	Press 1: To Check Date
	Press 2: To Check Calender
	Press 3: To Add User
	Press 4: To Configure Web_server
	Press 5: To configure SSH_Server
	Press 6: To Start Docker 
	Press 7: To Exit
	""")
	
#Function Asking the Available Options from user to perform that task
def Asking_option():
	os.system("tput setaf 2")
	print("Enter Your Choice:", end="")
	ch=input()	
	print("\n")
	return ch

#Function with various options and their working for Local System call
def Options_local(ch):
		os.system("tput setaf 6")
		if int(ch)==1:
			os.system("date")

		elif int(ch)==2:
    			os.system("cal")

		elif int(ch)==3:
			print("Name of the User: ", end="")
			create_user=input()
			os.system("useradd {}".format(create_user))

		elif int(ch)==4:
    			os.system("")

		elif int(ch)==5:
    			os.system("")

		elif int(ch)==6:
    			os.system("systemctl start docker")

		elif int(ch)==7:
			Credits()
			exit()

		else:
    			print("Error! Option Not Supported")


#Functions for Credits
def Credits():
	os.system("tput setaf 11")
	print("\t\t\t\t\t\t\tMade By Gursimar Singh")
	print("\n")
	os.system("tput setaf 7")
	

#Function with various options and their working for Remote System call
def Options_remote(ch):
		os.system("tput setaf 6")
		if int(ch)==1:
			os.print("ssh {} date".format(ip_address))

		elif int(ch)==2:
			os.print("ssh {} cal".format(ip_address))

		elif int(ch)==3:
			print("Name of the User you want to Add: ", end="")
			create_user=input()
			os.print("ssh {} useradd {}".format(ip_address,create_user))

		elif int(ch)==4:
    			print("")	#Change print in all options to os.system when actually working with
					#two systems. I am doing as I am doing alone.
		elif int(ch)==5:
    			print("")

		elif int(ch)==6:
    			print("")

		elif int(ch)==7:
			Credits()
			exit()

		else:
    			print("Error! Option Not Supported")


def Local_remote():
	#Asking User Where to perform the job
	os.system("tput setaf 7")
	print("Where you want to perform the Job (Local/Remote) System)")
	os.system("tput setaf 3")
	print("Press Keyword L for Local   OR   Press Keyword R for Remote:", end="")
	location=input()
	print("\n")
	return location


#-----------------------------------Start of the TUI.------------------------------------------------------



#------------------------------------Authentication--------------------------------------------------------
#Calling Head
Head()
#Calling Task function 
Task()
os.system("tput setaf 7")
#Calling Auth
Auth()
os.system("clear")


#---------------------------------Local or Remote Option---------------------------------------------------
#Calling Head
Head()
#Calling Task function 
Task()
#Calling Local_remote 
location=Local_remote()
if location == "R" or location == "r":
		#Asking for IP Address of remote System
		os.system("tput setaf 3")
		print("Enter the IP Address of Remote System:", end="")
		ip_address=input()
		print("\n")
os.system("clear")

#-----------------------------------While Loop for continuity----------------------------------------------

cont=True 
#Declaring Cont Variable to continue Till False

#Start of While Loop for Asking Options and Executing
while(cont == True):  
	
	#Calling Head
	Head()
	#Calling Task function 
	Task()

	#If the task is for Local System then do this
	if location == "L" or location == "l":
		os.system("tput setaf 7")
		print("You are in Local System")
		print("\n")

		#Calling Asking_option function
		ch=Asking_option()
		#Calling Options_local function
		Options_local(ch)


	#If the task for Remote System then do this
	elif location == "R" or location == "r":
		os.system("tput setaf 7")
		print("You are in Remote System")
		print("\n")

		#Calling Asking_option function
		ch=Asking_option()
		#Calling Options_remote function	
		Options_remote(ch)


	#If not both Local or Remote then do this
	else:
		os.system("tput setaf 1")
		print("Job Location Does not Supported!")
		print("You can use Either (Local or Remote) System")
		Credits()
		print("\n")
		exit()

	print("\n")
	os.system("tput setaf 7")
	input("Enter to Continue.......")
	os.system("clear")
	print("\n")





#------------------------------------------------Credits---------------------------------------------------
##os.system("tput setaf 11")
##print("\t\t\t\t\t\t\tMade By Arth Grp. 17")
#Outside While Loop for Exiting our TUI
##print("\n")
##os.system("tput setaf 7")
