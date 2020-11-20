from http.server import HTTPServer, CGIHTTPRequestHandler

serveradress = ("", 80)
server = HTTPServer(serveradress, CGIHTTPRequestHandler)

server.serve_forever()