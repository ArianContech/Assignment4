InputNumber = input("Please Enter an integer number: ")

try:
    intNum = int(InputNumber)
except ValueError:
    print("Unpeacefully converted to integer !")	
else:
    print(f"input number is integer : " , intNum ) 