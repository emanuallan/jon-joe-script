from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv

store = "https://www.joesnewbalanceoutlet.com"
filter = "/?Filters%5BSize%5D=" 


######################################
########## URL GENERATOR #############
######################################
def URLGenProduct(gender, accessory, size):
    url = store + "/" + gender + "/" + accessory + filter
    if (gender == "men"):
        if (accessory == "shoes"):
            if (size > 3 and size < 21):
                url = url + str(size) + "?Categories=men&Categories=shoes&PriceRange=&OnSale=&Icon=&Brand=0&PageSize=800&Page=1&Branded=False&ListType=Grid&Text=&Sorting=TopPicks"
            else:
                print("Invalid input provided")
                return
        elif (accessory == "clothing"):
            url = url + size + "?Categories=men&Categories=clothing&PriceRange=&OnSale=&Icon=&Brand=0&PageSize=800&Page=1&Branded=False&ListType=Grid&Text=&Sorting=TopPicks"
    elif (gender == "women"):
        if (accessory == "shoes"):
            if (size > 3 and size < 15):
                url = url + size + "/?Categories=women&Categories=shoes&PriceRange=&OnSale=&Icon=&Brand=0&PageSize=800&Page=1&Branded=False&ListType=Grid&Text=&Sorting=TopPicks"
            else: 
                print("Invalid input provided")
                return
        elif (accessory == "clothing"):
            url = url + size + "?Categories=women&Categories=clothing&PriceRange=&OnSale=&Icon=&Brand=0&PageSize=800&Page=1&Branded=False&ListType=Grid&Text=&Sorting=TopPicks"
    return url

def CheckProducts(URL):
    try:
        ######################################
        ############ WEB SCRAPE ##############
        ######################################

        driver = webdriver.Chrome(executable_path='/Users/allanserna/Downloads/chromedriver') #initializes the chrome page
        driver.get(URL) 
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "productChips")))
        items = driver.find_elements_by_class_name("impression")

        newDictionary = {}
        for x in range (len(items)):
            if (x % 2 == 0):
                product_name = items[x].get_attribute('data-productname')
                product_price = float(items[x].get_attribute('data-price')) * 0.6
                product_code = items[x].get_attribute('data-productcode')
                newDictionary.update({ product_code : [product_name, product_price]})

        ######################################
        ############ FILE I/O ################
        ######################################

        oldDictionary = {}
        with open('results.csv') as file:
            file_reader = csv.reader(file, delimiter=',')
            next(file_reader)
            for row in file_reader:
                if (row[0] != "NEW" or row[0] != "REMOVED"):
                    oldDictionary.update({row[0]: [row[1], row[2]] }) 

        finalDictionary = {}
        for key in list(newDictionary):
            if key in oldDictionary:
                
                price_change = float(oldDictionary.get(key)[1]) - newDictionary.get(key)[1]
                print("oldPrice: ", oldDictionary.get(key)[1] , "\n newPrice: ", newDictionary.get(key)[1], " \n Price change: ", price_change, " \n")
                finalDictionary.update({key: [newDictionary.get(key)[0], newDictionary.get(key)[1], price_change] })
                del oldDictionary[key]
                del newDictionary[key]
            
        #right here oldDictionary has all the deleted product & outDict has the new products

        with open('results_2.csv', 'w+') as file:
            file_writer = csv.writer(file)
            file_writer.writerow(['PRODUCT_CODE', 'ITEM', 'PRICE', 'PRICE CHANGE'])
            for key in list(finalDictionary):
                file_writer.writerow([key, finalDictionary.get(key)[0], finalDictionary.get(key)[1], finalDictionary.get(key)[2]])

            file_writer.writerow(['NEW', 'NEW', 'NEW', 'NEW'])
            for key in list(newDictionary):
                file_writer.writerow([key, newDictionary.get(key)[0], newDictionary.get(key)[1]])
            
            file_writer.writerow(['REMOVED', 'REMOVED', 'REMOVED', 'REMOVED'])
            for key in list(oldDictionary):
                file_writer.writerow([key, oldDictionary.get(key)[0], oldDictionary.get(key)[1]])

    finally:
        driver.quit()



def main():
    # gender = input("men or women? \n")
    # accessory = input("shoes or clothing? \n")
    # if (accessory == "shoes"):
    #     size = int(input("shoe size? \n"))
    # elif (accessory == "clothing"):
    #     size = (input("clothing size? \n"))
    
    # myURL = URLGenProduct(gender, accessory, size)
    CheckProducts('https://www.joesnewbalanceoutlet.com/men/shoes/?Filters%5BSize%5D=13&Categories=men&Categories=shoes&PriceRange=&OnSale=&Icon=&Brand=0&PageSize=800&Page=1&Branded=False&ListType=Grid&Text=&Sorting=TopPicks')
    #https://www.joesnewbalanceoutlet.com/men/shoes/?Filters%5BSize%5D=13&Categories=men&Categories=shoes&PriceRange=&OnSale=&Icon=&Brand=0&PageSize=800&Page=1&Branded=False&ListType=Grid&Text=&Sorting=TopPicks
main()