from create_csvs import CsvCreationForBuiltIn

def main():
    amount_of_pages = input("Enter amount of pages: ")
    CsvCreationForBuiltIn(int(amount_of_pages))

if __name__ == "__main__":
    main()