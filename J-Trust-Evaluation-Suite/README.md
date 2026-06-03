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
├── README.md                      # This documentation
├── contracts/
│   └── IJTrustInterfaces.sol      # Smart contract public interfaces (ABIs)
├── raw_data/
│   ├── deepjiandu_sample_metadata.json # Sampled metadata based on CIDOC CRM
│   ├── fig3_time_consumption.csv  # Cryptographic micro-benchmark logs
│   ├── fig4_comm_overhead.csv     # Network communication overhead logs
│   ├── fig5_verification.csv      # Consensus nodes vs verification time logs
│   ├── fig6_decryption.csv        # Policy attributes vs CP-ABE decryption logs
│   ├── fig7_throughput.csv        # Macro-system throughput (TPS) logs
│   ├── fig8_latency.csv           # Macro-system processing latency logs
│   ├── fig9_stacked_area.csv      # Dual-chain synergy batch logs
│   ├── fig10_radar.csv            # Multi-dimensional capability evaluation
│   ├── fig11_zkp_overhead.csv     # ZKP prover/verifier computational logs
│   └── table4_smart_contract_gas_profiler.csv  # Native EVM/FISCO BCOS Gas consumption logs for Table 4
└── benchmarks/
    ├── fisco_bcos_load_tester.py  # Prototype of the asynchronous RPC load tester
    └── reproduce_figures.py       # Data-driven plotting script (Parses CSV to Figures)
```

## 🚀How to Reproduce the Figures
We strictly avoid using inline hardcoded arrays for our performance evaluation. All figures (Fig 3 to Fig 11) in the manuscript are generated dynamically by parsing the raw CLI-style logs located in the raw_data/ directory.

## Prerequisites
Ensure you have Python 3.8+ installed along with the required data science libraries:

Bash
pip install pandas numpy matplotlib

## Execution
Navigate to the benchmarks/ directory and run the reproduction script:

Bash
cd benchmarks
python reproduce_figures.py

## Output
The script will utilize a custom load_cli_csv function to clean the terminal tags (e.g., [INFO], [DEBUG]) from the raw data files, extract the dataframes, and render the academic charts.

All generated figures will be automatically saved in high-quality formats (PNG, PDF, and EPS) in a newly created generated_figures/ directory. Notably, the macro-system throughput and latency charts (Fig 7 & Fig 8) will be plotted with explicit Standard Deviation Error Bars to demonstrate the network jitter observed during physical cluster testing.

## 📜 Dataset Provenance
The payload data used for the RPC stress testing in this evaluation suite was sampled from the DeepJiandu Dataset (https://doi.org/10.57760/sciencedb.08560). The metadata structure strictly complies with the international CIDOC CRM ontology standards for cultural heritage interoperability.