import openpyxl

#abrir planilha existente
book = openpyxl.load_workbook('Planilha de Compras.xlsx')
#selecionar pagina que quer abrir
frutas_page = book['frutas']
# Imprimindo os dados de cada linha
for rows in  frutas_page.iter_rows(min_row=2,max_row=5):
    for cell in rows:
        print(cell.value)





