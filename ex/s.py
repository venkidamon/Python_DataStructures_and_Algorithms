def stringg(s):
    d = ""
    f = ""
    for i in range(len(s)):
        if s[i] not in f:
            f += s[i]
        else:
            if len(d) < len(f):
                d = f
            e = f.index(s[i]) + 1
            print(e)
            print(f[e::])
            print(s[i])
            f = f[f.index(s[i])+1::] + s[i]
            
    return max(len(d), len(f))


s = stringg('jdshfdhfjskfsduemwj')

