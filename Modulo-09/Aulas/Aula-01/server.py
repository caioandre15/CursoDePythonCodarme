from http.server import HTTPServer, BaseHTTPRequestHandler

# Criando uma classe que herda de BaseHTTPRequestHandler e implementa o metódo Get
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200) # Define o retorno do servidor como 200
        self.send_header("Content-Type", "text/html; charset=UTF-8")
        self.send_header("Teste", "abc") # Adiciona um cabeçalho
        self.end_headers() # Informa que não existem mais cabeçahos
        data = f"""
        <html>
            <head>
                <title>Olá, Mundo!</title>
            </head>
            <body>
                <p>Testando nosso servidor HTTP!</p>
                <p>Diretório: {self.path}</p>
            </body>
        </html>
        """.encode()
        self.wfile.write(data)

        # self.wfile.write("Olá, mundo!".encode()) # Retorna uma mensagem para o cliente
        # encode() Converte a string para binário
        # data = f""" Atalho para escrever um bloco
# Contrutor por default espera receber o endereço e a porta.
# BaseHTTPRequestHandler tem a missão de receber as requisições
server = HTTPServer(('localhost', 8000), SimpleHandler)
server.serve_forever() # Faz com que o servidor fique ativo aguardando uma requisição

