from googletrans import Translator
translator = Translator()

code = "QSEKIJYS FKFYB VQJ AYDWTEC"
code_x = list(code)
new_code=[]


for i in range(26): # Each new code
    for j in range(len(code)):
        if code_x[j] != ' ':
            code_x[j] = chr((ord(code_x[j])+i-65)%26 +65)
    str_x = "".join(code_x)
    print(str_x)
    new_code.append(str_x)
    code_x = list(code)

print("\n")
for i in range(26): # Print each new code and print each new code translated
    print(new_code[i])
    print(translator.translate(new_code[i], dest='pt').text)
    print("\n")


