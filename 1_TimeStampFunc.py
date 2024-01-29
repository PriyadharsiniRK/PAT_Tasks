from datetime import datetime

def timestamp(file_path):
    currentTimestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "w") as textfile:
        textfile.write(currentTimestamp)
    print(f"Current timestamp '{currentTimestamp}' has been written to {file_path}")

timestamp("timestamp.txt")