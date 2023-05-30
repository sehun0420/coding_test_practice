def solution(code):
    idx = 0
    mode = 0
    ret = ''
    for i in code:
        if i == "1":
            if mode == 1:
                mode = 0
            else:
                mode = 1
        else:
            if mode == 0:
                if idx % 2 == 0:
                    ret += code[idx]
            elif mode == 1:
                if idx % 2 != 0:
                    ret += code[idx]
        idx += 1
        if idx == len(code):
            break
    if ret == '':
        return "EMPTY"
    return ret