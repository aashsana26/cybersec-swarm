import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def _safe_generate(prompt: str, model_name: str = "gemini-1.5-pro", max_tokens: int = 300, temperature: float = 0.3):
    try:
        model = genai.GenerativeModel(model_name)
        resp = model.generate_content(prompt, max_output_tokens=max_tokens)
        return getattr(resp, "text", str(resp))
    except Exception:
        return "SIMULATED-ATTACK: 1) Probe exposed admin endpoint 2) Leverage weak password to escalate 3) Exfiltrate data. Feasibility: 6/10."
        # returning some text for sample, but we'll add @tools from langchain to actually implement the actions

def attacker_agent(state: dict) -> dict:

    target = state.get("target", "target.example.com")
    logs = state.get("logs", [])

    context = "\n".join(logs[-6:]) if logs else "(no context)"

    prompt = (
        "You are an attacker simulator. Given the following context from defender/predictor logs, "
        "write 3 concise exploit steps an attacker might try (bullet list), and give a feasibility score 0-10.\n\n"
        f"Context:\n{context}\n\n"
        "Return plain text."
    )

    attack_text = _safe_generate(prompt, model_name="gemini-1.5-pro", max_tokens=300, temperature=0.3)

    logs.append(f"[Attacker] Simulated attack for {target}: {attack_text}")

    return {"target": target, "logs": logs, "attack_summary": attack_text}