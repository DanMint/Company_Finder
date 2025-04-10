from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re


class BuiltIn:
    def __init__(self, base_url):
        self.__base_url__ = base_url
        self.__driver__ = webdriver.Chrome()
        self.__all_companies__ = []
        self.__company_size__ = {}
        self.__companies_filterd_size__ = {}
        self.__retreive_all_companies_and_sizes__()
        
    def __retreive_all_companies_and_sizes__(self):
        for page_number in range(500, 501):
            temporary_url = self.__base_url__ + str(page_number)
            self.__driver__.get(temporary_url)
            html = self.__driver__.page_source
            soup = BeautifulSoup(html, "html.parser")
            companies_information = soup.find_all("div", class_="col-12 col-lg-9")

            for info in companies_information:
                print("--------------------------------------------")

                company_link_tag = info.find("a", href=True)
                slug = ""
                if company_link_tag:
                    href = company_link_tag['href']
                    slug = href.split("/company/")[-1]

                employees_span = info.find("span", string=lambda x: x and "Employees" in x)
                employees_number = ""
                if employees_span:
                    employees_number = employees_span.text.split()[0]  

                location_span = info.find("span", class_="text-gray-03")
                location_city = ""
                if location_span:
                    location_city = location_span.text.strip().split(",")[0]

                print(f"Slug: {slug}")
                print(f"Employees: {employees_number}")
                print(f"City: {location_city}")

                print("--------------------------------------------")

    @property
    def get_title(self):
        return self.__driver__.title
    
    @property
    def get_all_companies(self):
        return self.__all_companies__
    
    @property
    def get_all_companies_with_size(self):
        return self.__all_companies__

    @property
    def html_into_txt_debugging(self):
        with open("src/scraping/debugging/BuiltInBoston_soup_output.txt", "w", encoding="utf-8") as f:
            f.write(str(self.__soup__))

def main():
    test = BuiltIn("https://builtin.com/companies?country=USA&page=")
    test.get_all_companies_with_size
    # test.html_into_txt_debugging()

if __name__ == "__main__":
    main()