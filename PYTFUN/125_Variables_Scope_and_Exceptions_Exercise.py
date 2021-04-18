# PROGRAMMING EXERCISE
import csv
import re


def read_source_file():
    temperatures = []
    # Reading of user input in try-catch block to ensure no exception is thrown in case of wrong path provided by user
    try:
        # Test file available in data/ folder
        # filename = "./data/temperatures.csv"
        filename = input("Please put filepath plus name here, in format 'C:\\MyFiles\\temperatures.csv' ")

        with open(filename, 'r', encoding="utf8") as f:
            csv_data = csv.reader(f)
            data_lines = list(csv_data)

            for i in range(len(data_lines)):
                temperatures.append(data_lines[i][0])
    except:
        print("Please provide a valid path and filename!")

    print("Input temperature values: ")
    print(temperatures)

    return temperatures


def convert_celsius_values(temp_list):
    pattern = r"(-?([0-9]+(\.[0-9][0-9]?)?))C"
    converted_temperatures = []

    # Check if each individual value matches the regex pattern for Celsius temperature
    # If no match - value simply appended to final list
    # If match - value is converted from C to F and appended to final list
    for item in temp_list:
        match = re.search(pattern, item)
        if match:
            celsius_value = float(match.group(1))
            fahrenheit_value = (celsius_value * (9.0/5.0)) + 32
            converted_temperatures.append(f"{fahrenheit_value:.2f}F")
        else:
            converted_temperatures.append(item)

    return converted_temperatures


def save_final_file(final_list: list):
    # Write to .txt
    # with open('./data/outputFahrenheit.txt', mode='w', encoding='utf-8') as output:
    #     for value in convertedListItems:
    #         output.write(value + '\n')

    # Write to .csv
    with open('./data/outputFahrenheit.csv', mode='w', encoding='utf-8', newline='') as output:
        csv_writer = csv.writer(output, delimiter=';')
        for value in final_list:
            # Saving with value casted to string and then called .split() method on it, as otherwise
            # csv writer iterates over the string and puts a delimiter after each iterable character (e.g. 3;2;.;0;0;F)
            csv_writer.writerow(str(value).split())


tempList = read_source_file()
convertedListItems = convert_celsius_values(tempList)
save_final_file(convertedListItems)
