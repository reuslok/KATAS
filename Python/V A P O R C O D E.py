def vaporcode(s):
    a = ""
    s = s.upper()
    s = s.replace(" ", "")
    for x in s:
        a = a + x +"  "
    a = a.strip()
    return(a)
#2nd answer
return "  ".join(s.replace(" ", "").upper())
