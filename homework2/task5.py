def custom_range(*args):
    string_ch = args[0]
    if args[3:4]:
        start = string_ch.find(args[1])
        stop = string_ch.find(args[2])
        step = args[3]
        return list(string_ch[start:stop:step])
    if args[2:3]:
        start = string_ch.find(args[1])
        stop = string_ch.find(args[2])
        return list(string_ch[start:stop])
    if args[1:2]:
        stop = string_ch.find(args[1])
        return list(string_ch[:stop])
