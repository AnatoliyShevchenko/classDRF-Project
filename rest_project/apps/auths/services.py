SYMBOLS = '(@$^.,:;!_*-+()/#¤%&)'

def check_symbols_in_password(password):
    i: str
    symbols_count: int = 0
    numbers_count: int = 0
    str_count: int = 0
    for i in password:
        if i in SYMBOLS:
            symbols_count += 1
        elif i.isdigit():
            numbers_count += 1
        elif i.isalpha():
            str_count += 1

    if symbols_count > 0 and numbers_count > 0 and str_count > 0:
        return True
    
    return False
        