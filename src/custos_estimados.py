import matplotlib.pyplot as plt

# Dados atualizados de custo estimado com base no arquivo business_case.md
categorias = [
    'Desenvolvimento\n(Contratação Direta)', 
    'Desenvolvimento\n(Fábrica de Software)', 
    'Aquisição de Tecnologia e\nInfraestrutura (GCP)', 
    'Licenciamentos e\nSuporte Técnico\npara PaaS e SaaS', 
    'Treinamento e Adaptação\nOrganizacional', 
    'Marketing e Lançamento'
]

custos = [6.378, 8.622, 6.000, 20.000, 1.500, 4.000]  # Valores em milhões de R$

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(categorias, custos, color='lightgreen')

# Adicionar títulos e rótulos
ax.set_title('Distribuição dos custos estimados do projeto por categoria', fontsize=16)
ax.set_xlabel('Custo em milhões de R$', fontsize=14)
ax.set_ylabel('Categorias', fontsize=14)

# Exibir o gráfico de barras
plt.grid(True)
plt.show()
