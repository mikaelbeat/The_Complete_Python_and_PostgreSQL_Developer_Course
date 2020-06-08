
class My_custom_error(ValueError):
    pass


value1 = 9

if value1 < 10:
    raise My_custom_error("This is my custom error!")