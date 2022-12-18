int_var = 500
float_var = 50.9
string_var_text = 'Hello world'
string_var_num = '123.2'
bool_var = True
none_type = None

# int() - integer
# float() - float
# str () - string
# bool () - boolean

print(string_var_text + str(int_var))
print(string_var_text + str(float_var))
print(string_var_text + str(bool_var))

print(int_var)
print(float(int_var))

print(float_var)
print(int(float_var))

print(type(float(string_var_num)))
print(type(int(float(string_var_num))))
print((int(float(string_var_num))))

print(bool(int_var))
print(bool(string_var_text))
print(str(none_type))
# print(int(none_type))  # mistake

print(string_var_text + str(int_var))
print(string_var_text, int_var, None, True, 102020.323232)

print(float_var + float(string_var_num))
print(str(float_var) + string_var_num)













