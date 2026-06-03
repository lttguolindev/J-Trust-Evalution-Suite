import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# 创建输出目录（如果不存在）
os.makedirs('generated_figures', exist_ok=True)

# Load data, skipping the informational headers
data = pd.read_csv('../raw_data/table5_ablation_study.csv', skiprows=4)

variants = data['Variant'].str.replace('_', ' ')
tps_mean = data['TPS_Mean']
tps_std = data['TPS_Std']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(variants, tps_mean, yerr=tps_std, capsize=5, color=['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B3'])

ax.set_ylabel('System Throughput (TPS)')
ax.set_title('Ablation Study: Throughput Evaluation across Architecture Variants')
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('generated_figures/Fig_Ablation_TPS.png', dpi=300)
print("[SUCCESS] Ablation bar chart generated at generated_figures/Fig_Ablation_TPS.png")