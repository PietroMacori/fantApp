if __name__=="__main__":
    import xlrd

    loc=("/Users/pietromacori/github/fantApp/Quotazioni_Fantacalcio_Test.xlsx")

    wb=xlrd.open_workbook(loc)
    sheet=wb.sheet_by_index(0)
    sheet.cell_value(0,0)

    for i in range(sheet.nrows):
        for j in range(sheet.ncols):
            print(sheet.cell_value(i,j)),

        print("")
