# Imporing OS for executing the Linux Commands 
import os
#importing getpass for echo back less authentication
import getpass
#importing libraries for making the application speech friendly
import os
import pyttsx3 as tts
import speech_recognition as sr

#---------------------------------speech part---------------------------------------------------


def spoken_input():

	wel= "Hello, welcome to our Tech Menu. Please say the option number you would like to choose."
	tts.speak(wel)
	a=  """
		Press 1: To Check Date
		Press 2: To Check Calender
		Press 3: To Add User
		Press 4: To Configure Web_server
		Press 5: To configure SSH_Server
		Press 6: To Start Docker 
		Press 7: To Exit
		""" 
	tts.speak(a)  #this allows the device to instruct the user using speech

	r = sr.Recognizer()
	mic = sr.Microphone()


	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio= r.listen(source)
	x= r.recognize_google(audio)
	p= x.lower()
	print("You said: ",p)
	

	# converting spoken input into integer form for the program
	while (p!= 'seven'):
		if p=='one':
			ch=1
			tts.speak('Command is being executed')
			return ch

		elif p=='two':
			ch=2
			tts.speak('Command is being executed')
			return ch

		elif p=='three':
			ch=3
			tts.speak('Command is being executed')
			return ch

		elif p=='four':
			ch=4
			tts.speak('Command is being executed')
			return ch

		elif p=='five':
			ch=5
			tts.speak('Command is being executed')
			return ch

		elif p=='six':
			ch=6
			tts.speak('Command is being executed')
			return ch

		elif p=='seven':
			ch=7
			tts.speak('Command is being executed')
			ex='Menu closed. Have a lovely day!'
			print(ex)
			tts.speak(ex)
			return ch

		else:
			tts.speak('number not found in the menu')
			ch=7
			ex='Menu closed. Have a lovely day!'
			print(ex)
			tts.speak(ex)
			return ch


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
	Press 7: To Create LVM Partition
	Press 8: To Start AWS CLI
	Press 9: To Exit
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
			#LVM Creation Automation
			os.system("tput setaf 3")
			print("\t\t\tWelcome To LVM Creation")
			os.system("tput setaf 7")
			print("\t\t\t------------------------")
			
			a1 = input("Enter Disk1 Name :")
			a2 = input("Enter Disk2 Name :")
			v = input("Enter Name Of Your Volume Group :")
			l = input("Enter Name Of Your Logical Volume :")
			s = input("Enter Size Of Your Logical Volume :")
			mp = input("Enter Mount Point Of Your LVM :")
			#pv creation 
			os.system("pvcreate /dev/"+a1)
			os.system("pvcreate /dev/"+a2)
			#vg creation
			os.system("vgcreate "+v+" /dev/"+a1+" /dev/"+a2)
			#lv creation
			os.system("lvcreate --size "+s+" --name "+l+" "+v)
			#Formatting LVM
			os.system("mkfs.ext4 /dev/"+v+"/"+l)
			#mounting LVM
			os.system("mkdir /"+mp)
			os.system("mount /dev/"+v+"/"+l+" "+"/"+mp)
			os.system("cd /"+mp)
			exit()

		elif int(ch)==8:
			import os
	os.system("tput setaf 1")
	print("\t\t\tWelcome To AWS CLI Automation")
	os.system("tput setaf 7")
	print("\t\t\t------------------------------")
	os.system("aws configure")

	while True:
		os.system("clear")
		os.system("tput setaf 3")
		print("""	
		Press 1: To Launch EC2 Instance	
		Press 2: To Create Security Group	
		Press 3: To Create Key Pair	
		Press 4: To Launch EBS Volume	
		Press 5: To Attach EBS Volume With EC2 Instance 	
		Press 6: To Launched S3 Buckets	
		Press 7: To List S3 Buckets
		Press 8: To Create Cloud Front Distribution
		Press 9: To Exit	
		""")
		os.system("tput setaf 6")
		i = int(input("Enter Your Choice :"))
		print(i)
		if i==1:
			k1 = input("Enter Your Key Pair Name :")
			sgi = input("Enter Your Security Group ID :")
			si = input("Enter Your Subnet ID :")
			iid = input("Enter Your Image ID :")
			os.system("aws ec2 run-instances --image-id "+iid+" --instance-type t2.micro --count 1 --subnet-id "+si+" --security-group-ids "+sgi+" --key-name "+k1)
			os.system("tput setaf 7")
			print("------------------------EC2 Instance Launched Successfully---------------------------")
		elif i==2:
			gn = input("Enter Security Group Name :")
			gd = input("Enter Name Of your Security Group :")
			os.system("aws ec2 create-security-group --description "+gd+" --group-name "+gn)
			os.system("tput setaf 7")
			print("--------------------Security Group Launched Successfully----------------------")

		elif i==3:
			k = input("Enter Name Of Your Key Pair :")
			os.system("aws ec2 create-key-pair --key-name "+k)
			print("-------------------- Key Pair Created Successfully----------------------")
		elif i==4:
			az = input("Enter Availability Zone :")
			vt = input("Enter Volume Type :")
			si = input("Enter Size Of EBS Volume in GB :")
			os.system("aws ec2 create-volume --availability-zone "+az+" --volume-type "+vt+" --size "+si)
			print("-------------------- EBS Volume Launched Successfully----------------------")
		elif i==5:
			vi = input("Enter Your EBS Volume ID :")
			iii = input("Enter Your Instance ID :")
			di = input("Enter Your Device Name /dev/.. :")
			os.system("aws ec2 attach-volume  --volume-id "+vi+"  --instance-id "+iii+ "--device "+di)
			print("-------------------- EBS Volume Attached Successfully----------------------")
		elif i==6:
			bn = input("Enter Your Bucket Name :")
			os.system("aws s3 mb s3://"+bn)
			print("-------------------- S3 Bucket Created Successfully----------------------")
		elif i==7:
			bnn = input("Enter Your Bucket Name :")
			os.system("aws s3 ls s3://"+bnn)
		elif i==8:
			bnnn = ("Enter S3 Bucket Name :")
			im = ("Enter Image Name :")
			os.system("aws cloudfront create-distribution --origin-domain-name "+bnnn+".s3.amazonaws.com --default-root-object "+im)
			print("-------------------- Cloud Front Distribution Created Successfully----------------------")
		elif i==9:
		exit()

		
	

		elif int(ch)==9:
			Credits()
			exit()

		else:
    			print("Error! Option Not Supported")


#Functions for Credits
def Credits():
	os.system("tput setaf 11")
	print("\t\t\t\t\t\t\tMade By : Gursimar Singh, Janhavi Jain, Sourav Pattnaik, Kodgire Ashutosh and Akshit")
	print("\n")
	os.system("tput setaf 7")

	

#Function with various options and their working for Remote System call
def Options_remote(ch):
		os.system("tput setaf 6")
		if int(ch)==1:
			os.system("ssh {} date".format(ip_address))

		elif int(ch)==2:
			os.system("ssh {} cal".format(ip_address))

		elif int(ch)==3:
			print("Name of the User you want to Add: ", end="")
			create_user=input()
			os.system("ssh {} useradd {}".format(ip_address,create_user))

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
