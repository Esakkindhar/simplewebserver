# EX01 Developing a Simple Webserver
## Date: 
 01\09\2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:

from http.server import HTTPServer, BaseHTTPRequestHandler


content='''
<!DOCTYPE html>
<head>
    <title>Experiment 1</title>
</head>
<body>
    <table border="1" align="center" cellpadding="15" cellspacing="1">
        <caption><h1>List of Protocols in TCP/IP Protocol Suite</h1></caption>
        <tr bgcolor="blue" style="font-size:larger;">
            <th>Layer</th>
            <th>Responsibilties</th>
            <th>Protocols</th>
        </tr>
        <tr style="font-size:large;">
            <td>Application</td>
            <td>User-facing tasks like browsing, email, or file transfers</td>
            <td>HTTP, FTP, SMTP, DNS</td>
        </tr>
        <tr style="font-size:large;">
            <td>Transport</td>
            <td>End-to-end communication, error checking, and flow control</td>
            <td>TCP, UDP</td>
        </tr>
        <tr style="font-size:large;">
            <td>Network</td>
            <td>Routing and forwarding of packets across networks</td>
            <td>IP, ICMP, OSPF</td>
        </tr>
        <tr style="font-size:large;">
            <td>Data Link</td>
            <td>Node-to-node data transfer and error detection</td>
            <td>Ethernet, PPP, Switches</td>
        </tr>
        <tr style="font-size:large;">
            <td>Physical</td>
            <td>Transmission of raw bitstreams over physical media</td>
            <td>Cables, Hubs, Repeaters</td>
        </tr>
    </table>
</body>
</html>
'''
class myhandler (BaseHTTPRequestHandler):
     def do_GET(self):
        print("request received") 
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',5000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

## OUTPUT:
c:\Users\admin\OneDrive\Pictures\Screenshots\Screenshot 2025-08-29 063929.png

## RESULT:
The program for implementing simple webserver is executed successfully.
