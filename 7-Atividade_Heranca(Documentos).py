class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}"

class Email(Documento):
    def __init__(self, titulo, conteudo, remetente, destinatario):
        super().__init__(titulo, conteudo)
        self.remetente = remetente
        self.destinatario = destinatario

    def exibir(self):
        doc_info = super().exibir()
        return f"{doc_info}, Remetente: {self.remetente}, Destinatário: {self.destinatario}"

class Relatorio(Documento):
    def __init__(self, titulo, conteudo, data):
        super().__init__(titulo, conteudo)
        self.data = data

    def exibir(self):
        doc_info = super().exibir()
        return f"{doc_info}, Data: {self.data}"

documento_xxx = Documento("Documento XXX", "Este é um documento de XXX.")
print(documento_xxx.exibir())

email = Email("Conteudo Confidencial", "Proibido em 142 paises", "tad-remetente@gmail.com", "tad-destinatario@gmail.com")
print(email.exibir())

relatorio = Relatorio("Relatório", "Conteudo +18", "22/08/2023")
print(relatorio.exibir())