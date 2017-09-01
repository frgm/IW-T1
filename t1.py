import socket
import os.path
import json

def Main():
    host = "127.0.0.1"
    port = 9100
     
    sk = socket.socket()
    sk.bind((host,port))     
    sk.listen(1)
    conn, addr = sk.accept()
    httpOK = "HTTP/1.1 200 OK\nX-RequestEcho: "
    httpNF = "HTTP/1.1 404 Not Found"

    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            if "HTTP/1.1" not in data:
                    break
            print ("Conectado:\n" + str(data))
            datas = data.strip().splitlines()
            get = datas[0].split(' ')
            #no existe break
            headers = {}
            for d in datas[1:]:
                d1,d2 = d.split(': ')
                headers[d1] = d2
            res = {}
            res['path'] = get[1]
            res['protocol'] = get[2]
            res['method'] = get[0]
            res['headers'] = headers
            res = json.dumps(res)
            try:
                arc = open(os.path.dirname(os.path.realpath(__file__)) + get[1],'r')
            except IOError:
                conn.send(httpNF.encode())
                conn.close()
                exit()
            retorno = httpOK + res + '\n\n' + arc.read()
            conn.send(retorno.encode())
            conn.close()
            exit()
     
if __name__ == '__main__':
    Main()
    
    