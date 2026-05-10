# GotiHub Gemma Reasoning Service 🧠🛡️

The intelligence layer for the GotiHub-AGL ecosystem. This service acts as a sovereign sidecar that handles complex Agentic Reasoning using Google's **Gemma 4**, ensuring that all institutional actions are audited by AI before being committed to the **Midnight Network**.

## 🚀 The Role in the Ecosystem
In a "Sovereign Governance" model, business logic remains in Laravel, while specialized reasoning is offloaded to this service. It provides a **Transparency Trail** of the AI's internal logic, which is then verified via Zero-Knowledge (ZK) circuits.

## 🛠️ Tech Stack
- **Framework:** FastAPI (Asynchronous Python 3.11+)
- **LLM Engine:** Gemma 4 (via Ollama/vLLM)
- **Validation:** Pydantic v2
- **Protocol:** RESTful API with JSON-based Reasoning Schema

## 🏗️ Architecture: Multi-Agent Pipeline
This service doesn't just return a boolean. It runs a **Chain of Verification (CoV)**:
1. **Structural Agent:** Validates the DNA sequence format.
2. **Compliance Agent:** Checks historical batch integrity.
3. **Consensus Agent:** Finalizes the decision for ZK-locking.

## 🚦 Getting Started

### Prerequisites
- Python 3.11+
- Local LLM Runner (Ollama recommended)

### Installation
```bash
git clone [https://github.com/apurba-labs/gemma-reasoning-service.git](https://github.com/apurba-labs/gemma-reasoning-service.git)
cd gemma-reasoning-service
pip install -r requirements.txt