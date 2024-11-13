from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Path to your ChromeDriver
# driver_path = "path/to/your/chromedriver"

# Initialize the Chrome browser using Selenium WebDriver
driver = webdriver.Chrome()

# Open the Alibaba website with the search for 'paracord'
url = "https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=paracord&viewtype=&tab="
driver.get(url)

# Wait for the page to load completely
time.sleep(5)

# List to store scraped data
data = []

# Scraping loop for scrolling and collecting data
scroll_pause_time = 2  # Time to wait before scrolling further
scroll_height = driver.execute_script("return document.body.scrollHeight")

# Scroll and scrape data multiple times
while True:
    # Find product elements on the current page
    products = driver.find_elements(By.XPATH, '//div[@class="elements-title-normal__content"]')

    # Iterate over the products and extract details
    for product in products:
        try:
            # Extract product name
            product_name = product.text.strip()

            # Extract the product URL
            product_link = product.find_element(By.XPATH, './a').get_attribute("href")

            # Extract price (if available)
            price_element = product.find_element(By.XPATH, './ancestor::div[@class="organic-gallery-title"]/following-sibling::div[@class="price"]')
            price = price_element.text if price_element else "N/A"

            # Append the data to the list
            data.append([product_name, price, product_link])
        except Exception as e:
            print(f"Error extracting data: {e}")
    
    # Scroll down to load more products
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)  # Wait for the new content to load

    # Check if new products are loaded (scroll height has increased)
    new_scroll_height = driver.execute_script("return document.body.scrollHeight")
    if new_scroll_height == scroll_height:
        print("No more pages to load.")
        break
    scroll_height = new_scroll_height

# Convert the data into a DataFrame
df = pd.DataFrame(data, columns=["Product Name", "Price", "Product Link"])

# Save the DataFrame to a CSV file
df.to_csv("paracord_products.csv", index=False)

# Close the browser
driver.quit()

print("Scraping complete! Data saved to paracord_products.csv")
