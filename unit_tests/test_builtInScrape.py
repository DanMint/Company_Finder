import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from src.scraping.builtInScrape import BuiltIn

class TestBuiltInScrape(unittest.TestCase):
    @patch("src.scraping.builtInScrape.BuiltIn.__find_last_page_number__")
    @patch("src.scraping.builtInScrape.BuiltIn.__retrieve_page_html__")
    def test_retreive_company_information(self, mock_retrival, find_last_page_number):
        find_last_page_number.return_value = None
        with open("unit_tests/files_for_tests/BuiltInBoston_soup_output.txt", "r") as file:
            mock_retrival.return_value = file.read()

        built_in = BuiltIn(1)

        company_names = [
            "simply-business",
            "sophia-genetics",
            "cohere-health",
            "atlassian",
            "novo-nordisk-0",
            "rapid7",
            "squareworks-consulting",
            "agero",
            "kings-hawaiian",
            "federal-reserve-bank-boston",
            "artera",
            "schrodinger-inc",
            "bigtime-software-inc",
            "3play-media",
            "smartcat",
            "gradient-ai",
            "ekotrope",
            "morse-corp",
            "ellevation-education",
            "snyk"
        ]

        city_to_companies = {
            "Many locations": [
                "simply-business",
                "sophia-genetics",
                "atlassian",
                "novo-nordisk-0",
                "rapid7",
                "kings-hawaiian",
                "artera",
                "schrodinger-inc",
                "bigtime-software-inc",
                "3play-media",
                "morse-corp",
                "snyk"
            ],
            "Fully Remote": [
                "cohere-health",
                "squareworks-consulting",
                "smartcat",
                "ellevation-education"
            ],
            "Medford": [
                "agero"
            ],
            "Boston": [
                "federal-reserve-bank-boston",
                "gradient-ai",
                "ekotrope"
            ]
        }

        state_to_companies = {
            "Many locations": [
                "simply-business",
                "sophia-genetics",
                "atlassian",
                "novo-nordisk-0",
                "rapid7",
                "kings-hawaiian",
                "artera",
                "schrodinger-inc",
                "bigtime-software-inc",
                "3play-media",
                "morse-corp",
                "snyk"
            ],
            "Fully Remote": [
                "cohere-health",
                "squareworks-consulting",
                "smartcat",
                "ellevation-education"
            ],
            "Massachusetts": [
                "agero",
                "federal-reserve-bank-boston",
                "gradient-ai",
                "ekotrope"
            ]
        }

        company_to_information = {
            "simply-business": ["1,100", "Fintech • Information Technology • Insurance • Software", "Many locations", "Many locations", "Many locations", "4 Offices"],
            "sophia-genetics": ["450", "Artificial Intelligence • Big Data • Healthtech • Software • Biotech", "Many locations", "Many locations", "Many locations", "3 Offices"],
            "cohere-health": ["800", "Healthtech • Software", "Fully Remote", "Fully Remote", "USA", "1 office"],
            "atlassian": ["11,000", "Cloud • Information Technology • Productivity • Security • Software • App development • Automation", "Many locations", "Many locations", "Many locations", "15 Offices"],
            "novo-nordisk-0": ["69,000", "Healthtech • Software • Pharmaceutical", "Many locations", "Many locations", "Many locations", "12 Offices"],
            "rapid7": ["2,400", "Artificial Intelligence • Cloud • Information Technology • Sales • Security • Software • Cybersecurity", "Many locations", "Many locations", "Many locations", "14 Offices"],
            "squareworks-consulting": ["65", "Artificial Intelligence • Fintech • Payments • Software • Consulting • Financial Services • Automation", "Fully Remote", "Fully Remote", "USA", "1 office"],
            "agero": ["3,500", "Automotive • Big Data • Insurance • Software • Transportation", "Medford", "Massachusetts", "USA", "1 office"],
            "kings-hawaiian": ["1,500", "Food • Sales • Manufacturing", "Many locations", "Many locations", "Many locations", "3 Offices"],
            "federal-reserve-bank-boston": ["1,200", "Fintech • Information Technology • Payments • Financial Services • Cryptocurrency", "Boston", "Massachusetts", "USA", "1 office"],
            "artera": ["318", "Healthtech • Other • Sales • Software • Analytics • Conversational AI", "Many locations", "Many locations", "Many locations", "10 Offices"],
            "schrodinger-inc": ["937", "Artificial Intelligence • Big Data • Healthtech • Machine Learning • Software • Biotech • Pharmaceutical", "Many locations", "Many locations", "Many locations", "10 Offices"],
            "bigtime-software-inc": ["175", "Productivity • Professional Services • Sales • Software • Consulting", "Many locations", "Many locations", "Many locations", "4 Offices"],
            "3play-media": ["211", "Artificial Intelligence • Information Technology • Professional Services • Social Impact • Software", "Many locations", "Many locations", "Many locations", "3 Offices"],
            "smartcat": ["242", "Artificial Intelligence • Machine Learning • Natural Language Processing • Conversational AI", "Fully Remote", "Fully Remote", "USA", "1 office"],
            "gradient-ai": ["110", "Artificial Intelligence • Information Technology • Insurance • Machine Learning • Software • Analytics", "Boston", "Massachusetts", "USA", "1 office"],
            "ekotrope": ["29", "Cloud • Greentech • Information Technology • Software • Energy", "Boston", "Massachusetts", "USA", "1 office"],
            "morse-corp": ["180", "Aerospace • Artificial Intelligence • Computer Vision • Machine Learning • Software • Defense", "Many locations", "Many locations", "Many locations", "2 Offices"],
            "ellevation-education": ["225", "Edtech • Social Impact • Software", "Fully Remote", "Fully Remote", "USA", "1 office"],
            "snyk": ["1,000", "Artificial Intelligence • Cloud • Information Technology • Security • Software • Cybersecurity • Data Privacy", "Many locations", "Many locations", "Many locations", "10 Offices"]
        }

        size_range_to_companies = {
            "None": [],
            10: [],
            20: [],
            30: ["ekotrope"],
            40: [],
            50: [],
            75: ["squareworks-consulting"],
            100: [],
            150: [],
            200: ["bigtime-software-inc", "morse-corp", "3play-media"],
            250: ["smartcat", "ellevation-education"],
            300: [],
            400: ["artera"],
            500: ["sophia-genetics"],
            750: [],
            1000: ["gradient-ai", "simply-business", "kings-hawaiian", "federal-reserve-bank-boston", "snyk"],
            1500: [],
            2000: [],
            2500: ["rapid7"],
            3000: [],
            3500: ["agero"],
            4000: [],
            5000: [],
            7500: [],
            10000: ["atlassian", "novo-nordisk-0"]
        }

        self.assertEqual(company_names, built_in.get_companies_names_)
        self.assertEqual(city_to_companies, built_in.get_city_to_company_)
        
        self.assertEqual(state_to_companies, built_in.get_state_to_company_)
        self.assertEqual(company_to_information, built_in.get_company_to_information_)



if __name__ == "__main__":
    unittest.main()
