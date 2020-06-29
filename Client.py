#thang.ngn@outlook.com
import urllib3
import argparse
import json

class Request:
    #split the data string in order to send to server
    @classmethod
    def splitData(cls, data):
        arr = data.split("&")
        result = []
        for element in arr:
            temp = element.split("=")
            result.append(temp[0])
            result.append(temp[1])

        #make result become a dictionary instead of list
        result = {result[i] : result[i + 1] for i in range(0, len(result), 2)}
        return result 

    @classmethod
    def send_request_without_data(cls, method, address):
        http = urllib3.PoolManager()
        req = http.request(method, address)
        #print the response from server
        print("RESPONSE HEADER:")
        for key in req.headers:
            print(key, ":", req.headers[key])
        
        print("\nRESPONSE BODY:")
        print(req.data.decode())

    @classmethod
    def send_request_with_data(cls, method, data, address):
        http = urllib3.PoolManager()
        data = cls.splitData(data)
        
        #body is the encoded data
        req = http.request(method, address, headers={'Content-Type': 'application/json'}, body=json.dumps(data))
        #print the response from server
        print("RESPONSE HEADER:")
        for key in req.headers:
            print(key, ":", req.headers[key])

        print("\nRESPONSE BODY:")
        print(req.data.decode())



def main():
    #create a parser object
    parser = argparse.ArgumentParser(description="Make a request to server")

    #create arguments (command line arguments)
    parser.add_argument('-m', '--method', type=str, nargs=1, metavar="http method", help="Specify the HTTP method in use (GET/POST/PUT/HEAD/PATCH/DELETE). Default method is GET")
    parser.add_argument('-d', '--data', type=str, nargs=1, metavar="data to send", help="Specify data which is sent to server with POST/PATCH")
    parser.add_argument('-a', '--address', type=str, nargs=1, metavar="address", help="Address of the destination")

    # parse the arguments from standard input 
    args = parser.parse_args()

    if args.method == None or args.address == None:
        print("Method and address can not be empty")
        exit(1)
    elif args.data != None and args.method[0] != "POST" and args.method[0] != "post" and args.method[0] != "PATCH" and args.method[0] != "patch":
        print(args.method)
        print("Data can only be used with POST or PATCH")
        exit(1)
    
    if args.data != None:
        Request.send_request_with_data(args.method[0], args.data[0], args.address[0])
    else:
        Request.send_request_without_data(args.method[0], args.address[0])
    
if __name__ == "__main__":
    main()
