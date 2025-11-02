import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def _safe_generate(prompt: str, model_name: str = "gemini-1.5-pro", max_tokens: int = 300, temperature: float = 0.2):
    try:
        model = genai.GenerativeModel(model_name)
        resp = model.generate_content(prompt, max_output_tokens=max_tokens)

        return getattr(resp, "text", str(resp))
    except Exception as e:
        return "PREDICTION-FALLBACK: Based on the observed issues, a plausible near-term issue is chained privilege escalation via exposed admin endpoint."

# I'm using observer_agent's fake scan to "predict" future events here
def predictor_agent(state: dict):
    # observation -> fake scan dict

    logs = state.get("logs", [])
    target = state.get("target", "")

    recent_context = "\n".join(logs[-6:]) if logs else "(no logs available)"
    prompt = (
        "You are a security forecaster. Based on the following recent observation logs, "
        "predict 1-2 plausible near-future vulnerabilities or attack paths that could emerge.\n\n"
        f"Recent logs:\n{recent_context}\n\n"
        "Return a short plain-text prediction (1-2 bullets) and a one-sentence rationale."
    )

    prediction_text = _safe_generate(prompt, model_name="gemini-1.5-pro", max_tokens=250, temperature=0.2)

    # Append prediction to logs
    logs.append(f"[Predictor] Prediction for {target}: {prediction_text}")

    return {"target": target, "logs": logs}
