import re

name_in = input("Nome do arquivo de texto (entrada): ")
name_out = input("Nome do arquivo de texto (saida): ")

with open(name_in, encoding='utf8') as f:
    data = []
    while True:
        line = f.readline()
        if not line:
            break
        
        line = line.replace(".", "").replace(",", ".").strip()
        
        matches = re.findall(r'[A-Za-z_À-ÿ ]+|\d+\.\d+', line, re.UNICODE)
        results = [x.strip() + " | "  for x in matches]
        data.append("".join(results).replace(".", ","))

with open(name_out, 'w') as f:
    for d in data:
        f.write(d)
        f.write('\n')

print('finalizado')