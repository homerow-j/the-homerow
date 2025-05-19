#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
from tradingview_screener import Query, col

c_datetime = pd.to_datetime('today')
c_date = c_datetime.date()
cookies = {'sessionid': 'xnz2deqpdijl3xrxr442cqi531cjht8i'}

query_name = "USA_Best_Performing"
df_query_bp = (Query()
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
df_query_data_bp = pd.DataFrame(
    df_query_bp[1],
    columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'Perf.Y', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'currency', 'change', 'volume', 'market_cap_basic', 'fundamental_currency_code', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'sector', 'market', 'recommendation_mark', 'relative_volume_10d_calc'])
df_query_data_bp.to_csv(f"csv/{c_date}_{query_name}.csv")


query_name = "USA_Biggest_Losers"
df_query_bl = (Query().select(
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
df_query_data_bl = pd.DataFrame(
    df_query_bl[1],
    columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'market_cap_basic', 'fundamental_currency_code', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'currency', 'change', 'volume', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'sector', 'market', 'recommendation_mark', 'relative_volume_10d_calc'])
df_query_data_bl.to_csv(f"csv/{c_date}_{query_name}.csv")


query_name = "USA_Highest_Cash"
df_query_hc = (Query().select(
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
df_query_data_hc = pd.DataFrame(
    df_query_hc[1],
    columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'cash_n_short_term_invest_fq', 'fundamental_currency_code', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'currency', 'change', 'volume', 'market_cap_basic', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'sector', 'market', 'recommendation_mark', 'relative_volume_10d_calc'])
df_query_data_hc.to_csv(f"csv/{c_date}_{query_name}.csv")


query_name = "USA_Most_Active"
df_query_ma = (Query().select(
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
df_query_data_ma = pd.DataFrame(
    df_query_ma[1],
    columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'Value.Traded', 'currency', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'change', 'volume', 'relative_volume_10d_calc', 'market_cap_basic', 'fundamental_currency_code', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'market', 'sector', 'recommendation_mark'])
df_query_data_ma.to_csv(f"csv/{c_date}_{query_name}.csv")


query_name = "USA_Most_Volatile"
df_query_mv = (Query()
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
df_query_data_mv = pd.DataFrame(
    df_query_mv[1],
    columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'Volatility.D', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'currency', 'change', 'volume', 'market_cap_basic', 'fundamental_currency_code', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'sector', 'market', 'recommendation_mark', 'relative_volume_10d_calc'])
df_query_data_mv.to_csv(f"csv/{c_date}_{query_name}.csv")


query_name = "USA_PreMarket_Gainers"
df_query_pg = (Query()
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
df_query_data_pg = pd.DataFrame(
    df_query_pg[1],
    columns=['ticker', 'logoid', 'name', 'premarket_close', 'premarket_change_abs', 'premarket_change', 'premarket_volume', 'premarket_gap', 'close', 'change', 'volume', 'market_cap_basic', 'Perf.1Y.MarketCap', 'description', 'type', 'typespecs', 'update_mode', 'pricescale', 'minmov', 'fractional', 'minmove2', 'fundamental_currency_code', 'currency'])
df_query_data_pg.to_csv(f"csv/{c_date}_{query_name}.csv")


query_name = "USA PreMarket_Gap"
df_query_pmg = (Query()
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
df_query_data_pmg = pd.DataFrame(
    df_query_pmg[1],
    columns=['ticker', 'logoid', 'name', 'premarket_close', 'premarket_change_abs', 'premarket_change', 'premarket_volume', 'premarket_gap', 'close', 'change', 'volume', 'market_cap_basic', 'Perf.1Y.MarketCap', 'description', 'type', 'typespecs', 'update_mode', 'pricescale', 'minmov', 'fractional', 'minmove2', 'fundamental_currency_code', 'currency'])
df_query_data_pmg.to_csv(f"csv/{c_date}_{query_name}.csv")


query_name = "USA_PreMarket_Losers"
df_query_pl = (Query()
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
df_query_data_pl = pd.DataFrame(
    df_query_pl[1],
    columns=['ticker', 'logoid', 'name', 'premarket_close', 'premarket_change_abs', 'premarket_change', 'premarket_volume', 'premarket_gap', 'close', 'change', 'volume', 'market_cap_basic', 'Perf.1Y.MarketCap', 'description', 'type', 'typespecs', 'update_mode', 'pricescale', 'minmov', 'fractional', 'minmove2', 'fundamental_currency_code', 'currency'])
df_query_data_pl.to_csv(f"csv/{c_date}_{query_name}.csv")


query_name = "USA_PreMarket_Most_Active"
df_query_pma = (Query()
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
df_query_data_pma = pd.DataFrame(
    df_query_pma[1],
    columns=['ticker', 'logoid', 'name', 'premarket_close', 'premarket_change_abs', 'premarket_change', 'premarket_volume', 'premarket_gap', 'close', 'change', 'volume', 'market_cap_basic', 'Perf.1Y.MarketCap', 'description', 'type', 'typespecs', 'update_mode', 'pricescale', 'minmov', 'fractional', 'minmove2', 'fundamental_currency_code', 'currency'])
df_query_data_pma.to_csv(f"csv/{c_date}_{query_name}.csv")


query_name = "USA_Top_Gainers"
df_query_tg = (Query()
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
df_query_data_tg = pd.DataFrame(
    df_query_tg[1],
    columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'market_cap_basic', 'fundamental_currency_code', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'currency', 'change', 'volume', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'sector', 'market', 'recommendation_mark', 'relative_volume_10d_calc'])
df_query_data_tg.to_csv(f"csv/{c_date}_{query_name}.csv")


query_name = "USA_Unusual_Volume"
df_query_uv = (Query()
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
df_query_data_uv = pd.DataFrame(
    df_query_uv[1],
    columns=['ticker', 'name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'relative_volume_10d_calc', 'close', 'pricescale', 'minmov', 'fractional', 'minmove2', 'currency', 'change', 'volume', 'market_cap_basic', 'fundamental_currency_code', 'price_earnings_ttm', 'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm', 'dividends_yield_current', 'sector.tr', 'sector', 'market', 'recommendation_mark'])
df_query_data_uv.to_csv(f"csv/{c_date}_{query_name}.csv")
