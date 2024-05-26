import datetime
def timestamp_file():

    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{current_timestamp}.txt"
    with open(filename, 'w') as file:
        file.write(current_timestamp)

    print(f"File '{filename}' created with content: {current_timestamp}")
timestamp_file()
