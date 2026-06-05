from solution import valid_date

# Examples from docstring
assert valid_date('03-11-2000') == True
assert valid_date('15-01-2012') == False
assert valid_date('04-0-2040') == False
assert valid_date('06-04-2020') == True
assert valid_date('06/04/2020') == False

# Extra cases from specification
assert valid_date('') == False
assert valid_date('01-01-2000') == True
assert valid_date('02-29-2000') == True
assert valid_date('02-30-2000') == False
assert valid_date('04-30-2000') == True
assert valid_date('04-31-2000') == False
assert valid_date('05-31-2000') == True
assert valid_date('12-31-2000') == True
assert valid_date('13-01-2000') == False
assert valid_date('00-01-2000') == False
assert valid_date('01-00-2000') == False
assert valid_date('01-32-2000') == False
assert valid_date('01-1-2000') == False
assert valid_date('1-01-2000') == False
assert valid_date('01-01-200') == False
assert valid_date('01-01-20000') == False
