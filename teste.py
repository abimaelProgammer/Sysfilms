import csv
avaliacoes = [{"Titulo":"Shrek","Estrelas":5},{"Titulo":"Her","Estrelas":6}]
with open('teste.csv','a', newline='', encoding="utf-8") as arquivo:
      escritor = csv.writer(arquivo)
      avl = avaliacoes[-1]
      avl = [avl['Titulo'], avl['Estrelas']]
      escritor.writerow(avl)

print(avaliacoes[])      


