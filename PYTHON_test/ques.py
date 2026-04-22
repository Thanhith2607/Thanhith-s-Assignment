def calculate_ticket_price(seats, timing, is_weekend):

    
    prices = {
        "VIP": 500,
        "REGULAR": 300,
        "ECONOMY": 150
    }

    
    timing_mult = {
        "morning": 0.8,
        "afternoon": 1,
        "evening": 1.2,
        "night": 1.5
    }

    
    valid_seats = [s for s in seats if s in prices]

    if not valid_seats:
        return "No valid booking"

    
    base_total = sum(prices[s] for s in valid_seats)

    
    after_timing = base_total * timing_mult.get(timing, 1)

    
    if is_weekend:
        after_weekend = after_timing * 1.10
    else:
        after_weekend = after_timing

    
    discount = 0
    if len(valid_seats) >= 5:
        discount = after_weekend * 0.15
        after_discount = after_weekend - discount
    else:
        after_discount = after_weekend

    
    booking_fee = 50 * len(valid_seats)
    after_fee = after_discount + booking_fee

    
    tax = after_fee * 0.12

    
    final_amount = round(after_fee + tax)

    return {
        "base_total": round(base_total),
        "timing_adjustment": round(after_timing),
        "discount": round(discount),
        "tax": round(tax),
        "final_amount": final_amount
    }

seats = ["VIP", "REGULAR", "VIP"]
timing = "evening"
is_weekend = True

print(calculate_ticket_price(seats, timing, is_weekend))