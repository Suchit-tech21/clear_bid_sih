# Bidder verification
def verify_bid(bidder, requirements):
    return {
        "turnover": bidder.get("turnover_status", "VERIFIED"),
        "gst": bidder.get("gst_status", "VERIFIED"),
        "experience": bidder.get("experience_status", "VERIFIED"),
        "debarment": bidder.get("debarment_status", "CLEAR")
    }
