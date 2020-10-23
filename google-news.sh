#!/bin/bash
cd {YOUR_WORKING_DIR}
source .venv/bin/activate
mkdir {OUTPUT_DIR}
scrapy crawl google-news -a keyword="FB stock news" -o {OUTPUT_DIR}/facebook.csv
scrapy crawl google-news -a keyword="GOOGL stock news" -o {OUTPUT_DIR}/google.csv
scrapy crawl google-news -a keyword="AAPL stock news" -o {OUTPUT_DIR}/apple.csv
scrapy crawl google-news -a keyword="AMZN stock news" -o {OUTPUT_DIR}/amazon.csv
scrapy crawl google-news -a keyword="NFLX stock news" -o {OUTPUT_DIR}/netflix.csv
