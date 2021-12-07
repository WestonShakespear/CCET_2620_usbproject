import serial
import time

class hubtools:
    def __init__(self, port, baudrate):
        self.comm = serial.Serial(port=port, baudrate=baudrate, timeout=0.1)

    def poll(self):
        cur = self.comm.read().decode()

        self.comm.flushOutput()
        self.comm.flushInput()
        if cur == '':
            return 0
        d = self.fetchResponse(cur)

        return d

    def fetchResponse(self, first_char=''):
        while True:
            data = first_char
            timeout = 0

            while True:
                d = self.comm.read().decode()

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

    def sendChar(self, char):
        c = 0
        while True:
            print("sending")
            self.comm.write(bytes(char, 'utf-8'))
            time.sleep(0.1)
            d = self.fetchResponse()
            if d != "err":
                break
            c += 1
            if c >= 3:
                self.comm.flushOutput()
                self.comm.flushInput()
                d = "err"
                break
        return d
