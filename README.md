# article_scraper
This is a Scrapy project to scrape investment news from [https://fool.com](https://fool.com).


## Extracted data

This project extracts article url, combined with the article title, content, respective author names and published dates.
The extracted data looks like this sample:

    {
	originalUrl         https://www.fool.com/investing/2020/09/28/ford...
	url                 https://www.fool.com/investing/2020/09/28/ford...
	title               Ford Reveals Plans to Build Electric Vehicles ...
	content             Ford Motor Company (NYSE:F) has revealed plans...
	authorName                                              John Rosevear
	publishedDate                                    2020-09-28T18:47:00Z
	harvestDate                                      2020-09-28T21:38:41Z
	stockTicker                                                         F
	duplicateGroupId                                 S-502351933235786277
	index-date                                                 2020-09-28
	languageCode                                                       en
    }


## Spiders

This project contains two spiders and you can list them using the `list`
command:

    $ scrapy list
    fool-news
    fool-article

`fool-news` scrapes recent articles and `fool-article` scrapes individual articles from given urls.


## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl fool-news

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl fool-news -o news.csv

google-news.sh is for fetching google search urls. You will need to update it to point the correct directory.

If you want to run google-news.sh daily, run `crontab -e` and add

	0 8 * * *	bash {YOUR_WORKING_DIR}/google-news.sh
