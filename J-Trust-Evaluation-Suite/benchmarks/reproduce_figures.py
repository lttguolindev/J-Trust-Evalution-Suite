"""
J-Trust Evaluation Suite: Figure Reproduction Script (Data-Driven Version)
This script parses RAW CLI-style experimental logs (CSV files) obtained from
the FISCO BCOS MacBook Pro cluster and generates all figures presented in the
manuscript. It ensures 100% empirical reproducibility and traceability.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import warnings

# ==========================================
# Global Academic Style Configuration
# ==========================================
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

# Font configuration for cross-platform compatibility (prevents missing glyph warnings)
try:
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
except:
    pass

# Unified Color Scheme
COLORS = {
    'JTrust': '#FF0000',      # Red - Proposed Scheme
    'Centralized': '#4E79A7', # Blue - Centralized Scheme
    'SingleChain': '#F28E2B'  # Orange - Single-Chain Scheme
}

OUTPUT_DIR = "generated_figures"
DATA_DIR = os.path.join("..", "raw_data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==========================================
# Core Parsers and Auxiliary Functions
# ==========================================
def save_fig(fig_name):
    """Save high-quality multi-format academic figures (PNG, PDF, EPS)."""
    # Temporarily disable transparency for EPS export
    original_alpha = None

    for fmt in ['png', 'pdf', 'eps']:
        if fmt == 'eps':
            # EPS does not support transparency; remove alpha channel from all artists
            for artist in plt.gcf().findobj():
                if hasattr(artist, 'set_alpha'):
                    original_alpha = artist.get_alpha()
                    artist.set_alpha(None)

        plt.savefig(os.path.join(OUTPUT_DIR, f"{fig_name}.{fmt}"),
                   format=fmt, dpi=600, bbox_inches='tight',
                   facecolor='white', edgecolor='none')

        # Restore original transparency settings
        if fmt == 'eps' and original_alpha is not None:
            for artist in plt.gcf().findobj():
                if hasattr(artist, 'set_alpha'):
                    artist.set_alpha(original_alpha)

    print(f"[+] Successfully generated: {fig_name}")

def load_cli_csv(filename):
    """
    Parses CLI-style raw benchmark logs.
    Automatically ignores terminal output tags (e.g., [INFO], [DEBUG])
    and strips aligned whitespaces to extract pure DataFrames.
    """
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        print(f"[!] Error: Missing dataset {filepath}")
        return None

    try:
        df = pd.read_csv(filepath, comment='[', skipinitialspace=True)
        df.columns = [col.strip() for col in df.columns]

        # Data validation: check if DataFrame is empty
        if df.empty:
            print(f"[!] Warning: {filename} is empty")
            return None

        return df
    except Exception as e:
        print(f"[!] Error loading {filename}: {e}")
        return None

def validate_dataframe(df, required_cols, filename):
    """Validate if the DataFrame contains the required columns."""
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        print(f"[!] Warning: {filename} missing columns: {missing_cols}")
        return False
    return True

# ==========================================
# 1. Cryptographic and Architectural Micro-Benchmarks
# ==========================================

def plot_fig3_time_consumption():
    df = load_cli_csv("fig3_time_consumption.csv")
    if df is None: return

    required_cols = ['Phase', 'Centralized', 'SingleChain', 'JTrust']
    if not validate_dataframe(df, required_cols, "fig3_time_consumption.csv"):
        return

    x = np.arange(len(df['Phase']))
    width = 0.25
    fig, ax = plt.subplots(figsize=(12, 6))

    bars1 = ax.bar(x - width, df['Centralized'], width, label='Centralized Scheme', color=COLORS['Centralized'])
    bars2 = ax.bar(x, df['SingleChain'], width, label='Single-Chain Scheme', color=COLORS['SingleChain'])
    bars3 = ax.bar(x + width, df['JTrust'], width, label='J-Trust (Ours)', color=COLORS['JTrust'])

    ax.set_ylabel('Time Consumption (ms)', fontweight='bold')
    ax.set_xlabel('Processing Phase', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(df['Phase'].str.strip(), rotation=0, ha='center')
    ax.legend(loc='upper left', frameon=True, edgecolor='black')
    ax.grid(True, axis='y', linestyle=':', alpha=0.3)

    # Add numerical value labels to bars
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    save_fig('Fig3_Time_Consumption')
    plt.close()

def plot_fig4_comm_overhead():
    df = load_cli_csv("fig4_comm_overhead.csv")
    if df is None: return

    required_cols = ['Operation', 'Centralized', 'SingleChain', 'JTrust']
    if not validate_dataframe(df, required_cols, "fig4_comm_overhead.csv"):
        return

    x = np.arange(len(df['Operation']))
    width = 0.25
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.bar(x - width, df['Centralized'], width, label='Centralized Scheme', color=COLORS['Centralized'])
    ax.bar(x, df['SingleChain'], width, label='Single-Chain Scheme', color=COLORS['SingleChain'])
    ax.bar(x + width, df['JTrust'], width, label='J-Trust (Ours)', color=COLORS['JTrust'])

    ax.set_ylabel('Communication Overhead (KB)', fontweight='bold')
    ax.set_xlabel('Operation Type', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(df['Operation'].str.strip(), rotation=0, ha='center')
    ax.legend(loc='upper left', frameon=True, edgecolor='black')
    ax.grid(True, axis='y', linestyle=':', alpha=0.3)

    plt.tight_layout()
    save_fig('Fig4_Communication_Overhead')
    plt.close()

def plot_fig5_verification():
    df = load_cli_csv("fig5_verification.csv")
    if df is None: return

    required_cols = ['Nodes', 'Centralized', 'SingleChain', 'JTrust']
    if not validate_dataframe(df, required_cols, "fig5_verification.csv"):
        return

    plt.figure(figsize=(8, 6))

    plt.plot(df['Nodes'], df['SingleChain'], linestyle='--', marker='o',
             color=COLORS['SingleChain'], label='Single-Chain Scheme',
             linewidth=2, markersize=8)
    plt.plot(df['Nodes'], df['Centralized'], linestyle='-.', marker='s',
             color=COLORS['Centralized'], label='Centralized Scheme',
             linewidth=2, markersize=8)
    plt.plot(df['Nodes'], df['JTrust'], linestyle='-', marker='*',
             color=COLORS['JTrust'], label='J-Trust (Ours)',
             linewidth=2.5, markersize=10)

    plt.xlabel('Number of Consensus Nodes', fontweight='bold')
    plt.ylabel('Verification Time (ms)', fontweight='bold')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(loc='upper left', frameon=True, edgecolor='black')
    plt.xlim(10, 50)
    plt.tight_layout()
    save_fig('Fig5_Verification_Overhead')
    plt.close()

def plot_fig6_decryption():
    df = load_cli_csv("fig6_decryption.csv")
    if df is None: return

    required_cols = ['Attributes', 'Centralized', 'SingleChain', 'JTrust']
    if not validate_dataframe(df, required_cols, "fig6_decryption.csv"):
        return

    plt.figure(figsize=(8, 6))

    plt.plot(df['Attributes'], df['SingleChain'], linestyle='--', marker='o',
             color=COLORS['SingleChain'], label='Single-Chain Scheme (No Enc)',
             linewidth=2, markersize=8)
    plt.plot(df['Attributes'], df['Centralized'], linestyle='-.', marker='s',
             color=COLORS['Centralized'], label='Centralized Scheme (AES)',
             linewidth=2, markersize=8)
    plt.plot(df['Attributes'], df['JTrust'], linestyle='-', marker='*',
             color=COLORS['JTrust'], label='J-Trust (CP-ABE)',
             linewidth=2.5, markersize=10)

    plt.xlabel('Number of User Attributes', fontweight='bold')
    plt.ylabel('Decryption Time (ms)', fontweight='bold')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(loc='upper left', frameon=True, edgecolor='black')
    plt.xlim(5, 50)
    plt.tight_layout()
    save_fig('Fig6_Decryption_Performance')
    plt.close()

# ==========================================
# 2. Macro-Performance Evaluation
# ==========================================

def plot_fig7_throughput():
    df = load_cli_csv("fig7_throughput.csv")
    if df is None: return

    required_cols = ['Concurrent_Requests', 'JTrust_TPS_Mean', 'JTrust_TPS_Std',
                    'Centralized_TPS_Mean', 'Centralized_TPS_Std',
                    'SingleChain_TPS_Mean', 'SingleChain_TPS_Std']
    if not validate_dataframe(df, required_cols, "fig7_throughput.csv"):
        return

    loads = df['Concurrent_Requests']

    plt.figure(figsize=(10, 7))

    plt.errorbar(loads, df['JTrust_TPS_Mean'], yerr=df['JTrust_TPS_Std'],
                fmt='-o', linewidth=3, color=COLORS['JTrust'],
                marker='*', markersize=10, capsize=5, capthick=2,
                label='J-Trust (Dual-Chain)', elinewidth=2)
    plt.errorbar(loads, df['Centralized_TPS_Mean'], yerr=df['Centralized_TPS_Std'],
                fmt='--s', linewidth=2, color=COLORS['Centralized'],
                marker='s', markersize=8, capsize=4,
                label='Centralized Scheme', elinewidth=2)
    plt.errorbar(loads, df['SingleChain_TPS_Mean'], yerr=df['SingleChain_TPS_Std'],
                fmt='-.^', linewidth=2, color=COLORS['SingleChain'],
                marker='^', markersize=8, capsize=4,
                label='Single-Chain Scheme', elinewidth=2)

    plt.xlabel('Number of Accessed Nodes (Requests)', fontweight='bold')
    plt.ylabel('Throughput (TPS)', fontweight='bold')
    plt.grid(True, alpha=0.3, linestyle=':')
    plt.xticks(loads, rotation=45)
    plt.yticks(range(40, 130, 10))
    plt.legend(loc='lower right', frameon=True, shadow=True)
    plt.tight_layout()
    save_fig('Fig7_Throughput_Comparison')
    plt.close()

def plot_fig8_latency():
    df = load_cli_csv("fig8_latency.csv")
    if df is None: return

    required_cols = ['Concurrent_Requests', 'JTrust_Lat_Mean', 'JTrust_Lat_Std',
                    'Centralized_Lat_Mean', 'Centralized_Lat_Std',
                    'SingleChain_Lat_Mean', 'SingleChain_Lat_Std']
    if not validate_dataframe(df, required_cols, "fig8_latency.csv"):
        return

    loads = df['Concurrent_Requests']

    plt.figure(figsize=(10, 7))

    plt.errorbar(loads, df['JTrust_Lat_Mean'], yerr=df['JTrust_Lat_Std'],
                fmt='-o', linewidth=3, color=COLORS['JTrust'],
                marker='*', markersize=10, capsize=5, capthick=2,
                label='J-Trust (Dual-Chain)', elinewidth=2)
    plt.errorbar(loads, df['Centralized_Lat_Mean'], yerr=df['Centralized_Lat_Std'],
                fmt='--s', linewidth=2, color=COLORS['Centralized'],
                marker='s', markersize=8, capsize=4,
                label='Centralized Scheme', elinewidth=2)
    plt.errorbar(loads, df['SingleChain_Lat_Mean'], yerr=df['SingleChain_Lat_Std'],
                fmt='-.^', linewidth=2, color=COLORS['SingleChain'],
                marker='^', markersize=8, capsize=4,
                label='Single-Chain Scheme', elinewidth=2)

    plt.xlabel('Number of Accessed Nodes (Requests)', fontweight='bold')
    plt.ylabel('Processing Time (ms)', fontweight='bold')
    plt.grid(True, alpha=0.3, linestyle=':')
    plt.xticks(loads, rotation=45)
    plt.yticks(range(15, 80, 10))
    plt.legend(loc='upper left', frameon=True, shadow=True)
    plt.tight_layout()
    save_fig('Fig8_Processing_Time_Comparison')
    plt.close()

# ==========================================
# 3. Architectural Synergy and Boundary Scenarios
# ==========================================

def plot_fig9_stacked_area():
    df = load_cli_csv("fig9_stacked_area.csv")
    if df is None: return

    required_cols = ['Batch', 'MainChain', 'SideChain']
    if not validate_dataframe(df, required_cols, "fig9_stacked_area.csv"):
        return

    fig, ax = plt.subplots(figsize=(10, 6))

    main_chain_color = (45/255, 110/255, 170/255)
    side_chain_color = (150/255, 195/255, 230/255)

    ax.stackplot(df['Batch'], df['MainChain'], df['SideChain'],
                 labels=['Main-chain (Rights Confirmation)', 'Side-chain (Academic Revision)'],
                 colors=[main_chain_color, side_chain_color], alpha=0.85,
                 edgecolors='black', linewidths=0.5)

    ax.set_xlabel('Transaction Batch', fontweight='bold', labelpad=10)
    ax.set_ylabel('Number of Transactions Processed', fontweight='bold', labelpad=10)

    ticks = df['Batch'].values[::max(1, len(df)//6)]
    ax.set_xticks(ticks)
    ax.set_xticklabels([f'Batch {int(x)}' for x in ticks], fontsize=10)

    legend = ax.legend(loc='upper left', fontsize=11, frameon=True,
                      framealpha=0.9, edgecolor='black')
    for text in legend.get_texts():
        text.set_fontweight('bold')

    ax.grid(True, axis='y', linestyle=':', alpha=0.3)

    plt.tight_layout()
    save_fig('Fig9_Stacked_area_chart_professional')
    plt.close()

def plot_fig10_radar():
    df = load_cli_csv("fig10_radar.csv")
    if df is None: return

    required_cols = ['Dimension', 'JTrust', 'Centralized', 'SingleChain']
    if not validate_dataframe(df, required_cols, "fig10_radar.csv"):
        return

    categories = [c.strip() for c in df['Dimension']]
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    def get_data(col):
        val = list(df[col])
        return val + val[:1]

    fig, ax = plt.subplots(figsize=(9, 7), subplot_kw=dict(projection='polar'))

    # J-Trust (Filled polygon)
    jtrust_vals = get_data('JTrust')
    ax.plot(angles, jtrust_vals, 'o-', linewidth=2.5,
            label='J-Trust (Proposed)', color=COLORS['JTrust'], markersize=8)
    ax.fill(angles, jtrust_vals, alpha=0.2, color=COLORS['JTrust'])

    # Centralized
    ax.plot(angles, get_data('Centralized'), 's-', linewidth=2,
            label='Centralized Scheme', color=COLORS['Centralized'], markersize=7)

    # SingleChain
    ax.plot(angles, get_data('SingleChain'), '^-', linewidth=2,
            label='Single-Chain Scheme', color=COLORS['SingleChain'], markersize=7)

    ax.set_xticks(angles[:-1])
    cat_labels = [c.replace(' ', '\n') for c in categories]
    ax.set_xticklabels(cat_labels, fontsize=10)
    ax.set_ylim(0, 5.5)
    ax.set_yticklabels([f'{i:.1f}' for i in range(0, 6)], fontsize=9)
    ax.grid(True, linestyle=':', alpha=0.5)

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
             ncol=3, fontsize=11, frameon=True)

    plt.tight_layout()
    save_fig('Fig10_Radar_chart_professional')
    plt.close()


# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    print("=" * 57)
    print(" J-Trust Evaluation Suite: Data-Driven Figure Generation ")
    print(" Parsing raw CLI logs from ../raw_data/ directory...     ")
    print("=" * 57)

    # Verify data directory existence
    if not os.path.exists(DATA_DIR):
        print(f"[!] Error: Data directory '{DATA_DIR}' not found!")
        print("    Please ensure the raw_data directory exists in the parent folder.")
        exit(1)

    # Generate all figures sequentially
    figures = [
        ("Fig3: Time Consumption", plot_fig3_time_consumption),
        ("Fig4: Communication Overhead", plot_fig4_comm_overhead),
        ("Fig5: Verification Overhead", plot_fig5_verification),
        ("Fig6: Decryption Performance", plot_fig6_decryption),
        ("Fig7: Throughput Comparison", plot_fig7_throughput),
        ("Fig8: Processing Time Comparison", plot_fig8_latency),
        ("Fig9: Stacked Area Chart", plot_fig9_stacked_area),
        ("Fig10: Radar Chart", plot_fig10_radar)
    ]

    for fig_name, fig_func in figures:
        print(f"\n[>] Generating {fig_name}...")
        fig_func()

    print("\n" + "=" * 57)
    print(" All figures generated successfully!                     ")
    print(f" Output directory: {os.path.abspath(OUTPUT_DIR)}")
    print(" Ready for LaTeX manuscript integration.                 ")
    print("=" * 57)