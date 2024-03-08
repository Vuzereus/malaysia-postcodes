import csv
import os

STATES_FILE_PATH = 'Malaysia_Postcode-states.csv'
POSTCODES_FILE_PATH = 'Malaysia_Postcode-postcodes.csv'
STATES_FOLDER = 'states'

def extract_postcode_data(input_file: str, search_string: str, replace_string: str):
    with open(input_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        rows_to_save = []

        for row in reader:
            if search_string in row:
                modified_row = [cell.replace(search_string, replace_string) for cell in row]
                rows_to_save.append(modified_row)

    if not os.path.exists(STATES_FOLDER):
        os.makedirs(STATES_FOLDER)
        
    output_file = replace_string.replace(' ', '_') + '.csv'
    output_file = os.path.join(STATES_FOLDER, output_file)
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows_to_save)
    print(f'File `{output_file}` has been created')

def update_readme_file(states_folder_path: str):
    content = ''
    for filename in os.listdir(states_folder_path):
        if filename.endswith(".csv"):
            with open(os.path.join(states_folder_path, filename), 'r') as file:
                lines = file.readlines()
                first_postcode = lines[0].strip().split(',')[0]
                last_postcode = lines[-1].strip().split(',')[0]
                # print(f"Filename: {filename}, First Postcode: {first_postcode}, Last Postcode: {last_postcode}")
                content += f'- [{filename.replace("_", " ").replace(".csv", "")}](states/{filename}) ({first_postcode} - {last_postcode})\n'
    with open('README.md', 'w') as file:
        file.write('# Malaysia Postcodes Repository\n\n')
        file.write('Welcome to the Malaysia Postcodes repository! This resource is designed to support application development by providing up-to-date information on postcodes, cities, and states in Malaysia.\n\n')
        file.write('### Data Source\n\n')
        file.write('We\'ve sourced our data from [MalaysiaPostcode](https://malaysiapostcode.com/download), specifically the following files:\n\n')
        file.write('- [Malaysia_Postcode-states.csv](Malaysia_Postcode-states.csv)\n')
        file.write('- [Malaysia_Postcode-postcodes.csv](Malaysia_Postcode-postcodes.csv)\n\n')
        file.write('### Data Organization\n\n')
        file.write('To make navigation easier, we\'ve organized the data by state. Explore the individual state files for a comprehensive breakdown of postcodes.\n\n')
        file.write(content)
        file.write('\n')
        file.write('### Licensing\n\n')
        file.write('This repository and its data are governed by the [CC BY 4.0 DEED](https://creativecommons.org/licenses/by/4.0/deed.en). Feel free to use the information in accordance with the specified license. If you have any questions or need further assistance, don\'t hesitate to reach out. Happy coding!')
    print('README.md has been updated')

def main():
    with open(STATES_FILE_PATH, mode='r') as file:
        reader = csv.reader(file)
        data_array = []
        for row in reader:
            extract_postcode_data(POSTCODES_FILE_PATH, row[0], row[1])
            data_array.append(row)
    update_readme_file(STATES_FOLDER)

if __name__ == '__main__':
    main()