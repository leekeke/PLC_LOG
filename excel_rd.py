import xlrd

def excel_rd():
        excel_data = xlrd.open_workbook('par_data.xls')
        table = excel_data.sheets()[0]
        localip = table.cell(0,1).value
        print localip

if __name__ == '__main__':
    excel_rd()
