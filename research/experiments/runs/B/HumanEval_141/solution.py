def file_name_check(file_name):
    # Check if there's exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Split by dot
    name_part, ext_part = file_name.split('.')
    
    # Check if name part is not empty
    if not name_part:
        return 'No'
    
    # Check if name part starts with a letter
    if not name_part[0].isalpha():
        return 'No'
    
    # Check if extension is valid
    if ext_part not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # Count digits in the entire file name
    digit_count = sum(1 for c in file_name if c.isdigit())
    if digit_count > 3:
        return 'No'
    
    return 'Yes'
