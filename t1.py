import socket
 
def Main():
    host = "127.0.0.1"
    port = 9100
     
    sk = socket.socket()
    sk.bind((host,port))     
    sk.listen(1)
    conn, addr = sk.accept()
    header =  "HTTP/1.1 200 OK"
    json = '{"path": "/myapp/index_3.html", "protocol": "HTTP/1.1", "method": "GET", "headers": {"Accept": "text/html", "Accept-Language": "es-ES", "Host": "localhost:9100"}}'
    
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            if "HTTP/1.1" not in data:
                    break
            print ("from connected  user: " + str(data))
             
            #data = str(data).upper()
            data = header + "TEST"
            print ("sending: " + str(data))
            conn.send(data.encode())
            conn.close()
             exit()
     
if __name__ == '__main__':
    Main()
    
    