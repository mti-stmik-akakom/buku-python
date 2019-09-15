# function_default.py
#
# menghitung jumlah karakter tertentu dalam string
# jika the_char tidak ada, maka default menghitung 
# jumlah semua karakter

def jumlah(the_str, the_char=None):
    jml = 0
    if the_char:
        for a in the_str:
            if a == the_char:
                jml += 1
    else:
        for a in the_str:
            jml += 1
    return jml

str_obj = "Wabi Teknologi Indonesia"

jml_semua = jumlah(str_obj)
print(f'String {str_obj} mempunyai ' + str(jml_semua) + ' karakter')

jml_a = jumlah(str_obj, 'a')
print(f'String {str_obj} mempunyai ' + str(jml_a) + ' karakter a')
