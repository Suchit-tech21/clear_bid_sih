# ClearBid backend entry point
from tender import extract_requirements
from verification import verify_bid
from risk import calculate_risk
from fraud import detect_indicators
from audit import log_action

def evaluate_bid(tender, bidder):
    requirements = extract_requirements(tender)
    verification = verify_bid(bidder, requirements)
    indicators = detect_indicators(bidder)
    risk = calculate_risk(verification, indicators)
    log_action("SYSTEM", f"Evaluated {bidder['name']}")
    return {
        "requirements": requirements,
        "verification": verification,
        "indicators": indicators,
        "risk": risk
    }

# Later this function can be connected to FastAPI.
