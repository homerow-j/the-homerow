# Source/Financial

## USA Ten Base Metrics Day Fetch
* `usa_ten_base_metrics-day-fetch.py`: is a python script using the [tradingview_screener](https://pypi.org/project/tradingview-screener/) library. This script should be a module of classes aka library itself! Bear me with me as Iam only learning to be a programmer as I pretend to be one. It gather the day data for ten metrics: _Best Performing, Biggest Losers, Highest Cash, Most Active, Most Volatile, PreMarket Gainers, PreMarket Gap, PreMarket Losers, Premarket Most Active, Top Gainers, Unusual Volume_. It fetches each one, exports it to a `.csv` file and then reads each `.csv` file and commits the resulting table to a SQLite database. As the `tradingview_screener` library returns a DataFrame in a tuple this is a quick and easy way to work around that as the `.csv` is a table and `pandas` imports and exports it as a table.

In the beginning of the file are some variables that should be looked at and adjusted. First is the `cookies` which is your `sessionid` from your [Trading View] account. Look here how to get it: [docs](https://github.com/shner-elmo/TradingView-Screener/blob/master/README.md#other-ways-for-loading-cookies).

The other two are `csv_dir` and `db_dir` which determine where to put the respective spreadsheet and database files.

If running on a unix system that using the `env` (usually /usr/bin/env) program then the script can be run on in the terminal without calling pyhon directly in the command line. Good for scripting. More should use the decades old built-in shebang of shells on unix systems.

## YFinance Fetcher notebook
* `yfinance_fetcher.ipynb`: to quote myself "_A simple notebook for fetching market data from Yahoo! Finance, simply._"

An interactive way to fetch specific market data using the  python [yfinance](https://pypi.org/project/yfinance/) library. It's use is documentated in the notebook.
