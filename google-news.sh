#!/bin/bash
cd ~/Work/nobias/source/article_scraper
source .venv/bin/activate
mkdir urls
scrapy crawl google-news -a keyword="FB stock news" -o urls/facebook.csv
scrapy crawl google-news -a keyword="GOOGL stock news" -o urls/google.csv
scrapy crawl google-news -a keyword="AAPL stock news" -o urls/apple.csv
scrapy crawl google-news -a keyword="AMZN stock news" -o urls/amazon.csv
scrapy crawl google-news -a keyword="NFLX stock news" -o urls/netflix.csv
