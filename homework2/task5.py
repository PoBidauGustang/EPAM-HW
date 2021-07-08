def custom_range(*args):
    string_ch = args[0]
    if args[3:4]:
        start = string_ch.find(args[1])
        end = string_ch.find(args[2])
        step = args[3]
        return list(string_ch[start:end:step])
    if args[2:3]:
        start = string_ch.find(args[1])
        end = string_ch.find(args[2])
        return list(string_ch[start:end])
    if args[1:2]:
        start = string_ch.find(args[1])
        return list(string_ch[:start])
