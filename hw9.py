# battleship code
print("Hello world")
#input("Enter your input:")
import msvcrt
while True:
    input_char=msvcrt.getch()
    print(int.from_bytes(input_char, "big"))

    if int.from_bytes(input_char, "big") == 72: # ascii 17
        print("UP")
    elif int.from_bytes(input_char, "big") == 80: #chr(18):
        print("DOWN")
    elif int.from_bytes(input_char, "big") == 77: #chr(19):
        print("RIGHT")
    elif int.from_bytes(input_char, "big") == 75: #chr(20):
        print("LEFT")   
    elif input_char == b' ': #chr(32):
        print("SPACE") 
    else:
        print(input_char)                    