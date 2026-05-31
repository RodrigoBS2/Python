import serial
import time

# Configuration
# On Linux, ports are usually /dev/ttyUSB0 or /dev/ttyACM0
SERIAL_PORT = '/dev/ttyUSB0' 
BAUD_RATE = 9600
TIMEOUT = 1 # Seconds to wait for data

try:
    # Initialize serial connection
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT) as ser:
        print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
        
        while True:
            # Check if there are bytes waiting in the input buffer
            if ser.in_waiting > 0:
                # Read all available bytes
                data = ser.read(ser.in_waiting)
                
                # 'data' is a bytes object
                print(f"Received (hex): {data.hex()}")
                print(f"Received (raw): {data}")
            
            time.sleep(0.1) # Small delay to reduce CPU usage

except serial.SerialException as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nProgram stopped by user.")