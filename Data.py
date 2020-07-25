from bs4 import BeautifulSoup
import requests

# PRODUCT Realme X (Space Blue, 128 GB)  (4 GB RAM) START
url = "https://www.flipkart.com/realme-x-space-blue-128-gb/p/itmfgybqzcgbxs26?pid=MOBFGYBQKYA5Y7HG&amp;lid=LSTMOBFGYBQKYA5Y7HG7OS3JD&amp;marketplace=FLIPKART&amp;fm=personalisedRecommendation/p2p-same&amp;iid=R:s;p:MOBFPCX76F3BYQDH;pt:d;uid:2738d0b3-e217-f39d-a723-8492cdd41f2f;.MOBFGYBQKYA5Y7HG.LSTMOBFGYBQKYA5Y7HG7OS3JD&amp;ppt=dynamic&amp;ppn=dynamic&amp;ssid=16is4v6w2o0000001594907705358&amp;otracker=dynamic_reco_Similar%2BProducts_1_1.productCard.PMU_V2_INFINITE_Similar%2BProducts_MOBFGYBQKYA5Y7HG.LSTMOBFGYBQKYA5Y7HG7OS3JD_personalisedRecommendation/p2p-same_1&amp;otracker1=dynamic_reco_PINNED_personalisedRecommendation/p2p-same_Similar%2BProducts_DESKTOP_HORIZONTAL_productCard_cc_1_NA_view-all&amp;cid=MOBFGYBQKYA5Y7HG.LSTMOBFGYBQKYA5Y7HG7OS3JD"
r = requests.get(url)
html_content = r.content
soup = BeautifulSoup(html_content, "html.parser")



###############
# FUNCTION FOR TITLE
###############
def title(soup):
    
    title = soup.find("h1", class_="_9E25nV").get_text()
    price = soup.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[0:1]:
        return item

# FUNCTION FOR PRICE
def price(soup):
    # soup = BeautifulSoup(html_content, "html.parser")
    title = soup.find("h1", class_="_9E25nV").get_text()
    price = soup.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[1:2]:
        return item 

# FUNCTION FOR RATINGS
def rating(soup):
    # soup = BeautifulSoup(html_content, "html.parser")
    title = soup.find("h1", class_="_9E25nV").get_text()
    price = soup.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[2:3]:
        return item
###############
# PRODUCT Realme X (Space Blue, 128 GB)  (4 GB RAM) END
###############

###############
#PRODUCT 2 START
###############
url1 = "https://www.flipkart.com/redmi-note-8-pro-halo-white-128-gb/p/itmc585e6c8ffd12?pid=MOBFHGT9NWZHHSHF&lid=LSTMOBFHGT9NWZHHSHFKV1PHL&marketplace=FLIPKART&fm=personalisedRecommendation/p2p-same&iid=R:s;p:MOBFQ3DPMQHHTMBZ;pt:hp;uid:446c5ba1-8a2f-39aa-95d3-786b55fa1d8f;.MOBFHGT9NWZHHSHF.LSTMOBFHGT9NWZHHSHFKV1PHL&ppt=hp&ppn=homepage&ssid=5zwmvet1i80000001595082455321&otracker=hp_reco_Recommended%2BItems_2_11.productCard.PMU_V2_Recommended%2BItems_MOBFHGT9NWZHHSHF.LSTMOBFHGT9NWZHHSHFKV1PHL_personalisedRecommendation/p2p-same_1&otracker1=hp_reco_WHITELISTED_personalisedRecommendation/p2p-same_Recommended%2BItems_DESKTOP_HORIZONTAL_productCard_cc_2_NA_view-all&cid=MOBFHGT9NWZHHSHF.LSTMOBFHGT9NWZHHSHFKV1PHL"
r1 = requests.get(url1)
html_content1 = r1.content
soup1 = BeautifulSoup(html_content1, "html.parser")        
        
def title1(soup1):
    
    title = soup1.find("h1", class_="_9E25nV").get_text()
    price = soup1.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup1.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[0:1]:
        return item        

def price1(soup1):
    
    title = soup1.find("h1", class_="_9E25nV").get_text()
    price = soup1.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup1.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[1:2]:
        return item   

def rating1(soup1):
    
    title = soup1.find("h1", class_="_9E25nV").get_text()
    price = soup1.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup1.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[2:3]:
        return item         
###############
#PRODUCT 2 END
###############


###############
#PRODUCT 3 START
###############
url2 = "https://www.flipkart.com/redmi-k20-pro-flame-red-128-gb/p/itmfg7uysw6gs55a?pid=MOBFG7UYFKHFKBNB&lid=LSTMOBFG7UYFKHFKBNBIBDWWE&marketplace=FLIPKART&fm=personalisedRecommendation/p2p-same&iid=R:s;p:MOBFQ3DPMQHHTMBZ;pt:d;uid:3f15d067-f39c-5f39-7df5-8e936362ceb7;.MOBFG7UYFKHFKBNB.LSTMOBFG7UYFKHFKBNBIBDWWE&ppt=dynamic&ppn=dynamic&ssid=qbxmt0r0tc0000001595157170659&otracker=dynamic_reco_Similar%2BProducts_5_1.productCard.PMU_V2_INFINITE_Similar%2BProducts_MOBFG7UYFKHFKBNB.LSTMOBFG7UYFKHFKBNBIBDWWE_personalisedRecommendation/p2p-same_1&otracker1=dynamic_reco_PINNED_personalisedRecommendation/p2p-same_Similar%2BProducts_DESKTOP_HORIZONTAL_productCard_cc_5_NA_view-all&cid=MOBFG7UYFKHFKBNB.LSTMOBFG7UYFKHFKBNBIBDWWE"
r2 = requests.get(url2)
html_content2 = r2.content
soup2 = BeautifulSoup(html_content2, "html.parser")        
        
def title2(soup2):
    
    title = soup2.find("h1", class_="_9E25nV").get_text()
    price = soup2.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup2.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[0:1]:
        return item        

def price2(soup2):
    
    title = soup2.find("h1", class_="_9E25nV").get_text()
    price = soup2.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup2.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[1:2]:
        return item   

def rating2(soup2):
    
    title = soup2.find("h1", class_="_9E25nV").get_text()
    price = soup2.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup2.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[2:3]:
        return item         
###############
#PRODUCT 3 END
###############

###############
#PRODUCT 4 START
###############
url3 = "https://www.flipkart.com/poco-x2-atlantis-blue-64-gb/p/itmbe7b58e0378b8?pid=MOBFZGJ6ZGMD7GEZ&lid=LSTMOBFZGJ6ZGMD7GEZFXQGD2&fm=neo/merchandising&iid=M_ae319c35-f898-49f4-a9e4-dbb417589f61_1.HH31ZQBVX1JF&ssid=yd4tlwb6fk0000001595243414668&otracker=dynamic_omu_infinite_Best%2Bselling%2BPhones_4_1.dealCard.OMU_INFINITE_Best%2Bselling%2BPhones_HH31ZQBVX1JF&cid=HH31ZQBVX1JF"
r3 = requests.get(url3)
html_content3 = r3.content
soup3 = BeautifulSoup(html_content3, "html.parser")        
        
def title3(soup3):
    
    title = soup3.find("h1", class_="_9E25nV").get_text()
    price = soup3.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup3.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[0:1]:
        return item        

def price3(soup3):
    
    title = soup3.find("h1", class_="_9E25nV").get_text()
    price = soup3.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup3.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[1:2]:
        return item   

def rating3(soup3):
    
    title = soup3.find("h1", class_="_9E25nV").get_text()
    price = soup3.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup3.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[2:3]:
        return item         
###############
#PRODUCT 4 END
###############


###############
#PRODUCT 5 START
###############
url4 = "https://www.flipkart.com/mi-10-coral-green-256-gb/p/itm63f68fab40d26?pid=MOBFRXYADQEXBCKB&lid=LSTMOBFRXYADQEXBCKBDL8AFA&marketplace=FLIPKART&srno=b_1_12&otracker=nmenu_sub_Electronics_0_Mi&fm=organic&iid=2687eca8-7fac-4485-8466-5736dbf5637b.MOBFRXYADQEXBCKB.SEARCH&ppt=browse&ppn=browse&ssid=34y5h5upao0000001595342686308"
r4 = requests.get(url4)
html_content4 = r4.content
soup4 = BeautifulSoup(html_content4, "html.parser")        
        
def title4(soup4):
    
    title = soup4.find("h1", class_="_9E25nV").get_text()
    price = soup4.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup4.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[0:1]:
        return item        

def price4(soup4):
    
    title = soup4.find("h1", class_="_9E25nV").get_text()
    price = soup4.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup4.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[1:2]:
        return item   

def rating4(soup4):
    
    title = soup4.find("h1", class_="_9E25nV").get_text()
    price = soup4.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup4.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[2:3]:
        return item         
###############
#PRODUCT 5 END
###############



###############
#PRODUCT 6 START
###############
url5 = "https://www.flipkart.com/realme-6-pro-lightning-blue-64-gb/p/itm19b1945c12aee?pid=MOBFPCX76F3BYQDH&lid=LSTMOBFPCX76F3BYQDHGAICT2&marketplace=FLIPKART&fm=gamificationAndPersonalisation/recentlyViewed&iid=GAP_RECENTLY_VIEWED_DESKTOP_HORIZONTAL_3ea0020b-0115-48b8-a4f2-e6c4687278ba.MOBFPCX76F3BYQDH&ppt=hp&ppn=homepage&ssid=h15h27y4gw0000001595244181036&otracker=hp_recently_viewed_Recently%2BViewed_10_29.productCard.RECENTLY_VIEWED_Recently%2BViewed_MOBFPCX76F3BYQDH_gamificationAndPersonalisation/recentlyViewed_9&otracker1=hp_recently_viewed_PINNED_gamificationAndPersonalisation/recentlyViewed_Recently%2BViewed_DESKTOP_HORIZONTAL_productCard_cc_10_NA_view-all&cid=MOBFPCX76F3BYQDH"
r5 = requests.get(url5)
html_content5 = r5.content
soup5 = BeautifulSoup(html_content5, "html.parser")        
        
def title5(soup5):
    
    title = soup5.find("h1", class_="_9E25nV").get_text()
    price = soup5.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup5.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[0:1]:
        return item        

def price5(soup5):
    
    title = soup5.find("h1", class_="_9E25nV").get_text()
    price = soup5.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup5.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[1:2]:
        return item   

def rating5(soup5):
    
    title = soup5.find("h1", class_="_9E25nV").get_text()
    price = soup5.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup5.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[2:3]:
        return item         
###############
#PRODUCT 6 END
###############