import random

def get_fallback_prices():
    """Provides realistic mandi prices for 12 core crops."""
    return [
        {"commodity": "Paddy (Rice)", "modal_price": random.randint(2180, 2350), "market": "Mangaluru Mandi"},
        {"commodity": "Arecanut", "modal_price": random.randint(46000, 51000), "market": "Mangaluru Mandi"},
        {"commodity": "Coconut", "modal_price": random.randint(3200, 3900), "market": "Mysuru Mandi"},
        {"commodity": "Onion", "modal_price": random.randint(1900, 2400), "market": "Mysuru Mandi"},
        {"commodity": "Tomato", "modal_price": random.randint(1100, 1600), "market": "Hassan Mandi"},
        {"commodity": "Coffee", "modal_price": random.randint(36000, 39500), "market": "Kodagu Mandi"},
        {"commodity": "Cotton", "modal_price": random.randint(6800, 7400), "market": "Hubballi Mandi"},
        {"commodity": "Sugarcane", "modal_price": random.randint(310, 360), "market": "Mandya Mandi"},
        {"commodity": "Maize", "modal_price": random.randint(1950, 2250), "market": "Davanagere Mandi"},
        {"commodity": "Groundnut", "modal_price": random.randint(5800, 6400), "market": "Chitradurga Mandi"},
        {"commodity": "Turmeric", "modal_price": random.randint(12500, 14800), "market": "Chamarajanagar Mandi"},
        {"commodity": "Chilli (Red)", "modal_price": random.randint(19000, 24500), "market": "Byadgi Mandi"}
    ]