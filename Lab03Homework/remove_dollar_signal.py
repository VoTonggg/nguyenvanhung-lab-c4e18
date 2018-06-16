def remove_dollar_sign(s):
    s = s.replace("$", "")
    return s

no_dollar_string = remove_dollar_sign("$vot$$$$$$ong$")
print(no_dollar_string)