import matplotlib.pyplot as plt
import numpy as np

# Definir parâmetros para cálculo do VPL (Valor Presente Líquido)
taxa_desconto = 0.10  # Taxa de desconto de 10%
fluxos_caixa = np.array([-46.5, 14.37, 17.91936, 21.503232, 20.10656, 20.10656, 20.10656])  # Fluxos de caixa do projeto ao longo de 7 anos
anos = np.arange(0, len(fluxos_caixa))

# Calcular o VPL acumulado ao longo do tempo
vpl_acumulado = np.cumsum(fluxos_caixa / (1 + taxa_desconto) ** anos)

# Criar o gráfico de VPL acumulado
plt.figure(figsize=(10, 6))

# Plotar a linha de VPL acumulado
plt.plot(anos, vpl_acumulado, linestyle='--', marker='o', color='green', label='VPL Acumulado (R$ milhões)')

# Adicionar linha de break-even (VPL = 0)
plt.axvline(x=3.24, color='gray', linestyle='--', label='Break-even point (3,24 anos)')

# Adicionar rótulos e título
plt.title('VPL Acumulado ao Longo do Tempo (7 anos) - Tupi Finance S/A\n', fontsize=18)
plt.xlabel('Tempo (anos)', fontsize=16)
plt.ylabel('VPL Acumulado (R$ milhões)', fontsize=16)

# Anotar os valores de VPL em cada ponto
for i, txt in enumerate(vpl_acumulado):
    plt.annotate(f'{txt:.2f}', (anos[i], vpl_acumulado[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Adicionar legendas e exibir o gráfico
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
