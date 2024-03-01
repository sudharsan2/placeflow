import pandas as pd
from django.conf import settings
def write_list_to_excel(existing_file, column_name, data_list):
    # Load the existing Excel file
        file_path = (settings.BASE_DIR / "ExcelTemplate/appliedStudents.xlsx").resolve()
        df = pd.read_excel(file_path)

        # Add the data_list to the specified column
        df[column_name] = data_list

        # Save the updated DataFrame to the Excel file
        df.to_excel(existing_file, index=False)
        print(f'Data written to {existing_file} successfully.')