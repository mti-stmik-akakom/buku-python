def jumlah(arg1):
    jml = 0
    for a in arg1:
        jml += 1
    return jml

def main():
    str_obj = "Wabi Teknologi Indonesia"
    jml_str = jumlah(str_obj)

    print(f'String {str_obj} mempunyai ' + str(jml_str) + ' karakter')

#if __name__== "__main__":
#    main()

# Menggunakan Python 3 lebih singkat:
# langsung panggil main()

main()
