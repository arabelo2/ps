import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import newton

# Função para calcular a TIR (Taxa Interna de Retorno)
def calcular_tir(fluxos_caixa):
    return newton(lambda r: np.sum([fc / (1 + r)**i for i, fc in enumerate(fluxos_caixa)]), 0.1)

# Fluxos de caixa do projeto (em milhões de R$)
fluxos_caixa = np.array([-46.5, 14.37, 17.91936, 21.503232, 20.10656, 20.10656, 20.10656])

# Definir a taxa de desconto para o cálculo do VPL (10%)
taxa_desconto = 0.10

# Calcular o VPL (Valor Presente Líquido)
anos = np.arange(0, len(fluxos_caixa))
vpl_acumulado = np.cumsum(fluxos_caixa / (1 + taxa_desconto) ** anos)

# Calcular a TIR (Taxa Interna de Retorno)
tir = calcular_tir(fluxos_caixa) * 100  # Multiplicando por 100 para obter o valor em porcentagem

# Criar o gráfico de VPL acumulado ao longo do tempo
plt.figure(figsize=(10, 6))

# Plotar a linha de VPL acumulado
plt.plot(anos, vpl_acumulado, linestyle='--', marker='o', color='green', label='VPL Acumulado (R$ milhões)')

# Adicionar linha de break-even (VPL = 0)
plt.axhline(0, color='gray', linestyle='--', label='Break Even')

# Adicionar rótulos e título
plt.title(f'Gráfico de VPL Acumulado - TIR: {tir:.2f}% - Tupi Finance S/A', fontsize=16)
plt.xlabel('Tempo (anos)', fontsize=12)
plt.ylabel('VPL Acumulado (R$ milhões)', fontsize=12)

# Anotar os valores de VPL em cada ponto
for i, txt in enumerate(vpl_acumulado):
    plt.annotate(f'{txt:.2f}', (anos[i], vpl_acumulado[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Adicionar legendas e exibir o gráfico
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Exibir o VPL e TIR calculados
print(f"VPL (Valor Presente Líquido): R$ {vpl_acumulado[-1]:.2f} milhões")
print(f"TIR (Taxa Interna de Retorno): {tir:.2f}%")
