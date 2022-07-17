from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class amazonSearch():
    def search(self):
        baseUrl = "https://www.amazon.ca/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # i just put in iphone xr as a placeholder to test
        product = "iphone xr"

        # supposed to store listing titles, prices, review rating, links, images
        listingTitleList = []
        listingPriceList = []


        # clicks search bar then enters search
        searchBar = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
        searchBar.click()


        searchBar.send_keys(product)

        searchBtn = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
        searchBtn.click()

        # appends titles to title list
        sourceTitleList = driver.find_elements(By.CSS_SELECTOR, "span.a-size-base-plus.a-color-base.a-text-normal")

        for listing in sourceTitleList:
            listingTitleList.append(listing.text)

        # the prices in the html were  split between a whole part and a decimal part (ex. 20.99 -> 20   99
        sourcePriceListWhole = driver.find_elements(By.CSS_SELECTOR, "span.a-price-whole")
        sourcePriceListFraction = driver.find_elements(By.CSS_SELECTOR, "span.a-price-fraction")

        # the prices are strings since using float kept giving me errors | casting the whole string as a float solves the trick
        for num in range(len(sourcePriceListWhole)):
            price = float(sourcePriceListWhole[num].text + "." + sourcePriceListFraction[num].text)
            listingPriceList.append(price)

        # i tried zipping the two lists just to see if the listing title and the associated price were correct
        # sometimes its correct, other times it isn't

        combinedList = zip(listingTitleList, listingPriceList)
        zipped_list = list(combinedList)
        for i in range(len(zipped_list)):
            print(zipped_list[i])

        print(zipped_list)
        f = open("product_profiles.txt", "w")
        try:
            f.write(str(zipped_list))
        except:
            f.write(str(zipped_list[0:11]))
        f.close()

        time.sleep(2)

        # did not finish with images, links and reviews | perfectly fine, makes my life easier

ff = amazonSearch()
ff.search()