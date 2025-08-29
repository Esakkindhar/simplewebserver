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