Runtime : Python3

Prerequisite :
    pip install requests

Usage :
    python3 main.py

Description :
    TCP socket would be created at 0.0.0.0:8000 waiting for connection
    try 'telnet localhost 8000'
    protocol:
        tel <message>       # sending line notification to token holder
        heartbeat           # get heartbeat
        exit                # terminate connection