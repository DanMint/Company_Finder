from bs4 import BeautifulSoup

with open("unit_tests/files_for_tests/BuiltInBoston_soup_output.txt", "r") as file:
    html = file.read()
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
    location_country = ""
    total_offices = ""
    if location_span:
        location = location_span.text.strip().split(",")
        if len(location) == 1:
            location_city = "Many locations"
            location_state = "Many locations"
            location_country = "Many locations"
            total_offices = location[0]
        elif location[0] == "Fully Remote":
                location_city = "Fully Remote"
                location_state = "Fully Remote"
                location_country = location[1]
                total_offices = "1 office"
        else:
            location_city = location[0]
            location_state = location[1]
            location_country = location[2]
            total_offices = "1 office"
    print("-----------------------------------------------------------------")
    print(f"Company name: {company_name}")
    print(f"Company field: {company_field}")
    print(f"Employees number: {employees_number}")
    print(f"Location city: {location_city}")
    print(f"Location state: {location_state}")
    print(f"Location state: {location_country}")
    print(f"Total offices: {total_offices}")
    print("-----------------------------------------------------------------")