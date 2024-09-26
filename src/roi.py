import matplotlib.pyplot as plt
import numpy as np

# Expandir os dados para 7 anos
anos = np.array([0, 1, 2, 3, 3.24, 4, 5, 6, 7])
roi_percentual = np.array([-100, -69.1, -30.6, -15.7, 0, 15.7, 30, 45, 58.9])  # ROI ajustado até o 7º ano

# Criar o gráfico de ROI em porcentagem ao longo de 7 anos
plt.figure(figsize=(10, 6))

# Plotar a linha de ROI percentual ao longo do tempo
plt.plot(anos, roi_percentual, linestyle='--', marker='o', color='black', label='ROI (%)')

# Adicionar uma linha para o ponto de break-even
plt.axvline(x=3.24, color='red', linestyle='--', label='Break-even point (3,24 anos)')

# Marcar o ponto exato de break-even
plt.scatter([3.24], [0], color='red', s=100, edgecolor='black', zorder=5)

# Adicionar rótulos e título
plt.title('Retorno sobre Investimento (%) ao longo do tempo (7 anos) - Tupi Finance S/A\n', fontsize=20)
plt.xlabel('Tempo (anos)', fontsize=16)
plt.ylabel('ROI (%)', fontsize=16)

# Anotar os valores de ROI em cada ponto
for i, txt in enumerate(roi_percentual):
    plt.annotate(f'{txt:.1f}%', (anos[i], roi_percentual[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Adicionar legendas e exibir o gráfico
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
