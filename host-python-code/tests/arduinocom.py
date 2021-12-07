import serial
import time

port = '/dev/ttyACM1'

comm = serial.Serial(port=port, baudrate=115200, timeout=1)
comm.flushOutput()
comm.flushInput()

def write_read(x, max_tries):
    c = 0
    while True:
        print("sending")


        comm.write(bytes(x, 'utf-8'))
        time.sleep(0.1)
        d = getAns()
        if d != "err":
            break
        c += 1
        if c >= max_tries:
            d = "err"
            break


    # time.sleep(0.05)
    return d



def getAns():

    while True:
        data = ""
        timeout = 0

        while True:
            d = comm.read().decode()

            if d != '':
                data += d
            if d == '\n':
                break

            if d == '':
                timeout += 1
            if timeout > 10:
                data = 'err  '
                break
        if len(data) != 2:
            break

    return data[:-2]

while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num, 3)
    print(value) # printing the value

# while True:
#     cur = comm.read().decode()
#     if cur == '':
#         continue
#     d = cur + getAns()
#     print(d)

# a = 0
# while True:
#     time.sleep(1
