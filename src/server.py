#!/usr/bin/env python3
"""
Model Context Protocol (MCP) Server for Context Engineering & Evaluation
Implements JSON-RPC 2.0 interface compliant with Anthropic & Google Antigravity MCP specification.
"""

import sys
import json
from src.evaluator import ContextEvaluator

evaluator = ContextEvaluator()

TOOLS = [
    {
        "name": "compress_prompt_context",
        "description": "Prunes conversational filler and optimizes KV-cache footprint while maintaining semantic fidelity.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Raw uncompressed prompt payload"}
            },
            "required": ["text"]
        }
    },
    {
        "name": "audit_prompt_injection",
        "description": "Performs security audit against prompt injection, system leaks and delimiter breakouts (OWASP LLM01).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string", "description": "Candidate prompt to inspect"}
            },
            "required": ["prompt"]
        }
    },
    {
        "name": "verify_evidence_first",
        "description": "Enforces Evidence-First verification gate: validates execution output against deterministic assertions.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "execution_output": {"type": "string", "description": "Terminal or test output"},
                "expected_assertion": {"type": "string", "description": "Expected validation key"}
            },
            "required": ["execution_output", "expected_assertion"]
        }
    }
]

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")

    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS}}

    elif method == "tools/call":
        params = req.get("params", {})
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "compress_prompt_context":
            res = evaluator.compress_context(args.get("text", ""))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}

        elif name == "audit_prompt_injection":
            res = evaluator.audit_security(args.get("prompt", ""))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}

        elif name == "verify_evidence_first":
            passed = evaluator.verify_assertion(args.get("execution_output", ""), args.get("expected_assertion", ""))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"passed": passed}, indent=2)}]}}

        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}

    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "q1-context-eval-mcp", "version": "1.0.0"}
            }
        }
    return None

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            if res:
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
