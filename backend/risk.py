# Explainable risk engine
def calculate_risk(verification, indicators):
    score = 0
    if verification.get("turnover") == "MISMATCH":
        score += 40
    if indicators.get("relationship"):
        score += 25
    if indicators.get("price_similarity"):
        score += 20
    if indicators.get("document_similarity"):
        score += 15
    return min(score, 100)
