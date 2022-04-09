import camelot
# Для Анечки
def camelot_func(filename):
    tables = camelot.read_pdf(filename, pages = '1, 2-end', process_background = True)
    tables
    tables.export('filename.csv', f = 'csv', compress = True)
    i=0
    while i <= 9:
        tables[i]
        tables[i].parsing_report
        tables[i].to_csv('filename.csv')
        tables[i].df
        i = i + 1
        
# Роман, если что, помни, пожалуйста, что я глупая        
