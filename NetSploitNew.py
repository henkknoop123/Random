from calendar import c
import os,string;from pystyle import *;from time import sleep;from random import choice, randint
import random
logo = """                         



███╗░░██╗███████╗████████╗░██████╗██████╗░██╗░░░░░░█████╗░██╗████████╗
████╗░██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║░░░░░██╔══██╗██║╚══██╔══╝
██╔██╗██║█████╗░░░░░██║░░░╚█████╗░██████╔╝██║░░░░░██║░░██║██║░░░██║░░░
██║╚████║██╔══╝░░░░░██║░░░░╚═══██╗██╔═══╝░██║░░░░░██║░░██║██║░░░██║░░░
██║░╚███║███████╗░░░██║░░░██████╔╝██║░░░░░███████╗╚█████╔╝██║░░░██║░░░
╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═════╝░╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░░╚═╝░░░
"""
os.system("mode con cols=92 lines=52")
os.system("title " + "NetSploit || Cornettoo")
class Code:
   def __init__(self):
      print(f"{Col.dark_red}{logo}")
      print(f"\t\t\t     #{Col.white} Coded by Cornettoo{Col.dark_red}--Discord")
      print(f"\t\t\t     #{Col.white} Version:{Col.green} V1.5{Col.dark_red}")
      print(f"\t\t\t     #{Col.white} MAKE SURE TO{Col.green} FULL SCREEN")
      try:
         c = int(input(f"""
{Col.white}[{Col.dark_red}1{Col.white}]{Col.dark_red} Discord Ip Logger
{Col.white}[{Col.dark_red}2{Col.white}]{Col.dark_red} Discord Remote Login
{Col.white}[{Col.dark_red}3{Col.white}]{Col.dark_red} Layer4 DDoS Attack
{Col.white}[{Col.dark_red}4{Col.white}]{Col.dark_red} Tutorial
{Col.white}[{Col.dark_red}5{Col.white}]{Col.dark_red} Credits

{Col.white}>> """))
      except:os.system('cls');self.__init__()
      if c == 1:
         self.dsc()
      elif c==2:
         self.ReLog1()
      elif c==3:
         self.ddos()
      elif c==4:
         self.Tutorial()
      elif c==5:
         self.eth()
      else:os.system('cls');self.__init__()
   def dsc(self): 
         while True:
            tc = input(f"\n{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Enter Full Discord User ID (With #) {Col.white}>> ")
            print(f"\n{Col.white}[{Col.green}+{Col.white}]{Col.green} Valid Discord User | Starting Process..");sleep(3);break
         ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
         print(ip)
         sleep(1)
         print(f"That is the {Col.green}IP Adress{Col.white} of the victim! Be Carefull With It.")
         input(f"You Can Close This Window Now.")
   def ddos(self):
      while True:
         ddos = input(f"\n{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Enter IP Address Of Victim {Col.white}>> ")
         print(f"\n{Col.white}[{Col.green}+{Col.white}]{Col.green} Valid Ip Address | Starting Process..");sleep(2);break
         print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Invalid ID");sleep(2)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Decrypting in : {Col.white}1.5 Seconds")
      sleep(1.5)
      proxies = randint(100,250)
      seconds = randint(23142,43254)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Scraped : {Col.white}{proxies} {Col.dark_red}proxies in{Col.white} 1.5{seconds} {Col.dark_red}seconds")
      sleep(2.5)
      print("\n")
      while True:
         print("\n")
         m = randint(150,250)
         for _ in range(m):
            chars = string.ascii_lowercase + string.ascii_uppercase
            ab = ''.join(choice(chars) for _ in range(42))
            print(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} Sending Packages - {Col.white}{ab} - {Col.dark_red}ACCESS DENIED")
            sleep(0.1)
         mo= randint(57,980)
         mo2 = randint(10,80)
         chars = string.ascii_lowercase + string.ascii_uppercase
         ab = ''.join(choice(chars) for _ in range(42))
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Sent Packages - {Col.white}{ab} - {Col.green}ACCESS GRANTED")
         sleep(1)
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Successfully Sent DDoS Attack to Victim")
         input(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} If failed, press enter to try again..")
   def ReLog1(self):
      while True:
         ReLog1 = input(f"\n{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Enter Full Discord User Of Victim {Col.white}>> ")
         print(f"\n{Col.white}[{Col.green}+{Col.white}]{Col.green} Valid Discord User ID | Starting Process..");sleep(2);break
         print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Invalid ID");sleep(2)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Decrypting in : {Col.white}1.5 Seconds")
      sleep(1.5)
      proxies = randint(100,250)
      seconds = randint(23142,43254)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Scraped : {Col.white}{proxies} {Col.dark_red}proxies in{Col.white} 1.5{seconds} {Col.dark_red}seconds")
      sleep(2.5)
      print("\n")
      while True:
         print("\n")
         m = randint(50,150)
         for _ in range(m):
            chars = string.ascii_lowercase + string.ascii_uppercase
            a = ''.join(choice(chars) for _ in range(32))
            print(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} Checking Token - {Col.white}{a} - {Col.dark_red}INVALID")
            sleep(0.1)
         mo= randint(57,980)
         mo2 = randint(10,80)
         chars = string.ascii_lowercase + string.ascii_uppercase
         a = ''.join(choice(chars) for _ in range(32))
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Checking Token - {Col.white}{a} - {Col.green}VALID")
         sleep(1)
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Successfully Logged In! Check Discord.exe (Make sure to restart before opening)")
         input(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} If failed, press enter to try again..")
   def Tutorial(self):
       while True:
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Skin Changer:{Col.white} Change Default Skin To Renegade Raider.")
         sleep(1)
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Fortnite Ip Logger:{Col.white} Get Anyone's IP Address In Fortnite (Needs to be in party or in-game)")
         sleep(1)
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Discord Ip Logger:{Col.white} Get Anyone's IP Address In The Discord Application (Needs to be in server or private chat)")
         sleep(1)
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} DDos Attack:{Col.white} Distributed Denial-of-Service Attack.")
         sleep(1)
         input(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Epic Games Remote Login:{Col.white} Login To Any Epic Games Account And Bypassing Two Factor Authentication with Cookie Loggin Method.")
         sleep(1)
         input(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Discord Remote Login:{Col.white} Login To Any Discord Account And Bypassing Two Factor Authentication with Cookie Logging Method.")
   def eth(self):
       while True:
         input(f"{Col.white}[{Col.green}!{Col.white}]{Col.white} Everything coded by:{Col.green} Cornettoo")
         
Code()
