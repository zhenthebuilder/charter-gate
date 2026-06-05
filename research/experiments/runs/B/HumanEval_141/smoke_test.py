from solution import file_name_check

# Valid cases
assert file_name_check("example.txt") == 'Yes'
assert file_name_check("test.exe") == 'Yes'
assert file_name_check("file.dll") == 'Yes'
assert file_name_check("a.txt") == 'Yes'
assert file_name_check("abc123.txt") == 'Yes'
assert file_name_check("ABC.txt") == 'Yes'
assert file_name_check("MyFile.dll") == 'Yes'
assert file_name_check("a1b2c.txt") == 'Yes'

# Invalid cases
assert file_name_check("1example.dll") == 'No'
assert file_name_check("example") == 'No'
assert file_name_check("example.txt.doc") == 'No'
assert file_name_check(".txt") == 'No'
assert file_name_check("example.doc") == 'No'
assert file_name_check("a1b2c3d4.txt") == 'No'
assert file_name_check("example.") == 'No'
assert file_name_check(".") == 'No'
assert file_name_check("_file.txt") == 'No'
assert file_name_check("-file.txt") == 'No'
assert file_name_check("aaa.TXT") == 'No'
