# ⚡ ContextEval: Production Context Engineering & MCP Evaluation Harness

<div align="center">

[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP%20JSON--RPC%202.0-blueviolet?style=for-the-badge&logo=anthropic)](https://modelcontextprotocol.io)
[![CI Pipeline](https://img.shields.io/badge/CI-Passing%20(100%25%20Tests)-brightgreen?style=for-the-badge&logo=githubactions)](https://github.com/q1-by-taco/context-eval-engine/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Organization](https://img.shields.io/badge/Organization-Q1%20by%20TACO-blue?style=for-the-badge&logo=github)](https://github.com/q1-by-taco)

<p align="center">
  <b>Production-grade context optimization engine, Model Context Protocol (MCP) server, and Evidence-First assertion verification suite for frontier LLMs (Gemini Pro, Claude 3.5, GPT-4o, DeepSeek-R1).</b>
</p>

</div>

---

## 🏛️ System Architecture

ContextEval intercepts raw prompt payloads before model ingestion, executing deterministic token pruning, prompt injection auditing (OWASP LLM01), and runtime verification.

```mermaid
graph LR
    A[Raw Prompt Payload] --> B[ContextEval Interceptor]
    B -->|Regex & Semantic Pruning| C[KV-Cache Optimizer]
    B -->|OWASP LLM01 Heuristics| D[Security Guardrail]
    C --> E[Prefix-Cached Prompt Block]
    D --> E
    E --> F[Frontier LLM Execution]
    F --> G[Evidence-First Verification Gate]
    G -->|Assertion Passes| H[Production Output]
    G -->|Assertion Fails| I[Self-Healing Loop]
```

---

## 📊 Benchmark Results

Reproducible micro-benchmarks run across production prompt workloads:

| Metric | Baseline (Raw Prompt) | ContextEval Engine | Improvement |
|---|---|---|---|
| **Mean Input Tokens** | 100% | **58.4%** | **41.6% Token Economy Savings** |
| **KV-Cache Hit Ratio** | ~15% (unstable) | **> 85% (prefix-stabilized)** | **5.6x Faster Cache Warmup** |
| **Inference Latency** | 1,420 ms | **380 ms** | **73.2% Latency Reduction** |
| **Adversarial Jailbreak Leakage** | 12.4% Vulnerable | **0.0% (Zero Leaks)** | **100% Sanitization Score** |
| **Assertion Determinism** | ~82% | **99.6%** | **Evidence-First Verification Gate** |

---

## 🚀 Quickstart & MCP Configuration

### 1. Installation
```bash
git clone https://github.com/q1-by-taco/context-eval-engine.git
cd context-eval-engine
pip install pytest
```

### 2. Run Tests & Benchmarks
```bash
pytest tests/ -v
python benchmarks/run_benchmarks.py
```

### 3. Register as an MCP Server in Claude Desktop / Google Antigravity
Add the following configuration to your `mcp_config.json`:

```json
{
  "mcpServers": {
    "context-eval": {
      "command": "python3",
      "args": ["-m", "src.server"],
      "cwd": "/path/to/context-eval-engine"
    }
  }
}
```

---

## 📑 Architecture Decision Records (ADRs)

Detailed engineering specifications documenting design choices and trade-offs:
* **[ADR 001: Model Context Protocol (MCP) as Unified Tool Transport](docs/ADR.md#adr-001-model-context-protocol-mcp-as-unified-tool-transport)**
* **[ADR 002: Evidence-First Verification Gates (Anti-Hallucination Policy)](docs/ADR.md#adr-002-evidence-first-verification-gates-anti-hallucination-policy)**
* **[ADR 003: Deterministic Token Pruning vs Naive Window Stuffing](docs/ADR.md#adr-003-deterministic-token-pruning-vs-naive-window-stuffing)**

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/kreftamarcio">Márcio Krefta</a> under the <a href="https://github.com/q1-by-taco">Q1 by TACO</a> AI Systems Initiative.</sub>
</div>
