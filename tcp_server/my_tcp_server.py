import socket

TCP_IP = 'your ip address'
TCP_PORT = 5005
BUFFER_SIZE = 1024
FILENAME = "./filepath"

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

while True:
    try:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        #print("received data:", data.decode())
        fp.write(data.decode())
    except socket.timeout:
        print("Socket timed out, closing connection")
        break
    
# Close file
fp.close()
conn.close()
