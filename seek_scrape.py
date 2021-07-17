import requests
from bs4 import BeautifulSoup
while True:
    job = input("What job would you like to search for?").replace(" ", "-")
    location = input("What area would you like to search? ").replace(" ", "-")

    URL = 'https://www.seek.co.nz/' + job + '-jobs/in-' + location
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='app')

    articles = results.find_all('article')

    for article in articles:
        title_elem = article.find('h1')
        list_elem = article.find('ul')
        company_elem = article.select_one('[data-automation="jobCompany"]')
        location_elem = article.select_one('[data-automation="jobLocation"]')
        area_elem = article.select_one('[data-automation="jobArea"]')
        description_elem = article.select_one('[data-automation="jobShortDescription"]')

        if None in (title_elem, list_elem, company_elem, location_elem, area_elem, description_elem):
            continue

        print("-"*75)
        print("Role - " + title_elem.text)
        print("Company - " + company_elem.text)
        print("In - " + location_elem.text + " - " + area_elem.text + "\n")
        for item in list_elem:
            print("- " + item.text)
        print("\n" + description_elem.text)
