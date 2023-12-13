class Despesa:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

class Orcamento:
    def __init__(self, valor_inicial):
        self.valor_inicial = valor_inicial
        self.despesas = []

    def adicionar_despesa(self, despesa):
        self.despesas.append(despesa)
        print(f"Despesa '{despesa.descricao}' de R${despesa.valor:.2f} adicionada.")

    def calcular_saldo(self):
        total_despesas = sum(despesa.valor for despesa in self.despesas)
        saldo = self.valor_inicial - total_despesas
        return saldo

class Participante:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class MidiaSocial:
    def __init__(self, nome, link):
        self.nome = nome
        self.link = link

    def promover_evento(self, evento):
        mensagem = f"Participe do evento '{evento.nome}' em {evento.data_hora} no {evento.local}. #EventosTech #PythonConference"
        print(f"Promovendo o evento '{evento.nome}' nas redes sociais ({self.nome}): {mensagem}")

    def interagir_com_participantes(self, participante):
        mensagem = f"Obrigado por participar, {participante.nome}! Esperamos que tenha aproveitado o evento. #Feedback #EventoTech"
        print(f"Enviando mensagem para {participante.nome} nas redes sociais ({self.nome}): {mensagem}")

class Pesquisa:
    def __init__(self, pergunta):
        self.pergunta = pergunta
        self.respostas = {"Ótimo": 0, "Bom": 0, "Ruim": 0}

    def realizar_pesquisa(self):
        print(self.pergunta)
        print("Digite 1 se o evento foi ótimo.")
        print("Digite 2 se o evento foi bom.")
        print("Digite 3 se o evento foi ruim.")
       
        while True:
            resposta = input("Escolha uma opção: ")
            if resposta in ("1", "2", "3"):
                if resposta == "1":
                    self.respostas["Ótimo"] += 1
                elif resposta == "2":
                    self.respostas["Bom"] += 1
                elif resposta == "3":
                    self.respostas["Ruim"] += 1
                break
            else:
                print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

        print("Obrigado por avaliar o evento!")

class Evento:
    def __init__(self, nome, data_hora, local, descricao, orcamento_inicial):
        self.nome = nome
        self.data_hora = data_hora
        self.local = local
        self.descricao = descricao
        self.participantes = []
        self.agenda = {}
        self.palestrantes = []
        self.artistas = []
        self.fornecedores = []
        self.pesquisas = []  # Adicionado o atributo para armazenar pesquisas
        self.orcamento = Orcamento(orcamento_inicial)
        self.redes_sociais = []

    def adicionar_participante(self, nome, email, telefone):
        participante = Participante(nome, email, telefone)
        self.participantes.append(participante)
        print(f"Participante '{participante.nome}' adicionado ao evento '{self.nome}'.")

    def adicionar_despesa_evento(self, descricao, valor):
        despesa = Despesa(descricao, valor)
        self.orcamento.adicionar_despesa(despesa)

    def adicionar_midia_social(self, nome, link):
        midia_social = MidiaSocial(nome, link)
        self.redes_sociais.append(midia_social)
        print(f"Adicionada integração com {midia_social.nome} para o evento '{self.nome}'.")

    def adicionar_pesquisa(self, pergunta):
        pesquisa = Pesquisa(pergunta)
        self.pesquisas.append(pesquisa)
        print(f"Pesquisa adicionada ao evento '{self.nome}': {pergunta}")

    def promover_evento_nas_redes_sociais(self):
        for midia_social in self.redes_sociais:
            midia_social.promover_evento(self)

    def interagir_com_participantes_nas_redes_sociais(self):
        for participante in self.participantes:
            for midia_social in self.redes_sociais:
                midia_social.interagir_com_participantes(participante)

    def realizar_pesquisas(self):
        if not self.pesquisas:
            print("Não há pesquisas disponíveis para este evento.")
            return

        for pesquisa in self.pesquisas:
            pesquisa.realizar_pesquisa()

# Receber inputs do usuário para criar um evento
nome_evento = input("Digite o nome do evento: ")
data_hora_evento = input("Digite a data e hora do evento (formato: YYYY-MM-DD HH:MM): ")
local_evento = input("Digite o local do evento: ")
descricao_evento = input("Digite a descrição do evento: ")
orcamento_inicial_evento = float(input("Digite o orçamento inicial do evento:"))

# Criar uma instância do evento
evento1 = Evento(nome_evento, data_hora_evento, local_evento, descricao_evento, orcamento_inicial_evento)

# Adicionar participantes ao evento
quantidade_participantes = int(input("Digite a quantidade de participantes a serem registrados: "))
for _ in range(quantidade_participantes):
    nome_participante = input("Digite o nome do participante: ")
    email_participante = input("Digite o e-mail do participante: ")
    telefone_participante = input("Digite o telefone do participante: ")
    evento1.adicionar_participante(nome_participante, email_participante, telefone_participante)

# Adicionar despesas ao evento
quantidade_despesas = int(input("Digite a quantidade de despesas a serem adicionadas: "))
for _ in range(quantidade_despesas):
    descricao_despesa = input("Digite a descrição da despesa: ")
    valor_despesa = float(input("Digite o valor da despesa: "))
    evento1.adicionar_despesa_evento(descricao_despesa, valor_despesa)

# Adicionar plataformas de mídia social ao evento
quantidade_midias_sociais = int(input("Digite a quantidade de plataformas de mídia social a serem adicionadas: "))
for _ in range(quantidade_midias_sociais):
    nome_midia_social = input("Digite o nome da plataforma de mídia social: ")
    link_midia_social = input("Digite o link da plataforma de mídia social: ")
    evento1.adicionar_midia_social(nome_midia_social, link_midia_social)

# Adicionar pesquisas ao evento
evento1.adicionar_pesquisa("Como você avalia o evento?")

# Promover evento nas redes sociais
evento1.promover_evento_nas_redes_sociais()

# Interagir com participantes nas redes sociais
evento1.interagir_com_participantes_nas_redes_sociais()

# Realizar pesquisas
evento1.realizar_pesquisas()