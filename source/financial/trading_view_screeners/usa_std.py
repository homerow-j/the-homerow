import os
import pandas as pd
from tradingview_screener import Query, col


c_datetime = pd.to_datetime('today')


cookies = {'sessionid': 'xnz2deqpdijl3xrxr442cqi531cjht8i'}


def check_csv_dir():
    if not os.path.isdir("csv"):
        os.makedirs("csv")


def usa_best_performing():
    query_name_bp = "USA_Best_Performing"
    query_bp = (Query()
                .select(
        'name',
        'description',
        'logoid',
        'update_mode',
        'type',
        'typespecs',
        'Perf.Y',
        'close',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'currency',
        'change',
        'volume',
        'market_cap_basic',
        'fundamental_currency_code',
        'price_earnings_ttm',
        'earnings_per_share_diluted_ttm',
        'earnings_per_share_diluted_yoy_growth_ttm',
        'dividends_yield_current',
        'sector.tr',
        'sector',
        'market',
        'recommendation_mark',
        'relative_volume_10d_calc',
    )
        .where(
        col('exchange').isin(['AMEX', 'CBOE', 'NASDAQ', 'NYSE']),
        col('is_primary') == True,
        col('typespecs').has('common'),
        col('typespecs').has_none_of('preferred'),
        col('type') == 'stock',
        col('active_symbol') == True,
        col('market_cap_basic') > 0,
    )
        .order_by('Perf.Y', ascending=False, nulls_first=False)
        .limit(100)
        .set_markets('america')
        .set_property('preset', 'best_performing')
        .set_property('symbols', {'query': {'types': ['stock', 'fund', 'dr', 'structured']}})
        .get_scanner_data(cookies=cookies))
    query_data_bp = pd.DataFrame(
        query_bp[1],
        columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'Perf.Y', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'currency', 'change', 'volume', 'market_cap_basic', 'fundamental_currency_code', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'sector', 'market', 'recommendation_mark', 'relative_volume_10d_calc'])
    query_data_bp.to_csv(f"csv/{c_datetime}_{query_name_bp}.csv")


def usa_biggest_losers():
    query_name_bl = "USA_Biggest_Losers"
    query_bl = (Query().select(
        'name',
        'description',
        'logoid',
        'update_mode',
        'type',
        'typespecs',
        'market_cap_basic',
        'fundamental_currency_code',
        'close',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'currency',
        'change',
        'volume',
        'price_earnings_ttm',
        'earnings_per_share_diluted_ttm',
        'earnings_per_share_diluted_yoy_growth_ttm',
        'dividends_yield_current',
        'sector.tr',
        'sector',
        'market',
        'recommendation_mark',
        'relative_volume_10d_calc',
    )
        .where(
        col('exchange').isin(['AMEX', 'CBOE', 'NASDAQ', 'NYSE']),
        col('is_primary') == True,
        col('typespecs').has('common'),
        col('typespecs').has_none_of('preferred'),
        col('type') == 'stock',
        col('close').between(2, 10000),
        col('change') < 0,
        col('active_symbol') == True,
    )
        .order_by('change', ascending=True, nulls_first=False)
        .limit(100)
        .set_markets('america')
        .set_property('symbols', {'query': {'types': ['stock', 'fund', 'dr', 'structured']}})
        .set_property('preset', 'losers')
        .get_scanner_data(cookies=cookies))
    query_data_bl = pd.DataFrame(
        query_bl[1],
        columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'market_cap_basic', 'fundamental_currency_code', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'currency', 'change', 'volume', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'sector', 'market', 'recommendation_mark', 'relative_volume_10d_calc'])
    query_data_bl.to_csv(f"csv/{c_datetime}_{query_name_bl}.csv")


def usa_highest_cash():
    query_name_hc = "USA_Highest_Cash"
    query_hc = (Query().select(
        'name',
        'description',
        'logoid',
        'update_mode',
        'type',
        'typespecs',
        'cash_n_short_term_invest_fq',
        'fundamental_currency_code',
        'close',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'currency',
        'change',
        'volume',
        'market_cap_basic',
        'price_earnings_ttm',
        'earnings_per_share_diluted_ttm',
        'earnings_per_share_diluted_yoy_growth_ttm',
        'dividends_yield_current',
        'sector.tr',
        'sector',
        'market',
        'recommendation_mark',
        'relative_volume_10d_calc',
    )
        .where(
        col('exchange').isin(['AMEX', 'CBOE', 'NASDAQ', 'NYSE']),
        col('is_primary') == True,
        col('typespecs').has('common'),
        col('typespecs').has_none_of('preferred'),
        col('type') == 'stock',
    )
        .order_by('cash_n_short_term_invest_fq', ascending=False, nulls_first=False)
        .limit(100)
        .set_markets('america')
        .set_property('symbols', {'query': {'types': ['stock', 'fund', 'dr', 'structured']}})
        .set_property('preset', 'highest_cash')
        .get_scanner_data(cookies=cookies))
    query_data_hc = pd.DataFrame(
        query_hc[1],
        columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'cash_n_short_term_invest_fq', 'fundamental_currency_code', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'currency', 'change', 'volume', 'market_cap_basic', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'sector', 'market', 'recommendation_mark', 'relative_volume_10d_calc'])
    query_data_hc.to_csv(f"csv/{c_datetime}_{query_name_hc}.csv")


def usa_most_active():
    query_name_ma = "USA_Most_Active"
    query_ma = (Query().select(
        'name',
        'description',
        'logoid',
        'update_mode',
        'type',
        'typespecs',
        'Value.Traded',
        'currency',
        'close',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'change',
        'volume',
        'relative_volume_10d_calc',
        'market_cap_basic',
        'fundamental_currency_code',
        'price_earnings_ttm',
        'earnings_per_share_diluted_ttm',
        'earnings_per_share_diluted_yoy_growth_ttm',
        'dividends_yield_current',
        'sector.tr',
        'market',
        'sector',
        'recommendation_mark',
    )
        .where(
        col('exchange').isin(['AMEX', 'CBOE', 'NASDAQ', 'NYSE']),
        col('is_primary') == True,
        col('typespecs').has('common'),
        col('typespecs').has_none_of('preferred'),
        col('type') == 'stock',
        col('close').between(2, 10000),
        col('active_symbol') == True,
    )
        .order_by('Value.Traded', ascending=False, nulls_first=False)
        .limit(100)
        .set_markets('america')
        .set_property('symbols', {'query': {'types': ['stock', 'fund', 'dr', 'structured']}})
        .set_property('preset', 'volume_leaders')
        .get_scanner_data(cookies=cookies))
    query_data_ma = pd.DataFrame(
        query_ma[1],
        columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'Value.Traded', 'currency', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'change', 'volume', 'relative_volume_10d_calc', 'market_cap_basic', 'fundamental_currency_code', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'market', 'sector', 'recommendation_mark'])
    query_data_ma.to_csv(f"csv/{c_datetime}_{query_name_ma}.csv")


def usa_most_volatile():
    query_name_mv = "USA_Most_Volatile"
    query_mv = (Query()
                .select(
        'name',
        'description',
        'logoid',
        'update_mode',
        'type',
        'typespecs',
        'Volatility.D',
        'close',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'currency',
        'change',
        'volume',
        'market_cap_basic',
        'fundamental_currency_code',
        'price_earnings_ttm',
        'earnings_per_share_diluted_ttm',
        'earnings_per_share_diluted_yoy_growth_ttm',
        'dividends_yield_current',
        'sector.tr',
        'sector',
        'market',
        'recommendation_mark',
        'relative_volume_10d_calc',
    )
        .where(
        col('exchange').isin(['AMEX', 'CBOE', 'NASDAQ', 'NYSE']),
        col('is_primary') == True,
        col('typespecs').has('common'),
        col('typespecs').has_none_of('preferred'),
        col('type') == 'stock',
        col('active_symbol') == True,
    )
        .order_by('Volatility.D', ascending=False, nulls_first=False)
        .limit(100)
        .set_markets('america')
        .set_property('symbols', {'query': {'types': ['stock', 'fund', 'dr', 'structured']}})
        .set_property('preset', 'most_volatile')
        .get_scanner_data(cookies=cookies))
    query_data_mv = pd.DataFrame(
        query_mv[1],
        columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'Volatility.D', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'currency', 'change', 'volume', 'market_cap_basic', 'fundamental_currency_code', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'sector', 'market', 'recommendation_mark', 'relative_volume_10d_calc'])
    query_data_mv.to_csv(f"csv/{c_datetime}_{query_name_mv}.csv")


def usa_premarket_gainers():
    query_name_pg = "USA_PreMarket_Gainers"
    query_pg = (Query()
                .select(
        'logoid',
        'name',
        'premarket_close',
        'premarket_change_abs',
        'premarket_change',
        'premarket_volume',
        'premarket_gap',
        'close',
        'change',
        'volume',
        'market_cap_basic',
        'Perf.1Y.MarketCap',
        'description',
        'type',
        'typespecs',
        'update_mode',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'fundamental_currency_code',
        'currency',
    )
        .where(
        col('exchange').isin(['AMEX', 'CBOE', 'NASDAQ', 'NYSE']),
        col('is_primary') == True,
        col('typespecs').has('common'),
        col('typespecs').has_none_of('preferred'),
        col('type') == 'stock',
        col('premarket_change') > 0,
        col('premarket_change').not_empty(),
        col('active_symbol') == True,
    )
        .order_by('premarket_change', ascending=False, nulls_first=False)
        .limit(100)
        .set_markets('america')
        .set_property('symbols', {'query': {'types': ['stock', 'fund', 'dr', 'structured']}})
        .set_property('preset', 'pre-market-gainers')
        .get_scanner_data(cookies=cookies))
    query_data_pg = pd.DataFrame(
        query_pg[1],
        columns=['ticker', 'logoid', 'name', 'premarket_close', 'premarket_change_abs', 'premarket_change', 'premarket_volume', 'premarket_gap', 'close', 'change', 'volume', 'market_cap_basic', 'Perf.1Y.MarketCap', 'description', 'type', 'typespecs', 'update_mode', 'pricescale', 'minmov', 'fractional', 'minmove2', 'fundamental_currency_code', 'currency'])
    query_data_pg.to_csv(f"csv/{c_datetime}_{query_name_pg}.csv")


def usa_premarket_gap():
    query_name_pmg = "USA PreMarket_Gap"
    query_pmg = (Query()
                 .select(
        'logoid',
        'name',
        'premarket_close',
        'premarket_change_abs',
        'premarket_change',
        'premarket_volume',
        'premarket_gap',
        'close',
        'change',
        'volume',
        'market_cap_basic',
        'Perf.1Y.MarketCap',
        'description',
        'type',
        'typespecs',
        'update_mode',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'fundamental_currency_code',
        'currency',
    )
        .where(
        col('exchange').isin(['AMEX', 'CBOE', 'NASDAQ', 'NYSE']),
        col('is_primary') == True,
        col('typespecs').has('common'),
        col('typespecs').has_none_of('preferred'),
        col('type') == 'stock',
        col('premarket_gap').not_empty(),
        col('active_symbol') == True,
    )
        .order_by('premarket_gap', ascending=False, nulls_first=False)
        .limit(100)
        .set_markets('america')
        .set_property('symbols', {'query': {'types': ['stock', 'fund', 'dr', 'structured']}})
        .set_property('preset', 'pre_market_gappers')
        .get_scanner_data(cookies=cookies))
    query_data_pmg = pd.DataFrame(
        query_pmg[1],
        columns=['ticker', 'logoid', 'name', 'premarket_close', 'premarket_change_abs', 'premarket_change', 'premarket_volume', 'premarket_gap', 'close', 'change', 'volume', 'market_cap_basic', 'Perf.1Y.MarketCap', 'description', 'type', 'typespecs', 'update_mode', 'pricescale', 'minmov', 'fractional', 'minmove2', 'fundamental_currency_code', 'currency'])
    query_data_pmg.to_csv(f"csv/{c_datetime}_{query_name_pmg}.csv")


def usa_premarket_losers():
    query_name_pml = "USA_PreMarket_Losers"
    query_pml = (Query()
                 .select(
        'logoid',
        'name',
        'premarket_close',
        'premarket_change_abs',
        'premarket_change',
        'premarket_volume',
        'premarket_gap',
        'close',
        'change',
        'volume',
        'market_cap_basic',
        'Perf.1Y.MarketCap',
        'description',
        'type',
        'typespecs',
        'update_mode',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'fundamental_currency_code',
        'currency',
    )
        .where(
        col('exchange').isin(['AMEX', 'CBOE', 'NASDAQ', 'NYSE']),
        col('is_primary') == True,
        col('typespecs').has('common'),
        col('typespecs').has_none_of('preferred'),
        col('type') == 'stock',
        col('premarket_change') < 0,
        col('premarket_change').not_empty(),
        col('active_symbol') == True,
    )
        .order_by('premarket_change', ascending=True, nulls_first=False)
        .limit(100)
        .set_markets('america')
        .set_property('symbols', {'query': {'types': ['stock', 'fund', 'dr', 'structured']}})
        .set_property('preset', 'pre-market-losers')
        .get_scanner_data(cookies=cookies))
    query_data_pml = pd.DataFrame(
        query_pml[1],
        columns=['ticker', 'logoid', 'name', 'premarket_close', 'premarket_change_abs', 'premarket_change', 'premarket_volume', 'premarket_gap', 'close', 'change', 'volume', 'market_cap_basic', 'Perf.1Y.MarketCap', 'description', 'type', 'typespecs', 'update_mode', 'pricescale', 'minmov', 'fractional', 'minmove2', 'fundamental_currency_code', 'currency'])
    query_data_pml.to_csv(f"csv/{c_datetime}_{query_name_pml}.csv")


def usa_premarket_most_active():
    query_name_pma = "USA_PreMarket_Most_Active"
    query_pma = (Query()
                 .select(
        'logoid',
        'name',
        'premarket_close',
        'premarket_change_abs',
        'premarket_change',
        'premarket_volume',
        'premarket_gap',
        'close',
        'change',
        'volume',
        'market_cap_basic',
        'Perf.1Y.MarketCap',
        'description',
        'type',
        'typespecs',
        'update_mode',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'fundamental_currency_code',
        'currency',
    )
        .where(
        col('exchange').isin(['AMEX', 'CBOE', 'NASDAQ', 'NYSE']),
        col('is_primary') == True,
        col('typespecs').has('common'),
        col('typespecs').has_none_of('preferred'),
        col('type') == 'stock',
        col('premarket_volume').not_empty(),
        col('active_symbol') == True,
    )
        .order_by('premarket_volume', ascending=False, nulls_first=False)
        .limit(100)
        .set_markets('america')
        .set_property('symbols', {'query': {'types': ['stock', 'fund', 'dr', 'structured']}})
        .set_property('preset', 'pre_market_most_active')
        .get_scanner_data(cookies=cookies))
    query_data_pma = pd.DataFrame(
        query_pma[1],
        columns=['ticker', 'logoid', 'name', 'premarket_close', 'premarket_change_abs', 'premarket_change', 'premarket_volume', 'premarket_gap', 'close', 'change', 'volume', 'market_cap_basic', 'Perf.1Y.MarketCap', 'description', 'type', 'typespecs', 'update_mode', 'pricescale', 'minmov', 'fractional', 'minmove2', 'fundamental_currency_code', 'currency'])
    query_data_pma.to_csv(f"csv/{c_datetime}_{query_name_pma}.csv")


def usa_top_gainers():
    query_name_tg = "USA_Top_Gainers"
    query_tg = (Query()
                .select(
        'name',
        'description',
        'logoid',
        'update_mode',
        'type',
        'typespecs',
        'market_cap_basic',
        'fundamental_currency_code',
        'close',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'currency',
        'change',
        'volume',
        'price_earnings_ttm',
        'earnings_per_share_diluted_ttm',
        'earnings_per_share_diluted_yoy_growth_ttm',
        'dividends_yield_current',
        'sector.tr',
        'sector',
        'market',
        'recommendation_mark',
        'relative_volume_10d_calc',
    )
        .where(
        col('exchange').isin(['AMEX', 'CBOE', 'NASDAQ', 'NYSE']),
        col('is_primary') == True,
        col('typespecs').has('common'),
        col('typespecs').has_none_of('preferred'),
        col('type') == 'stock',
        col('close').between(2, 10000),
        col('change') > 0,
        col('active_symbol') == True,
    )
        .order_by('change', ascending=False, nulls_first=False)
        .limit(100)
        .set_markets('america')
        .set_property('symbols', {'query': {'types': ['stock', 'fund', 'dr', 'structured']}})
        .set_property('preset', 'gainers')
        .get_scanner_data(cookies=cookies))
    query_data_tg = pd.DataFrame(
        query_tg[1],
        columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'market_cap_basic', 'fundamental_currency_code', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'currency', 'change', 'volume', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'sector', 'market', 'recommendation_mark', 'relative_volume_10d_calc'])
    query_data_tg.to_csv(f"csv/{c_datetime}_{query_name_tg}.csv")


def usa_unusual_volume():
    query_name_uv = "USA_Unusual_Volume"
    query_uv = (Query()
                .select(
        'name',
        'description',
        'logoid',
        'update_mode',
        'type',
        'typespecs',
        'relative_volume_10d_calc',
        'close',
        'pricescale',
        'minmov',
        'fractional',
        'minmove2',
        'currency',
        'change',
        'volume',
        'market_cap_basic',
        'fundamental_currency_code',
        'price_earnings_ttm',
        'earnings_per_share_diluted_ttm',
        'earnings_per_share_diluted_yoy_growth_ttm',
        'dividends_yield_current',
        'sector.tr',
        'sector',
        'market',
        'recommendation_mark',
    )
        .where(
        col('exchange').isin(['AMEX', 'CBOE', 'NASDAQ', 'NYSE']),
        col('is_primary') == True,
        col('typespecs').has('common'),
        col('typespecs').has_none_of('preferred'),
        col('type') == 'stock',
        col('active_symbol') == True,
    )
        .order_by('relative_volume_10d_calc', ascending=False, nulls_first=False)
        .limit(100)
        .set_markets('america')
        .set_property('symbols', {'query': {'types': ['stock', 'fund', 'dr', 'structured']}})
        .set_property('preset', 'unusual_volume')
        .get_scanner_data(cookies=cookies))
    query_data_uv = pd.DataFrame(
        query_uv[1],
        columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'relative_volume_10d_calc', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'currency', 'change', 'volume', 'market_cap_basic', 'fundamental_currency_code', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'sector', 'market', 'recommendation_mark'])
    query_data_uv.to_csv(f"csv/{c_datetime}_{query_name_uv}.csv")


def usa_std():
    check_csv_dir()
    usa_best_performing()
    usa_biggest_losers()
    usa_highest_cash()
    usa_most_active()
    usa_most_volatile()
    usa_premarket_gainers()
    usa_premarket_gap()
    usa_premarket_losers()
    usa_premarket_most_active()
    usa_top_gainers()
    usa_unusual_volume()


usa_std()
