from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def get_content(self):
        with open("html_sky/index.html", encoding='utf-8') as file:
            self.info = file.read()
            return self.info

    def do_GET(self):
        content = self.get_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    webServer.server_close()
    print("Server stopped.")
