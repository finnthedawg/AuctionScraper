import cfscrape
scraper = cfscrape.create_scraper()
web_data = scraper.get("https://www.directliquidation.com/electronics/?s=&idx=dl_prod_posts_product_end_date_ts_asc&page=10").content
print(web_data)