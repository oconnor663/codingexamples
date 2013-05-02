import http.server

class MyHandler(http.server.BaseHTTPRequestHandler):

  reply = "foo!"

  def do_GET(self):
    print("Got a request!")
    self.wfile.write(self.reply.encode('utf-8'))

server = http.server.HTTPServer(('localhost', 8000), MyHandler)

server.serve_forever()
