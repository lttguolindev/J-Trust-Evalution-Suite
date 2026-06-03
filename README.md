# J-Trust: Evaluation and Benchmarking Suite

This repository contains the evaluation suite, raw empirical logs, and smart contract interfaces for the paper: **"J-Trust: A Trustworthy and Accountable Governance Scheme for Jiandu Digital Resources with Fine-Grained Access Control"**.

## 🔒 Security & Code Availability Statement

To strictly adhere to operational security protocols for public-facing cultural heritage infrastructures, the full production-grade source code of the J-Trust core logic (including specific Zero-Knowledge Proof circuits and full threshold signature aggregation implementations) is withheld. This restriction is enforced to prevent potential zero-day vulnerabilities and protect the integrity of the heritage data. Access to the core implementation may be granted to qualified academic researchers upon reasonable request to the corresponding author and the execution of a Non-Disclosure Agreement (NDA).

However, to ensure **100% empirical reproducibility and academic transparency**, this repository provides:
1. **Raw Experimental Logs:** The authentic CLI terminal output dumps generated during our localized MacBook Pro M3 cluster benchmarking process (using customized FISCO BCOS).
2. **Data-Driven Evaluation Scripts:** Python scripts that parse the raw CSV logs to regenerate every performance figure presented in the manuscript.
3. **Smart Contract Interfaces (ABIs):** Demonstrating the dual-chain data structures and architectural interactions.
4. **Load Testing Prototypes:** Demonstrating how concurrent RPC requests were formulated and dispatched to the cluster.

---

## 📂 Repository Structure

```text
J-Trust-Evaluation-Suite/
├── README.md                                   # This documentation
├── contracts/
│   └── IJTrustInterfaces.sol                   # Smart contract public interfaces (ABIs)
├── zkp_circuits/
│   └── CrossChainSync.circom                   # Reference R1CS circuit configuration (Groth16/BN254)
├── benchmarks/
│   ├── fisco_bcos_load_tester.py               # Prototype of the asynchronous RPC load tester
│   ├── reproduce_figures.py                    # Data-driven plotting script (Fig 3 - Fig 11)
│   └── plot_ablation.py                        # Script to generate Ablation Study throughput charts
└── raw_data/
    ├── deepjiandu_sample_metadata.json         # Sampled metadata strictly compliant with CIDOC CRM
    ├── table4_smart_contract_gas_profiler.csv  # Native EVM/FISCO BCOS Gas consumption logs
    ├── table5_ablation_study.csv               # Raw logs validating the multi-dimensional ablation study
    ├── fig3_time_consumption.csv               # Cryptographic micro-benchmark logs
    ├── fig4_comm_overhead.csv                  # Network communication overhead logs
    ├── fig5_verification.csv                   # Consensus nodes vs verification time logs
    ├── fig6_decryption.csv                     # Policy attributes vs CP-ABE decryption logs
    ├── fig7_throughput.csv                     # Macro-system throughput (TPS) logs
    ├── fig8_latency.csv                        # Macro-system processing latency logs
    ├── fig9_stacked_area.csv                   # Dual-chain synergy batch logs
    ├── fig10_radar.csv                         # Multi-dimensional capability evaluation
    └── fig11_zkp_overhead.csv                  # ZKP prover/verifier computational logs

```

## 🚀How to Reproduce the Figures
We strictly avoid using inline hardcoded arrays for our performance evaluation. All figures (Fig 3 to Fig 11) in the manuscript are generated dynamically by parsing the raw CLI-style logs located in the raw_data/ directory.

## Prerequisites
Ensure you have Python 3.8+ installed along with the required data science libraries:

### Bash
pip install pandas numpy matplotlib

## Execution
Navigate to the benchmarks/ directory and run the reproduction script:

### Bash
cd benchmarks

# 1. Reproduce Main Manuscript Figures (Fig 3 to Fig 11)
python reproduce_figures.py

# 2. Reproduce Ablation Study Results (Table 5 & Extended Charts)
python plot_ablation.py

## Output & Methodology
The plotting scripts utilize a custom load_cli_csv function to automatically clean terminal tags (e.g., [INFO], [DEBUG]) and strip aligned whitespaces from the raw data files, extracting the pure dataframes.All generated figures will be automatically saved in high-quality academic formats (PNG, PDF, and EPS) in a newly created generated_figures/ directory. Notably, the macro-system throughput and the architectural ablation charts are plotted with explicit Standard Deviation ($\pm \sigma$) Error Bars to empirically demonstrate the network jitter observed during our 1,000 independent iterations of stress testing.

## 📜 Dataset Provenance & Cryptographic Standards
·Dataset: The payload data used for the RPC stress testing in this evaluation suite was sampled from the DeepJiandu Dataset (https://doi.org/10.57760/sciencedb.08560).
·Ontology: The metadata structure strictly complies with the international CIDOC CRM ontology standards (ISO 21127:2014) for cultural heritage interoperability.
·Cryptography: ZKP parameters are standardized over the BN254 (ALT_BN128) elliptic curve, maintaining EVM compatibility. The cross-chain verification strictly consumes constant $\mathcal{O}(1)$ Gas on the main chain.
