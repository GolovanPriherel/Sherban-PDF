import tabula
from glob import glob
import PDF_2_Funs as pf
import fitz

if __name__ == "__main__":
    directory = 'PDFs/*.pdf'

    for filename in glob(directory):
        doc = fitz.open(filename)
        for pages in range(0, doc.pageCount):
            print(pages)
            try:
                data_set = tabula.read_pdf(filename, output_format='dataframe',
                                           pandas_options=({'header': None, "error_bad_lines": False}),
                                           pages=pages,
                                           stream=True,
                                           lattice=False,
                                           multiple_tables=False,
                                           silent=True) # Игнор ошибок

            except Exception as error:
                print(error)
                # sales_list = pd.DataFrame()
                data_set = None

            if data_set:
                # Очикстка данных от пробелов и прочего
                cleared_data = pf.clearing(data_set)

                # Обрезка .pdf
                pdf_names = filename[:-4]

                # Запись в один CSV файл с помощью модуля CSV
                pf.write_one_csv(pdf_names, data_set, pages)

                # Запись в один CSV файл с помощью Pandas
                # pf.write_one_pandas(pdf_names, data_set)