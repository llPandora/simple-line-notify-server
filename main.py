import requests
import socket

if __name__ == '__main__':

    line_token = 'UawjDRkARXD9k49XaSlEIe3iOwpieifdApbjo3wtrI1'

    TCP_IP = '0.0.0.0'
    TCP_PORT = 8000
    BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    while(1):
        print('waiting for connection')
        conn, addr = s.accept()

        try:
            while (1):
                data = conn.recv(BUFFER_SIZE).decode('utf-8')
                print(data)
                if data.startswith('tel '):
                    # specify headers & parameters
                    headers = {'Authorization': 'Bearer ' + line_token}
                    params = {'message': data[4:]}

                    # send request
                    r = requests.post('https://notify-api.line.me/api/notify', params=params, headers=headers)

                    # notify response
                    conn.send("status code : {}\n".format(r.status_code).encode('utf-8'))

                if data.startswith('exit'):
                    break
                if data.startswith('heartbeat'):
                    conn.send('1'.encode('utf-8'))

        finally:
            conn.close()



#curl -X POST -H 'Authorization: Bearer UawjDRkARXD9k49XaSlEIe3iOwpieifdApbjo3wtrI1' -F 'message=foobar' https://notify-api.line.me/api/notify