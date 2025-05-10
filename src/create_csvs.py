import csv
from scraping import builtInScrape

class CsvCreationForBuiltIn:
    def __init__(self, amount_of_pages):
        self.__amount_of_pages__ = amount_of_pages
        self.__company_names__ = None
        self.__size_range_to_companies__ = None
        self.__city_to_company__ = None
        self.__state_to_company__ = None
        self.__company_to_information__ = None

        self.driver_functon()

    def driver_functon(self):
        self.__populate_information__()
        self.__csv_state_to_company__()
        self.__csv_city_to_company__()
        self.__csv_company_names__()
        self.__csv_company_to_information__()
        self.__csv_size_range_to_companies__()

    def __populate_information__(self):
        new_scrape = builtInScrape.BuiltIn(self.__amount_of_pages__)
        self.__company_names__ = new_scrape.get_companies_names_
        self.__size_range_to_companies__ = new_scrape.get_size_range_to_companies_
        self.__state_to_company__ = new_scrape.get_state_to_company_
        self.__city_to_company__ = new_scrape.get_city_to_company_
        self.__company_to_information__ = new_scrape.get_company_to_information_

    def __csv_company_names__(self):
        with open("csv_data_files/company_names.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Company'])

            for company in self.__company_names__:
                writer.writerow([company])

    def __csv_state_to_company__(self):
        with open("csv_data_files/state_to_company.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['State', 'Company'])

            for state, companies in self.__state_to_company__.items():
                for company in companies:
                    writer.writerow([state, company])

    def __csv_city_to_company__(self):
        with open("csv_data_files/city_to_company.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['State', 'Company'])

            for city, companies in self.__city_to_company__.items():
                for company in companies:
                    writer.writerow([city, company])


    def __csv_size_range_to_companies__(self):
        with open("csv_data_files/size_to_company.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Size', 'Company'])

            for size, companies in self.__size_range_to_companies__.items():
                for company in companies:
                    writer.writerow([size, company])

    def __csv_company_to_information__ (self):
        header = ['Company', 'Employee Count', 'Industries', 'City', 'State', 'Office Count']

        with open('csv_data_files/companies_to_information.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)  # write the header

            for company, details in self.__company_to_information__.items():
                row = [company] + details
                writer.writerow(row)


    
def main():
    amount_of_pages = input("Enter amount of pages")
    temp = CsvCreationForBuiltIn(int(amount_of_pages))

if __name__ == "__main__":
    main()