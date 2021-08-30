from datetime import date


MONTH = {'january': 1,
         'february': 2,
         'march': 3,
         'april': 4,
         'may': 5,
         'june': 6,
         'july': 7,
         'august': 8,
         'september': 9,
         'october': 10,
         'november': 11,
         'december': 12
        }
def check_coupon(entered_code: str, correct_code: str, current_date: str, expiration_date: str) -> bool:    
    if entered_code is correct_code:
        current_date = current_date.replace(',', '')
        expiration_date = expiration_date.replace(',', '')
        formatted_current = [MONTH.get(i.lower()) if i.lower() in MONTH.keys() else int(i) for i in current_date.split()]
        formatted_expiration = [MONTH.get(i.lower()) if i.lower() in MONTH.keys() else int(i) for i in expiration_date.split()]
        to_date_current = date(formatted_current[2], formatted_current[0], formatted_current[1])
        to_date_formatted_expiration = date(formatted_expiration[2], formatted_expiration[0], formatted_expiration[1])
        if to_date_current <= to_date_formatted_expiration:
            return True
        return False        
    return False
