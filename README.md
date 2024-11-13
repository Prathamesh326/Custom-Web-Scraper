
# Custom Web Scraper

A simple and customizable web scraper using **Selenium** and **Python** to scrape product data from e-commerce websites. This particular scraper is designed to extract product information (name, price, and link) from Alibaba, but it can be adapted to scrape other websites with minimal changes.

## Features

- Scrapes product name, price, and link from the search results page of Alibaba.
- Uses Selenium WebDriver for automating the browser and scrolling through the page.
- Handles dynamic content by scrolling and waiting for new products to load.
- Saves the scraped data into a CSV file.

## Installation

### Requirements

To run this scraper, you'll need:

- Python 3.x
- Chrome browser
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) (matching the version of your Chrome browser)
- Selenium library
- Pandas library

### Steps to Install

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Prathamesh326/Custom-Web-Scraper.git
   cd Custom-Web-Scraper
   ```

2. **Install Required Libraries**

   Install Selenium and Pandas using `pip`:

   ```bash
   pip install selenium pandas
   ```

3. **Download ChromeDriver**

   Ensure you have the correct version of ChromeDriver that matches your version of Google Chrome. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/).

4. **Configure ChromeDriver Path**

   Update the `driver_path` in the script with the path to your `chromedriver` executable.

   ```python
   driver_path = "path/to/your/chromedriver"
   ```

## Usage

1. Open `main.py` and modify the `driver_path` variable to point to your local `chromedriver` file.
   
2. Run the script:

   ```bash
   python main.py
   ```

3. The script will:

   - Open the browser and navigate to Alibaba's search results for "paracord."
   - Scroll through the page, collecting product names, prices, and links.
   - Save the scraped data to a CSV file called `paracord_products.csv`.

## Example Output

The output will be saved as `paracord_products.csv` with the following columns:

- **Product Name**: Name of the product.
- **Price**: The price of the product (if available).
- **Product Link**: Link to the product page on Alibaba.

```csv
Product Name, Price, Product Link
"Paracord 550", "$15.99", "https://www.alibaba.com/product-detail/Paracord-550_12345678.html"
"Survival Paracord", "$12.50", "https://www.alibaba.com/product-detail/Survival-Paracord_23456789.html"
...
```

## Contributing

Contributions are welcome! If you find any bugs or want to improve the scraper, feel free to fork the repository, create a pull request, and submit your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This scraper is designed for educational purposes. Be sure to follow the website's terms of service and scraping guidelines to ensure compliance with legal and ethical standards.
