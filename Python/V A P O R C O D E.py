def vaporcode(s):
    a = ""
    s = s.upper()
    s = s.replace(" ", "")
    for x in s:
        a = a + x +"  "
    a = a.strip()
    return(a)
