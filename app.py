from flask import Flask, render_template,request,url_for
from bs4 import BeautifulSoup
import requests
from Data import price,rating,title,soup,soup1,price1,title1,rating1
from Data import price2,title2,rating2,soup2,price3,title3,rating3,soup3
from Data import price4,title4,rating4,soup4,price5,title5,rating5,soup5



app = Flask(__name__)



# FUNCTION CONNECTED FROM DATA.PY EG. TITLE PRICE 
#############
#PRODUCT 1
#############
price = price(soup)
title = title(soup)
rating = rating(soup)

#############
#PRODUCT 2
#############
price1 = price1(soup1)
title1 = title1(soup1)
rating1 = rating1(soup1)

#############
#PRODUCT 3
#############
price2 = price2(soup2)
title2 = title2(soup2)
rating2 = rating2(soup2)

#############
#PRODUCT 4
#############
price3 = price3(soup3)
title3 = title3(soup3)
rating3 = rating3(soup3)

#############
#PRODUCT 5
#############
price4 = price4(soup4)
title4 = title4(soup4)
rating4 = rating4(soup4)

#############
#PRODUCT 6
#############
price5 = price5(soup5)
title5 = title5(soup5)
rating5 = rating5(soup5)


@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/products')
def Products():
    return render_template('products.html', main = [price,title,rating], 
    main1 = [price1,title1,rating1], main2 = [price2,title2,rating2],
    main3 = [price3,title3,rating3] , main4 = [price4,title4,rating4],
    main5 = [price5,title5,rating5])




if __name__ == "__main__":
    app.run()