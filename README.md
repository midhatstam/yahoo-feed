# Yahoo Finance: scraping news and fetching api

## Installation:

- #### With docker
    - Run commands inside project root folder:
        - `docker-compose up --build`
    

## API:
### GET `/api/news`
- Fetching news with pagination and filter enabled.
- Usable filters as query param: `ticker`, `region`, `guid`.
  * Example: `http://localhost:8000/api/news?ticker=AAPL&region=US`
- No authentication (_AllowAny_ permission)

## Admin dashboard:
Tasks can be created in admin dashboard in "Periodic tasks" menu.

- URL: `http://localhost:8000/admin`
- Username: `admin`
- Password: `admin`

### Task parameters example to provide (must be in JSON format):
- News Collector Task:
    - **kwargs**: {"ticker": "AAPL", "region": "US", "lang": "en-US"}
    
- News Collector Dispatch Task:
    - **kwargs**: {"tickers": ["AAPL", "YHOO", "MSFT"], "region": "US", "lang": "en-US"}

