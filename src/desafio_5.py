def inverter_string(s):
    invertida = ""
    for i in range(len(s)-1, -1, -1):
        invertida += s[i]
    return invertida

if __name__ == "__main__":
    string = input("Informe uma string para inverter: ")
    print(f"String invertida: {inverter_string(string)}")
