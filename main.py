from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver

to_location = 'DXB'
url = 'https://www.nz.kayak.com/flights/AKL-{to_location}/2023-07-16/2023-07-17?sort=bestflight_a'.format(to_location=to_location)

driver = webdriver.Chrome()
driver.get(url)

wait = WebDriverWait(driver, 10)
flight_rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="inner-grid keel-grid"]')))

lst_prices = []
lst_company_names = []

for web_element in flight_rows:
    element_html = web_element.get_attribute('outerHTML')
    element_soup = BeautifulSoup(element_html, 'html.parser')

    price = element_soup.find("div", {"class": "col-price result-column js-no-dtog"}) \
                       .find("span", {"class": "price-text"}).text
    lst_prices.append(price)

    company_names = element_soup.find("span", {"class": "codeshares-airline-names"}).text
    lst_company_names.append(company_names)

print(lst_company_names)
print(lst_prices)
