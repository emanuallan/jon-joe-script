<div align="center">
<img src="https://www.joesnewbalanceoutlet.com/Content/images/logo.png" alt="nb-logo" style="border:5px solid black">
</div>

<h1 align="center">Joe's New Balance Shoe Tracker Script</h1>


<div align="center">
A python script that uses the Selenium and ChromeDriver module to crawl New Balance's outlet store website, Joe's, and checks for price changes (+/-) and new arrivals, as well as, removals amongst sneakers and clothing and exports them as a csv file.
</div>

## 🍭 Characteristics
- Checks for price changes (+/-)
- Checks for new shoe arrivals
- Checks for shoe removals
- Exports into .csv file


## 📦 Installation & Setup
```bash
$ git clone https://github.com/emanuallan/jon-joe-script.git
```
- got to https://www.joesnewbalanceoutlet.com/
- Go to 
  - MEN: https://www.joesnewbalanceoutlet.com/men/shoes/?Categories=men&Categories=shoes&PriceRange=&OnSale=&Icon=&Brand=0&PageSize=800&Page=1&Branded=False&ListType=Grid&Text=&Sorting=TopPicks
  - WOMEN: https://www.joesnewbalanceoutlet.com/women/shoes/?Categories=women&Categories=shoes&PriceRange=&OnSale=&Icon=&Brand=0&PageSize=800&Page=1&Branded=False&ListType=Grid&Text=&Sorting=TopPicks
- Select your size
- Copy the URL at the top
- Go into search script.py and replace the link at the bottom of the file in the `CheckProducts` method with the link you copied
- Run the script


## 🔨 What's Next?
- Creating an executable that takes in user input to generate the link needed
- Script currently has to run for clothing seperately, will cange so that both shoes and clothing are covered in one run

## ❓ More info
Joe's New Balance Outlet: https://www.joesnewbalanceoutlet.com/

