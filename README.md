# article_scraper
This is a Scrapy project to scrape investment news from [https://fool.com](https://fool.com).


## Extracted data

This project extracts article url, combined with the article title, content, respective author names and published dates.
The extracted data looks like this sample:

    {
        'originalUrl': 'https://fool.com/retirement/plans/roth-401k/roth-401k-vs-roth-ira/',
        'authorName': 'Christy Bieber',
        'publishedDate': 'Sep 22, 2020',
        'title': 'Roth IRA vs. Roth 401(k): Which Is Best for You?',
        'content': 'Both the Roth 401(k) and the Roth IRA can help you reach your retirement goals. Each has its advantages and disadvantages.'
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
