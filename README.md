# Simple-Server-and-Client

## Server

Run ```py Server.py``` to start the server. Enter ```admin/admin``` in order to log in.

## Client

usage: Client.py [-h] [-m http method] [-d data to send] [-a address]

Make a request to server

optional arguments:

  -h, --help            show this help message and exit
  
  -m http method, --method http method
  
   Specify the HTTP method in use (GET/POST/PUT/HEAD/PATCH/DELETE). Default method is GET
   
  -d data to send, --data data to send
  
  Specify data which is sent to server with POST/PATCH
  
  -a address, --address address
  
                        Address of the destination
