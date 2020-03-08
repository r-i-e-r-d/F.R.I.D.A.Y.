import xlsxwriter


def create_credsheet(username, password):
    path = "/home/devi/F.R.I.D.A.Y./"
    credbook = xlsxwriter.Workbook(path + "cred/cred.xlsx")
    credsheet = credbook.add_worksheet("User Sheet")
    row, col = 0, 0
    credsheet.write(row, col, username)
    credsheet.write(row, col + 1, password)
    row += 1
    credbook.close()
