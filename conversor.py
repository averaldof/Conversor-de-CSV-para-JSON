import csv;
import json;

def conversor_json(arqCSV, arqJSON):
    data = {};

    with open(arqCSV, encoding='utf-8') as cvsf:
        #leitura do arquivo CSV
        leitorCSV= csv.DictReader(cvsf);

        for rows in leitorCSV:
            key = rows['No']
            data[key] = rows

    with open(arqJSON, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4));


arqCSV = input("Digite o nome do arquivo csv: ");
arqJSON = input("Digite o nome do futuro arquivo JSON: ");

conversor_json(arqCSV, arqJSON);