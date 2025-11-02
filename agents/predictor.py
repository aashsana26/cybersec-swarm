import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def _safe_generate(prompt: str, model_name: str = "gemini-1.5-pro", max_tokens: int = 300, temperature: float = 0.2):
    try:
        model = genai.GenerativeModel(model_name)
        resp = model.generate_content(prompt, max_output_tokens=max_tokens)
        # .text is the recommended field
        return getattr(resp, "text", str(resp))
    except Exception as e:
        # fallback deterministic text (safe: no LLM call)
        return "PREDICTION-FALLBACK: Based on the observed issues, a plausible near-term issue is chained privilege escalation via exposed admin endpoint."

# I'm using observer_agent's fake scan to "predict" future events here
def predictor_agent(observation: dict):
    # observation -> fake scan dict

    # get only the importnt part s of the observation in this format
    # \n Title (Risk, Confidence)
    issues_text = "\n".join([f"- {i['title']} (risk {i['risk']}, conf {i['confidence']})" for i in observation.get("issues", [])])

    prompt = (
        "You are a security forecaster. Based on the following current issues, "
        "predict 1-2 plausible near-future vulnerabilities or attack paths that could emerge.\n\n"
        f"Current issues for {observation.get('system')}:\n{issues_text}\n\n"
        "Return a JSON with keys: 'predicted_issues' (list of short strings) and 'rationale' (short)."
    )

    text = _safe_generate(prompt, model_name="gemini-1.5-pro", max_tokens=300, temperature=0.2)

    return {
        "observation": observation,
        "prediction_text": text
    }
