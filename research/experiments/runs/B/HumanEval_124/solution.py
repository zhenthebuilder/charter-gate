def valid_date(date):
    # Rule 1: Check if date is not empty
    if not date:
        return False
    
    # Rule 4: Check format mm-dd-yyyy
    parts = date.split('-')
    if len(parts) != 3:
        return False
    
    month_str, day_str, year_str = parts
    
    # Check that each part has the right length and is numeric
    if len(month_str) != 2 or not month_str.isdigit():
        return False
    if len(day_str) != 2 or not day_str.isdigit():
        return False
    if len(year_str) != 4 or not year_str.isdigit():
        return False
    
    month = int(month_str)
    day = int(day_str)
    year = int(year_str)
    
    # Rule 3: Check month is 1-12
    if month < 1 or month > 12:
        return False
    
    # Rule 2: Check day based on month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:  # month == 2
        max_days = 29
    
    if day < 1 or day > max_days:
        return False
    
    return True
