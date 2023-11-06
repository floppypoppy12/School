#Caesar Cipher encoder and decoder.
import time
#-------------------------------------
def choice():
  print("This program will encode or decode a caesar cipher!")
  decision=int(input("Type '1' for encode and '2' for decode:"))
  if decision==1:
    encode()
  else:
    decode ()
#-------------------------------------




#-------------------------------------
#Exceptions
def encode():
  #-----------------------------------
  print("Reminder: All input characters must be in the same case!")
  tbe=input(str("Please enter a message to be encoded:"))
  key=int(input("How much would you like it to shift by?:"))
  message=[]
  for i in range(0,len(tbe)):
    message.append(tbe[i])
  #-----------------------------------
  #Individual Character put into array
  newmessage=[]
  #-----------------------------------
  #Character exceptions and loop
  for messageindex in range(0,len(message)):
    lettervalue=ord(message[messageindex])
    newvalue=lettervalue+key
    if lettervalue>122:
      newvalue=lettervalue
    if lettervalue<97 and lettervalue>90:
      newvalue=lettervalue
    if lettervalue<65 and lettervalue>31:
      newvalue=lettervalue
    if newvalue>122 and lettervalue<122:
      newvalue=newvalue-26
    #Exceptions for capitals
    if newvalue>90 and lettervalue<90:
      newvalue=newvalue-26
      
    newmessage.append(chr(newvalue))
  newmessage1=''.join(newmessage)
  print("Your new message is:",newmessage1)


def decode():
  print("Reminder: All letters must be in the same case!")
  tbd=input(str("Please enter a message to be decoded:"))
  print("Do you know how much it was shifted by?")
  eliminationdecision=input("(y/n):")
  if eliminationdecision=='n':
    tbdelim=input("Please enter a message to be decoded:")
    dmessage=[]
    for a in range(0,len(tbd)):
      dmessage.append(tbd[a])
    dnewmessage=[]
    #Characters put into a list
    #Exceptions and loop
    for p in range (0,27):
      elimkey=p
      dnewmessage=[]
      for dmessageindex in range(0,len(dmessage)):
        dlettervalue=ord(dmessage[dmessageindex])
        dnewvalue=dlettervalue-elimkey
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
#--------------------------------------------------------------------
  elif eliminationdecision=='y':
    dkey=int(input("How much was it shifted by:"))
    dmessage=[]
    for a in range(0,len(tbd)):
      dmessage.append(tbd[a])
    dnewmessage=[]
    #Characters put into a list
    #Exceptions and loop
    for dmessageindex in range(0,len(dmessage)):
      dlettervalue=ord(dmessage[dmessageindex])
      dnewvalue=dlettervalue-dkey
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
  else:
    eliminationdecision=input("(y/n):")
    print("Your original message is:",dnewmessage1)
    
  
  
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
  
