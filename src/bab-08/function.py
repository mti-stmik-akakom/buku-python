def jumlah(arg1):
    jml = 0
    for a in arg1:
        jml += 1
    return jml

str_obj = "Wabi Teknologi Indonesia"
jml_str = jumlah(str_obj)

print(f'String {str_obj} mempunyai ' + str(jml_str) + ' karakter')
