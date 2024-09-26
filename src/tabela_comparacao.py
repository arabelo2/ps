import matplotlib.pyplot as plt
import pandas as pd

# Dados para o gráfico de comparação make-or-buy
data = {
    "Critério": ["Custo Inicial", "Tempo de Implementação", "Escalabilidade", "Controle"],
    "Make": ["Alto", "Longo (6-12 meses)", "Alta, mas com custo", "Total controle"],
    "Buy (Startup)": ["Moderado", "Rápido (3-6 meses)", "Alta", "Menor controle"],
    "Plataformas como Serviço": ["Baixo", "Muito Rápido (1-2 meses)", "Alta", "Dependente de terceiros"]
}

# Criar um DataFrame
df = pd.DataFrame(data)

# Exibir a tabela
print(df)

# Gráfico para linha do tempo do plano de implementação
fig, ax = plt.subplots(figsize=(10, 6))

# Fases do plano de implementação e seus tempos
fases = ["Desenvolvimento", "Testes", "Lançamento Piloto", "Lançamento Completo"]
tempos = [2, 4, 5, 6]

# Criar gráfico de linha do tempo
ax.plot(tempos, fases, marker='o', linestyle='-', color='b')

# Adicionar títulos e rótulos
ax.set_title('Plano de Implementação - Linha do Tempo')
ax.set_xlabel('Meses')
ax.set_ylabel('Fases')

plt.grid(True)

# Exibir o gráfico
plt.show()
