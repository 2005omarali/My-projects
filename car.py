age = int(input("how old are you?\n:"))
licence = input("do you have driver licence(yes , no )?\n:")
if age >=18 and licence == "yes":
    print("you can drive acar")
elif age<18 or licence != "yes":
    print ("sorry , you cant drive acar")