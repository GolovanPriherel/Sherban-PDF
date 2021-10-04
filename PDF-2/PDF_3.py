import tabula
from glob import glob
import PDF_2_Funs as pf

if __name__ == "__main__":
    directory = 'PDFs/*.pdf'

    for filename in glob(directory):
        try:
            data_set = tabula.read_pdf(filename, output_format='dataframe', pandas_options=({'header': None}),
                                       pages='all', stream=True, lattice=False, multiple_tables=False, silent=True)
        except:
            # sales_list = pd.DataFrame()
            data_set = None

        if data_set:
            # Очикстка данных от пробелов и прочего
            cleared_data = pf.clearing(data_set)

            # Обрезка .pdf
            pdf_names = filename[:-4]

            # Запись в один CSV файл с помощью модуля CSV
            pf.write_one_csv(pdf_names, data_set)


            # Запись в один CSV файл с помощью Pandas
            # pf.write_one_pandas(pdf_names, data_set)
