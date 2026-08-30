# Fraud/anomaly indicators
# Indicators support investigation; they do not prove fraud.
def detect_indicators(bidder):
    return {
        "relationship": bidder.get("relationship_flag", False),
        "price_similarity": bidder.get("price_similarity", False),
        "document_similarity": bidder.get("document_similarity", False)
    }
