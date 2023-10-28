import os # part-1
os.system("pkg install cmatrix")
os.system("clear")
os.system("pkg install nano")
os.system("pkg install figlet")
os.system("pkg install ruby")
os.system("pkg install gem")
os.system("gem install lolcat")
os.system("clear")

#- part-4
def system():
    print ("")
    os.system("figlet cmatrix |lolcat")
    print ("")
    print ("\033[1;31m[1] \033[1;32mgreen")
    print ("\033[1;31m[2] \033[1;32mred")
    print ("\033[1;31m[3] \033[1;32mblue")
    print ("\033[1;31m[4] \033[1;32mcyan")
    print ("\033[1;31m[5] \033[1;32myellow")
    print ("\033[1;31m[6] \033[1;32mmagenta")
    print ("\033[1;31m[7] \033[1;32mexit")
    print ("")
    x=int(input("\033[1;31m[*] \033[1;33mEnter Your Tool Number \033[1;31m》》:\033[1;34m"))
    if x==1:
       os.system("cmatrix -C green")
    elif x==2:
         os.system("cmatrix -C red")
    elif x==3:
         os.system("cmatrix -C blue")
    elif x==4:
         os.system("cmatrix -C cyan")
    elif x==5:
         os.system("cmatrix -C yellow")
    elif x==6:
         os.system("cmatrix -C magenta")
    elif x==7:
         os.system("clear")
    else:
      print ("Too not fund ..!")
# part-2
def main():
    os.system("figlet cmatrix |lolcat")
    print ("\033[1;37m________________________________")
    print ("\033[1;31m   Tool by-:")
    print ("\033[1;36m       Termux hacking")
    print ("\033[1;37m________________________________")
    print ("\033[1;31m[1] \033[1;32mStart ")
    print ("\033[1;31m[2] \033[1;32mupdate")
    print ("\033[1;31m[3] \033[1;32mhelp  ")
    print ("\033[1;31m[4] \033[1;32mexit  ")
    print ("") # part-3
    x=int(input("\033[1;31m[*] \033[1;33mEnter Your Tool Number \033[1;31m》》:\033[1;34m "))
    if x==1:
       os.system("clear")
       system()
    elif x==2:
         os.system("figlet update |lolcat")
         os.system("pkg updete && pkg upgrate")
    elif x==3:
         os.system("figlet help |lolcat")
         os.system(" ")
    elif x==4:
         os.system("clear")
    else:
       print ("\033[1;31m[•] Tool not fund..!")
main()
