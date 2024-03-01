import pandas as pd
from django.conf import settings
# def write_list_to_excel(existing_file, column_name, data_list):
#     # Load the existing Excel file
#         file_path = (settings.BASE_DIR / "ExcelTemplate/appliedStudents.xlsx").resolve()
#         df = pd.read_excel(file_path)

#         # Add the data_list to the specified column
#         df[column_name] = data_list

#         # Save the updated DataFrame to the Excel file
#         df.to_excel(existing_file, index=False)
#         print(f'Data written to {existing_file} successfully.')

def write_dict_to_excel(existing_file, data_dict):
    # Load the existing Excel file
    df = pd.read_excel(existing_file)

    # Add each column from the data_dict to the DataFrame
    for column_name, data_list in data_dict.items():
        df[column_name] = data_list

    # Save the updated DataFrame to the Excel file
    df.to_excel('appliedStudent.xlsx', index=False)
    print(f'Data written to {existing_file} successfully.')