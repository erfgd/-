#we need java to run this code(https://www.java.com/en/download/)
#Also, we need the pandas and tabula libraries in main.
#import tabula
#import pandas as pd
#pip install tabula-py - for java runtime


def tabula_import(filename):
    PDF=tabula.read_pdf(filename, pages='all', multiple_tables=True)
    
    #if you want view the result before saving - delete "#" from next string:
    #print ('\nTables from PDF file\n'+str(PDF))

    pdf_out_csv = "the path to the file"
    tabula.convert_into (filename, pdf_out_csv, output_format = "csv", pages='all', multiple_tables=True)
    print("Done")

    # openpyxl (cmd --> pip install openpyxl) to export to Excel from pandas dataframe  -- if we will use exel too.
    #functions to import to exel:
    #pdf_out_xlsx = "the path to the file"
    #PDF = pd.DataFrame(PDF)
    #PDF.to_excel(pdf_out_xlsx,index=False)