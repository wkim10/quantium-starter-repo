import csv
import os

with open("./final_data.csv", "w") as output_file:
    csvwriter = csv.writer(output_file)

    header = ["sales", "date", "region"]
    csvwriter.writerow(header)

    for file in os.listdir("./data"):
        with open(f"./data/{file}", "r") as input_file:
            csvreader = csv.reader(input_file)

            row_index = 0
            for row in csvreader:
                if row_index > 0:
                    product = row[0]

                    if product == "pink morsel":
                        singular_price = row[1]
                        quantity = row[2]
                        date = row[3]
                        region = row[4]

                        price = float(singular_price[1:])
                        sale = float(quantity) * price

                        csvwriter.writerow([sale, date, region])
                    
                row_index += 1