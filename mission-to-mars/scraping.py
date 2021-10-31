# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt
import requests
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres": mars_hemispheres(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):
   # Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    try:
        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first <a> tag and save it as  `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url


def mars_facts():
    try:
        # use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
    
    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns = ['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HMTL format, and bootstrap
    return df.to_html(classes="table table-bordered table-hover")


def mars_hemispheres(browser):
    """
    Return list of dictionaries of the four Mars hemisphere images and titles

    args:
        browser: Splinter browser object for web scraping
    """

    # 1. Use browser to visit the URL 
    url = 'https://marshemispheres.com/'

    # retrieve page
    response = requests.get(url)

    # create Beautiful soup object
    hemisphere_soup = soup(response.text, 'html.parser')

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    results = hemisphere_soup.find_all('div', class_='item')

    # Loop through results
    for result in results:
        try:
            # get link to enhanced image
            link = result.a['href']
            image_url = f"{url}{link}"
            #print(image_url)
            
            # visit image url
            browser.visit(image_url)
            
            # initialize Beautiful soup objet
            html = browser.html
            soup_img_download = soup(html, 'html.parser')
            
            # get full image tag
            full_image_tag = soup_img_download.find('a', text='Sample')
            
            # get full image href
            full_image_href = f"{url}{full_image_tag['href']}"
            print(full_image_href)
            
            # get title of enhanced image
            title = result.find('h3').text
            
            # Add to dictionary to image list
            hemisphere_image_urls.append({'img_url':full_image_href, 'title':title})
        except Exception as e:
            print(e)

    return hemisphere_image_urls


if __name__ == "__main__":
    #If running as script, print scraped data
    print(scrape_all())
