import serial
import time
import serial.rs485

# Configure the serial port
ser = serial.Serial(
    port="/dev/ttyS0", 
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)
# Enable RS485 mode
# ser.rs485 = serial.rs485.RS485Settings()
try:
    i=0
    while True:

        print(i)
        # Send data01 05 00 00 FF 00 CRC
        ser.write(b'01')
        ser.write(b'05')
        ser.write(b'00')
        ser.write(b'00')
        ser.write(b'FF')
        ser.write(b'00')
        ser.write(b'CRC')
        print(b'Hello, RS232!')
        ser.flush()  # Ensure all data is transmitted
        # Read data
        data = ser.readline().decode('utf-8').strip()
        if data:
            print(f"Received: {data}")

        time.sleep(1)
        i+=1

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")
