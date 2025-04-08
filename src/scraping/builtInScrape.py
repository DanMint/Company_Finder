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
            company_links = soup.find_all("div", class_="d-flex align-items-center my-sm mt-lg-0")
            company_sizes = soup.find_all("div", class_="d-inline me-lg-lg")

            stripped_companies = set()
            for div in company_links:
                anchors = div.find_all("a", href=True)
                for a in anchors:
                    href = a['href']
                    if href.startswith("/company/"):
                        company_slug = href.replace("/company/", "")
                        stripped_companies.add(company_slug)

            stripped_companies = list(stripped_companies)
        
            stripped_sizes = []
            for company_size in company_sizes:
                size = company_size.find("span")
                if size:
                    text = size.get_text()
                    match = re.search(r'[\d,]+', text)
                    if match:
                        number = int(match.group(0).replace(',', ''))
                        stripped_sizes.append(number)

            for pos in range(0, len(stripped_companies)):
                self.__all_companies__.append(stripped_companies[pos])
                self.__company_size__[stripped_companies[pos]] = stripped_sizes[pos]

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