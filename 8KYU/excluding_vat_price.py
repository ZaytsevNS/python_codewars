# Solution for task: https://www.codewars.com/kata/5890d8bc9f0f422cf200006b/

def excluding_vat_price(price):
    
    """
    This function calculates the original product price, without VAT.
    """
    
    return round(price / 1.15, 2) if price else -1
