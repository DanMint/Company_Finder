from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re
import random



class BuiltIn:
    def __init__(self, final_page_number=2504):
        self.__base_url__ = "https://builtin.com/companies?country=USA&page="
        self.__driver__ = webdriver.Chrome()
        self.__final_page_number__ = final_page_number
        self.__find_last_page_number__()
        self.__companies_names__ = []
        # These are ranges. 10 means 1-10, 20 means 11-20, 30 means 21-30, etc.
        self.__size_range__ = [10, 20, 30, 40, 50, 75, 100, 150, 200, 250, 300, 400, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000, 7500, 10000]
        # These are ranges. 10 means 1-10, 20 means 11-20, 30 means 21-30, etc.
        self.__size_range_to_companies__ = {"None":[], 10:[], 20:[], 30:[], 40:[], 50:[], 75:[], 100:[], 150:[], 200:[], 250:[], 300:[], 400:[], 500:[], 750:[], 1000:[], 1500:[], 2000:[], 2500:[], 3000:[], 3500:[], 4000:[], 5000:[], 7500:[], 10000:[]}
        self.__city_to_company__ = {}
        self.__state_to_company__ = {}
        # key = name of company(str), Value = employees_number, company_field, location_city, location_state, total_offices
        self.__company_to_information__ = {}
        self.__retreive_company_information__()
        
    def __find_last_page_number__(self) -> None:
        # This function is used to find the last page number of the website
        # The last page number is used to iterate through the pages of the website
        # The last page number is found by checking if the last page number is valid
        # If the last page number is not valid, it will decrement the last page number and check again
        # This will continue until a valid last page number is found
        temporary_url = self.__base_url__ + str(self.__final_page_number__)
        self.__driver__.get(temporary_url)
        html = self.__driver__.page_source
        soup = BeautifulSoup(html, "html.parser")
        last_page_number = soup.find("h2", class_="font-Montserrat fw-extrabold fs-2xl fs-lg-3xl text-midnight text-center mt-3xl mt-lg-4xl")
        if last_page_number:
            self.__final_page_number__ -= 1
            self.__final_page_number__()
        return 

    def __retrieve_page_html__(self, page_number) -> str:
        temporary_url = self.__base_url__ + str(page_number)
        self.__driver__.get(temporary_url)
        return self.__driver__.page_source

    def __retreive_company_information__(self):
        pages = list(range(1, self.__final_page_number__ + 1))
        random.shuffle(pages)  # Randomize page access order to avoid detection
        # self.__final_page_number__ + 1
        for idx, page_number in enumerate(pages, 1):
            if idx % 100 == 0:
                print(f"Processed {idx} pages, taking a longer break.")
                time.sleep(random.uniform(100, 250)) 
            html = self.__retrieve_page_html__(page_number)
            soup = BeautifulSoup(html, "html.parser")
            companies_information = soup.find_all("div", class_="col-12 col-lg-9")

            for info in companies_information:
                company_link_tag = info.find("a", href=True)
                company_name = ""
                if company_link_tag:
                    href = company_link_tag['href']
                    company_name = href.split("/company/")[-1]

                company_field_div = info.find("div", class_="font-barlow fw-medium text-gray-04 mb-sm")
                company_field = ""
                if company_field_div:
                    company_field = company_field_div.get_text(strip=True)
                
                    
                employees_span = info.find("span", string=lambda x: x and "Employees" in x)
                employees_number = ""
                if employees_span:
                    employees_number = employees_span.text.split()[0]  

                location_span = info.find("span", class_="text-gray-03")
                location_city = ""
                location_state = ""
                total_offices = ""
                if location_span:
                    location = location_span.text.strip().split(",")
                    if len(location) == 1:
                        location_city = "Many locations"
                        location_state = "Many locations"
                        total_offices = location[0]
                    elif location[0] == "Fully Remote":
                            location_city = "Fully Remote"
                            location_state = "Fully Remote"
                            total_offices = "1 office"
                    else:
                        location_city = location[0]
                        location_state = location[1]
                        total_offices = "1 office"

                location_state = location_state.strip()  
                location_city = location_city.strip()

                self.__companies_names__.append(company_name)
                self.__company_to_information__[company_name] = [employees_number, company_field, location_city, location_state, total_offices]

                if location_state in self.__state_to_company__:
                    self.__state_to_company__[location_state].append(company_name)
                else:
                    self.__state_to_company__[location_state] = [company_name]

                if location_city in self.__city_to_company__:
                    self.__city_to_company__[location_city].append(company_name)
                else:
                    self.__city_to_company__[location_city] = [company_name]
                
                self.__put_company_to_range(company_name, employees_number)

            time.sleep(random.uniform(5,10))

    def __put_company_to_range(self, company_name, employees_number) -> None:
        if not employees_number:
            self.__size_range_to_companies__["None"].append(company_name)
            return
        temp = int(employees_number.replace(",", ""))
        closest_number = min(self.__size_range__, key=lambda x: abs(x - temp))
        self.__size_range_to_companies__[closest_number].append(company_name)


    @property
    def get_title(self):
        return self.__driver__.title
    
    @property
    def get_companies_names_(self):
        return self.__companies_names__
    
    @property
    def get_company_to_information_(self):
        return self.__company_to_information__
    
    @property
    def get_state_to_company_(self):
        return self.__state_to_company__
    
    @property
    def get_city_to_company_(self):
        return self.__city_to_company__
    
    @property
    def get_size_range_to_companies_(self):
        return self.__size_range_to_companies__
    
    @property
    def html_into_txt_debugging(self):
        with open("src/scraping/debugging/BuiltInBoston_soup_output.txt", "w", encoding="utf-8") as f:
            f.write(str(self.__soup__))

def main():
    test = BuiltIn()
    print("---------------------------------------------------")
    print(test.get_city_to_company_)
    print("---------------------------------------------------")
    print(test.get_state_to_company_)
    print("---------------------------------------------------")
    print(test.get_size_range_to_companies_)
    print("---------------------------------------------------")
    print(test.get_company_to_information_)
    print("---------------------------------------------------")
    print(test.get_companies_names_)
    print("---------------------------------------------------")



if __name__ == "__main__":
    main()