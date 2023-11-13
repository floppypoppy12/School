#Caesar Cipher encoder and decoder.
import time
#-------------------------------------
def choice():
  print("This program will encode or decode a caesar cipher!")
  decision=input("Type '1' for encode and '2' for decode:")
  if decision=='1':
    encode()
  elif decision=='2':
    decode ()
  else:
    choice()
#-------------------------------------

def counting(key,message,messageindex,countkey):
  count=0
  if countkey>26:
    countkey=countkey%26
  elif countkey<1:
    counting(key)
  if message[messageindex].isupper()==True or message[messageindex].islower()==True:
    count=count+1
  else:
    count=count
  if ord(message[messageindex])!=32:
    if count%countkey==0:
      key=key+1
    else:
      key=key
  else:
    key=key
  return key

#-------------------------------------
#Exceptions
def encode():
  #-----------------------------------
  print("Reminder: All input characters must be in the same case!")
  tbe=input(str("Please enter a message to be encoded:"))
  key=int(input("Shift 1:"))
  countingd=input("Alphabetical:")
  if countingd=='y':
    countkey=int(input("Shift 2:"))
  message=[]
  for i in range(0,len(tbe)):
    message.append(tbe[i])
  #-----------------------------------
  #Individual Character put into array
  newmessage=[]
  #-----------------------------------
  #Character exceptions and loop
  count=0
  for messageindex in range(0,len(message)):
    if countingd=='y':
      key=counting(key,message,i,countkey)
    lettervalue=ord(message[messageindex])
    newvalue=lettervalue+key
    if lettervalue>122:
      newvalue=lettervalue
    if lettervalue<97 and lettervalue>90:
      newvalue=lettervalue
    if lettervalue<65 and lettervalue>31:
      newvalue=lettervalue
    if newvalue>122 and lettervalue<122:
      while newvalue>122 and lettervalue<122:
        newvalue=newvalue-26
    #Exceptions for capitals
    if newvalue>90 and lettervalue<90:
      newvalue=newvalue-26
    #----------------------------------------------------------
    if message[messageindex].isupper()==True or message[messageindex].islower()==True:
      count=count+1
    else:
      count=count
    if counting=='y' and ord(message[messageindex])!=32:
      if count%countkey==0:
        key=key+1
      else:
        key=key
    else:
      key=key
    newmessage.append(chr(newvalue))
  newmessage1=''.join(newmessage)
  print("Your new message is:",newmessage1)


def decode():
  print("Reminder: All letters must be in the same case!")
  tbd=input(str("Please enter a message to be decoded:"))
  print("Do you know how much it was shifted by?")
  eliminationdecision=input("(y/n):")
  if eliminationdecision=='n':
    decoden(tbd)
  elif eliminationdecision=='y':
    decodey(tbd,key)
  else:
    decode()
#--------------------------------------------------------------------
def decodey(tbd,key):
    key=int(input("How much was it shifted by:"))
    dmessage=[]
    for a in range(0,len(tbd)):
      dmessage.append(tbd[a])
    dnewmessage=[]
    #Characters put into a list
    #Exceptions and loop
    for dmessageindex in range(0,len(dmessage)):
      dlettervalue=ord(dmessage[dmessageindex])
      dnewvalue=dlettervalue-key
      if dlettervalue>122:
        dnewvalue=dlettervalue
      if dlettervalue<97 and dlettervalue>90:
        dnewvalue=dlettervalue
      if dlettervalue<65 and dlettervalue>31:
        dnewvalue=dlettervalue
      if dlettervalue>=97 and dnewvalue<97:
        dnewvalue=dnewvalue+26
      if dnewvalue<65 and dlettervalue>=65:
        dnewvalue=dnewvalue+26
      dnewmessage.append(chr(dnewvalue))
      dnewmessage1=''.join(dnewmessage)
    print("Your original message is:",dnewmessage1)
    
def decoden(tbd):
    tbdelim=input("Please enter a message to be decoded:")
    dmessage=[]
    for a in range(0,len(tbd)):
      dmessage.append(tbd[a])
    dnewmessage=[]
    #Characters put into a list
    #Exceptions and loop
    for p in range (1,27):
      elimkey=0
      dnewmessage=[]
      for dmessageindex in range(0,len(dmessage)):
        dlettervalue=ord(dmessage[dmessageindex])
        dnewvalue=dlettervalue-p
        if dlettervalue>122:
          dnewvalue=dlettervalue
        if dlettervalue<97 and dlettervalue>90:
          dnewvalue=dlettervalue
        if dlettervalue<65 and dlettervalue>31:
          dnewvalue=dlettervalue
        if dlettervalue>=97 and dnewvalue<97:
          dnewvalue=dnewvalue+26
        if dnewvalue<65 and dlettervalue>=65:
          dnewvalue=dnewvalue+26
        dnewmessage.append(chr(dnewvalue))
        dnewmessage1=''.join(dnewmessage)
      print(p,":",dnewmessage1)
  
choice()
time.sleep(1)
print("Would you like to go again?")
time.sleep(0.5)
print("Choose 'y' for yes and 'n' for no!")
again=input(":")

if again=='y':
  choice()
else:
  print("Good luck!")
  
