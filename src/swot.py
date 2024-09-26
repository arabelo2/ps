import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Definir os textos da análise SWOT
swot_text = {
    "Forças": "Tecnologia avançada e escalável\n\nExperiência superior do usuário\n\nParcerias estratégicas com líderes de mercado",
    "Fraquezas": "Complexidade na integração de sistemas legados\n\nRecursos orçamentários limitados\n\nPrazo agressivo de lançamento\n\nDependência de fornecedores externos\n\nProcessos internos de procurement (lento)",
    "Oportunidades": "Crescimento do mercado de fintech\n\nRegulamentações favoráveis para operações digitais",
    "Ameaças": "Concorrência intensa de grandes players\n\nRiscos crescentes de segurança cibernética"
}

# Criar a figura e os eixos
fig, ax = plt.subplots(figsize=(8, 6))

# Definir os blocos de cores para cada quadrante
colors = {
    "Forças": 'skyblue', 
    "Fraquezas": 'orange', 
    "Oportunidades": 'lightgreen', 
    "Ameaças": 'lightcoral'
}

# Desenhar os blocos de cada seção
ax.add_patch(Rectangle((0, 0.5), 0.5, 0.5, color=colors["Forças"], ec="black"))
ax.add_patch(Rectangle((0.5, 0.5), 0.5, 0.5, color=colors["Fraquezas"], ec="black"))
ax.add_patch(Rectangle((0, 0), 0.5, 0.5, color=colors["Oportunidades"], ec="black"))
ax.add_patch(Rectangle((0.5, 0), 0.5, 0.5, color=colors["Ameaças"], ec="black"))

# Adicionar os textos para cada seção
ax.text(0.25, 0.75, "FORÇAS\n\n" + swot_text["Forças"], ha='center', va='center', fontsize=12, color="black", weight="normal")
ax.text(0.75, 0.75, "FRAQUEZAS\n\n" + swot_text["Fraquezas"], ha='center', va='center', fontsize=12, color="black", weight="normal")
ax.text(0.25, 0.25, "OPORTUNIDADES\n\n" + swot_text["Oportunidades"], ha='center', va='center', fontsize=12, color="black", weight="normal")
ax.text(0.75, 0.25, "AMEAÇAS\n\n" + swot_text["Ameaças"], ha='center', va='center', fontsize=12, color="black", weight="normal")

# Remover os eixos
ax.set_xticks([])
ax.set_yticks([])

# Título
plt.title("Análise SWOT - Tupi Finance S/A\n", fontsize=18, weight="bold")

# Mostrar o gráfico
plt.show()
