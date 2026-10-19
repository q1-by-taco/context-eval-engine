# Architecture Decision Records (ADR)

## ADR 001: Model Context Protocol (MCP) as Unified Tool Transport

### Status
Accepted

### Context
In 2025/2026, autonomous agent frameworks fragmented across proprietary SDK interfaces (LangChain, LlamaIndex, OpenAI Assistants, Anthropic Tool Use). This led to severe vendor lock-in, duplicate tool definitions, and brittle schema adaptations.

### Decision
Adopt the **Model Context Protocol (MCP)** specification (JSON-RPC 2.0 over standard I/O and SSE) as the sole tool transport layer for ContextEval.

### Consequences
* **Positive:** Complete cross-compatibility across Google Antigravity, Claude Code, Cursor, and custom agent harnesses.
* **Positive:** Strict capability negotiation and sandboxed tool execution.
* **Negative:** Minor serialization overhead (~0.05ms) compared to native in-memory Python function pointers.

---

## ADR 002: Evidence-First Verification Gates (Anti-Hallucination Policy)

### Status
Accepted

### Context
Frontier models frequently suffer from "confident hallucination"—asserting that a software bug is resolved or a system is functioning without execution proof.

### Decision
Mandate the **Verification Before Completion** standard. An agent cannot transition to the `COMPLETED` state without passing an automated verification assertion (unit test output, exit code 0, or AST validation hash).

### Consequences
* **Positive:** Eliminates false-positive completions in autonomous coding pipelines.
* **Negative:** Requires environment access and test execution runtime for validation.

---

## ADR 003: Deterministic Token Pruning vs Naive Window Stuffing

### Status
Accepted

### Context
Long-context windows (1M–2M tokens in Gemini 1.5/2.0) lead to sloppy context stuffing, increasing inference latency by 300% and inflating operational costs.

### Decision
Implement deterministic regex and semantic pruning of conversational boilerplate before context ingestion. Preserve immutable prefix blocks to maximize provider-side KV-cache hit rates.

### Consequences
* **Positive:** Up to 45% reduction in input token costs and 80% latency decrease via prompt caching.
* **Negative:** Edge cases where informal user language contains subtle domain nuances must be guarded with fallback thresholds.
