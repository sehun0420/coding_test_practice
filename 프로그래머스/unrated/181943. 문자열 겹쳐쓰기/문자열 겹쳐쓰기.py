def solution(my_string, overwrite_string, s):
    a = s + len(overwrite_string)
    result = my_string[:s] + overwrite_string[:] + my_string[a:]
    return result