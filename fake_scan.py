import random
import datetime

# CHATGPT fake scan module to generate a fake report

# Fake list of issues -> this would be generated from an actual scan
COMMON_ISSUES = [
    ("Open port 22 (SSH)", 7),
    ("Open port 80 (HTTP)", 5),
    ("Open port 443 (HTTPS)", 3),
    ("Publicly exposed admin endpoint /admin", 8),
    ("Outdated dependency: Flask 1.1.2", 6),
    ("Weak password policy (min length < 6)", 7),
    ("Missing rate limiting on login endpoint", 8),
    ("CORS misconfiguration", 4),
    ("Directory listing enabled", 5),
    ("Unvalidated file upload endpoint", 9),
]

def simulate_security_scan(system_name="target.example.com"):
    issues = []
    weights = [w for (string, w) in COMMON_ISSUES]
    chosen = random.choices(COMMON_ISSUES, weights=weights, k=random.randint(2, 4))
    for title, score in chosen:
        issues.append({
            "title": title,
            "confidence": round(random.uniform(0.6, 0.97), 2),
            "risk": score
        })
    risk_score = sum(i["risk"] for i in issues) // len(issues)
    return {
        "system": system_name,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "issues": issues,
        "risk_score": int(risk_score)
    }


# Sample dictionary of the fake_scan output for my reference
# {
#   "system": "target.example.com",
#   "timestamp": "2025-11-02T14:32:18.456789Z",
#   "issues": [
#     {
#       "title": "Outdated SSL/TLS Protocol",
#       "confidence": 0.89,
#       "risk": 7
#     },
#     {
#       "title": "Missing Security Headers",
#       "confidence": 0.74,
#       "risk": 5
#     },
#     {
#       "title": "Weak Password Policy",
#       "confidence": 0.92,
#       "risk": 8
#     }
#   ],
#   "risk_score": 6
# }