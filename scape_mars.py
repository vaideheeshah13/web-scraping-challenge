# Import Dependecies 
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd 
import webdriver_manager.chrome import ChromeDriverManager
import requests 

# Initialize browser
def init_browser(): 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Mac Users
    #executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    #return Browser('chrome', **executable_path, headless=False)


# dictionary imported into Mongo 
def scrape():
    browser = init_browser()
    mars_dict = {}

# NASA MARS NEWS
def scrape_mars_news():

        # Initialize browser 
        browser = init_browser()
        url = "https://redplanetscience.com/"
        browser.visit(url)
        html = browser.html
        soup = bs(html, 'html.parser')


        #latest news title and news_paragraph
        news_title = soup.find('div', class_="content_title").text
        news_p = soup.find('div', class_="article_teaser_body").text

        # Dictionary entry from MARS NEWS
        mars_dict'news_title'] = news_title
        mars_dict['news_paragraph'] = news_p

        return mars_dict

        browser.quit()

# FEATURED IMAGE
def scrape_mars_image():


        # Initialize browser 
        browser = init_browser()
        url = 'https://spaceimages-mars.com'
        browser.visit(url)

        # HTML Object 
        html = browser.html
        soup = bs(html, "html.parser")

        #featured image
        featured_image_url = soup.find('img', class_="headerimage")['src']
        featured_image_url = f'{url}{featured_image_url}'
    
        mars_dict['featured_image_url'] = featured_image_url 
        
        return mars_dict

        browser.quit()

# Mars Facts
def scrape_mars_facts():

    # Visit Mars facts url 
    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url)
    table = pd.read_html(facts_url) 


    table_df = table[0]
    table_html = table_df.to_html()
    table_html = table_html.replace('\n', '')


    # Dictionary entry from MARS FACTS
    mars_dict['mars_facts'] = table_html

    return mars_dict


# MARS HEMISPHERES


def scrape_mars_hemispheres():

        # Initialize browser 
        browser = init_browser()

        hemispheres_images_url = 'https://marshemispheres.com/'
        
        browser.visit(hemispheres_images_url)
        
        html_hemispheres = browser.html
        
        soup = bs(html_hemispheres, 'html.parser')
        
        items = soup.find_all('div', class_='item')

        hemisphere_image_urls=[]
        
        # links = browser.find_by_css("a.product-item img")
    
    for i in range(4):
        hemisphere_dict = {}
        browser.find_by_css("a.product-item img")[i].click()
        sample = browser.find_by_text("Sample").first
        hemisphere_dict["img_url"]=sample["href"]
        hemisphere_dict["title"]=browser.find_by_css("h2.title").text
        hemisphere_image_urls.append(hemisphere_dict)
        browser.back()
       

        mars_dict['hemispheres_images_url'] = hemispheres_images_url


        return mars_dict

        browser.quit()