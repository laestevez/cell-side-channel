import socket
import time
import sys

TCP_IP = 'your ip address'
TCP_PORT = 5005
BUFFER_SIZE = 1024
pin = sys.argv[1]

timestamp = time.strftime("%H%M%S")
FILENAME = f"./{pin}/{pin}_{timestamp}"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
print("Starting server...")
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)

# Set a timeout of 10 seconds
conn.settimeout(10)

# Open file for writing
fp = open(FILENAME, "w")
fp.write(f"{pin}\n")

while True:
    try:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        print("received data:", data.decode())
        fp.write(data.decode())
    except socket.timeout:
        print("Socket timed out, closing connection")
        break
    
# Close file
fp.close()
conn.close()
