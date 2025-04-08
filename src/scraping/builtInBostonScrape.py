from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class BuiltInBoston:
    def __init__(self):
        self.__base_url__ = "https://www.builtinboston.com/companies?country=USA&page="
        self.__driver__ = webdriver.Chrome()
        self.__all_companies__ = [None]
        
    def __retreive_all_companies__(self):
        for page_number in range(1, 142):
            temporary_url = self.__base_url__ + str(page_number)
            self.__driver__.get(temporary_url)
            html = self.__driver__.page_source
            soup = BeautifulSoup(html, "html.parser")
            company_links = soup.find_all("a", href=True)
            stripped = [a['href'].replace("/company/", "") for a in company_links if a['href'].startswith("/company/")]

            for item in set(stripped):
                base = item.split("/")[0]
                if base not in self.__all_companies__:
                    self.__all_companies__.append(base)
        
        print(self.__all_companies__)

    @property
    def get_title(self):
        return self.__driver__.title
    
    @property
    def get_all_boston_companies(self):
        return self.__all_companies__
    
    @property
    def html_into_txt_debugging(self):
        with open("src/scraping/debugging/BuiltInBoston_soup_output.txt", "w", encoding="utf-8") as f:
            f.write(str(self.__soup__))


# title = driver.title
# content = driver.find_element(By.NAME, 'Password')
# print(content)
# driver.implicitly_wait(20)

# print(title)

def main():
    test = BuiltInBoston()
    print(test.get_title)
    test.__retreive_all_companies__()
    # test.html_into_txt_debugging()

if __name__ == "__main__":
    main()