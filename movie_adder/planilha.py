import xlwings as xw


def adicionar_filme_planilha(arquivo_planilha, dados_filme):
    """
    Adiciona um filme à planilha Excel.
    """
    app = xw.App(visible=False)
    wb = app.books.open(arquivo_planilha)
    sheet = wb.sheets[0]

    ultima_linha = sheet.range(
        'A' + str(sheet.cells.last_cell.row)).end('up').row
    proxima_linha = ultima_linha + 1

    sheet.range(f"A{proxima_linha}").value = dados_filme["Título"]
    sheet.range(f"B{proxima_linha}").value = dados_filme["Gênero"]
    sheet.range(f"C{proxima_linha}").value = dados_filme["Ano"]
    sheet.range(f"D{proxima_linha}").value = dados_filme["Nota"]
    sheet.range(f"E{proxima_linha}").value = dados_filme["Assistido"]

    wb.save(arquivo_planilha)
    wb.close()
    app.quit()
    print(f"Filme '{dados_filme['Título']}' adicionado com sucesso!")
