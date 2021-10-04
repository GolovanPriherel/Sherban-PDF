import pandas as pd
import csv

def clearing(sells_raw):
    all_tabs = pd.DataFrame()
    for tabs in sells_raw:
        tabs.fillna('', inplace=True)
        empty_df = pd.DataFrame()
        all_tabs = pd.concat([all_tabs, tabs, empty_df], ignore_index=True)
        return all_tabs

# Запись в CSV разными файлами
# def write_many_csv():
#         # Запись в разные файлы с помощью пандаса
#         tabs.to_csv(f'{names}_Pd.csv', sep=';', encoding='windows-1251', index_label=False, header=False,
#                     index=False)

# Запись в CSV одним файлом
def write_one_csv(dir_file, dataframe, pages):
    if dataframe:
        print(dataframe[0].shape)
        if dataframe[0].shape[0] > 3:
            with open(f'{dir_file}_{pages}.csv', 'w', newline="", encoding='utf-8') as file:
                for tabs in dataframe:
                    # Запись в один файл с помощью csv
                    writer = csv.writer(file, delimiter=';')
                    for raws in range(tabs.shape[0]):
                        try:
                            writer.writerow(list(tabs.iloc[raws]))
                        except Exception as error:
                            print(error)
                            writer.writerow('Утеряны данные')

# Запись в пандас одним файлом
# def write_one_pandas(dir_file, dataframe):
#     empty_df = pd.DataFrame()
#     for tabs in dataframe:
#         tabs.to_csv(f'{dir_file}_pd.csv', sep=';', encoding='windows-1251',
#                          index_label=False, header=False, index=False)