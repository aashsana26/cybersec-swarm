import os
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def _safe_generate(prompt: str, model_name: str = "gemini-1.5-pro", max_tokens: int = 300, temperature: float = 0.0):
    try:
        model = genai.GenerativeModel(model_name)
        resp = model.generate_content(prompt, max_output_tokens=max_tokens)
        return getattr(resp, "text", str(resp))
    except Exception:
        return "REMEDIATION-FALLBACK: 1) Patch the dependency 2) Add rate limiting 3) Block offending IPs and enforce MFA 4) Harden admin endpoints."
        # returning some text for sample, but we'll add @tools from langchain to actually implement the actions

def defender_agent(state: dict) -> dict:
    target = state.get("target", "target.example.com")
    logs = state.get("logs", [])

    context = "\n".join(logs[-8:]) if logs else "(no context)"

    prompt = (
        "You are a defensive security engineer. Given this context (attacker simulation + predictions), "
        "list 4 prioritized mitigations (short bullets) and a short remediation plan.\n\n"
        f"Context:\n{context}\n\n"
        "Return plain text."
    )

    defense_text = _safe_generate(prompt, model_name="gemini-1.5-pro", max_tokens=300, temperature=0.0)

    logs.append(f"[Defender] Defense plan for {target}: {defense_text}")

    return {"target": target, "logs": logs}


agents / ar