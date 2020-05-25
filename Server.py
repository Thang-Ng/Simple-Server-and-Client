import sys
import os
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

class MyHandler(BaseHTTPRequestHandler):
    def set_response(self):
        self.send_response(200)
        self.send_header('Content_type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print("------------------------------")
        self.set_response()
        print(self.headers)
        print("------------------------------")
        with open(os.path.join(sys.path[0], "docs/GET.html")) as f:
            response = f.read()
        self.wfile.write(response.encode())
        return
    
    def do_POST(self):
        print("------------------------------")
        self.set_response()
        print(self.headers)
        content_length = int(self.headers.get('Content-length'))
        req_body = self.rfile.read(content_length)
        print("Request body:\n", req_body)
        print("------------------------------")

        #response being sent back to client
        msg = "<!DOCTYPE html>"\
                "<html>"\
                    "<head>"\
                        '<meta http-equiv="Content-Type" content="text/html;charset=utf-8">'\
                        '<title>POST request</title>'\
                    '</head>'\
                    '<body>'\
                        '<h1>Hi there</h1>'\
                        '<p>You have sent me a POST request</p>'
        msg = msg + "<p>Data: " + req_body.decode() + "</p>" + "</body></html>"
        self.wfile.write(msg.encode())
        return

    def do_PUT(self):
        print("------------------------------")
        self.set_response()
        print(self.headers)
        content_length = int(self.headers.get('Content-length'))
        req_body = self.rfile.read(content_length)
        print("Request body:\n", req_body)
        print("------------------------------")

        #response being sent back to client
        msg = '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
                <title>POST request</title>
            </head>
            <body>
                <h1>Hi there</h1>
                <p>You have sent me a PUT request</p>
            </body>
        </html>'''
        self.wfile.write(msg.encode())
        return
    
    def do_HEAD(self):
        self.set_response()

    def do_DELETE(self):
        print("------------------------------")
        self.set_response()
        print(self.headers)
        content_length = int(self.headers.get('Content-length'))
        req_body = self.rfile.read(content_length)
        print("Request body:\n", req_body)
        print("------------------------------")

        #response being sent back to client
        msg = '''
        <!DOCTYPE html/>
        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
                <title>POST request</title>
            </head>
            <body>
                <h1>Hi there</h1>
                <p>You have sent me a DELETE request</p>
            </body>
        </html>'''
        self.wfile.write(msg.encode())
        return
              
def main():
    print("Use admin/admin to login")
    user = input("Username: ")
    pwd = input("Password: ")

    while user != "admin" or pwd != "admin":
        print("Invalid username and password\n")
        user = input("Username: ")
        pwd = input("Password: ")

    try:
        server = HTTPServer(('', PORT_NUMBER), MyHandler)
        print("Server is running on port", PORT_NUMBER)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

if __name__ == "__main__":
    main()