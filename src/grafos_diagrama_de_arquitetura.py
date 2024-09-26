from pyvis.network import Network
import networkx as nx

# Criar o grafo para o diagrama de contêineres da TFSA
G = nx.DiGraph()

# Adicionar os nós (containers da arquitetura)
G.add_node("Cliente")
G.add_node("Front-end (Mobile/Web)")
G.add_node("API Gateway")
G.add_node("Back-end Services")
G.add_node("Banco de Dados Relacional")
G.add_node("Banco de Dados Não Relacional")
G.add_node("Customer Management")
G.add_node("Account Management")
G.add_node("Money Movement Management")
G.add_node("Payment Management")
G.add_node("Risk Management")
G.add_node("Salesforce (CRM)")
G.add_node("Tecban (External Provider)")
G.add_node("BACEN (Regulatory)")

# Adicionar as conexões (fluxo de dados)
G.add_edges_from([
    ("Cliente", "Front-end (Mobile/Web)"),
    ("Front-end (Mobile/Web)", "API Gateway"),
    ("API Gateway", "Back-end Services"),
    ("Back-end Services", "Customer Management"),
    ("Back-end Services", "Account Management"),
    ("Back-end Services", "Money Movement Management"),
    ("Back-end Services", "Payment Management"),
    ("Back-end Services", "Risk Management"),
    ("Back-end Services", "Banco de Dados Relacional"),
    ("Back-end Services", "Banco de Dados Não Relacional"),
    ("Back-end Services", "Salesforce (CRM)"),
    ("Money Movement Management", "Tecban (External Provider)"),
    ("Risk Management", "BACEN (Regulatory)")
])

# Criar um objeto Network
net = Network(height="750px", width="100%", directed=True)

# Carregar o grafo de networkx
net.from_nx(G)

# Configurações adicionais (opcional)
net.toggle_physics(True)  # Ativa movimentação física dos nós

# Salvar e mostrar o gráfico interativo
net.show("tfsa_container_diagram.html")
