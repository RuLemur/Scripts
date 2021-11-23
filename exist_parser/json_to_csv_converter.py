import csv
import json

# Opening JSON file
with open('result.json') as json_file:
    result_data = json.load(json_file)

# field names
row_names = ['brand', 'model', 'year_from', 'year_to', 'img_link', 'model_link']


# name of csv file
filename = "models.csv"

with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(row_names)

    row_data = list(list())
    for brand, models in result_data.items():
        for model in models:
            row = list()
            row.append(brand)
            row.append(model['name'])
            row.append(model['year_from'])
            if model['year_to'] == 'наст. время':
                row.append('')
            else:
                row.append(model['year_to'])
            row.append(model['model_img'])
            row.append(model['model_link'])
            row_data.append(row)

    # writing the data rows
    csvwriter.writerows(row_data)
