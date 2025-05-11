#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
import yfinance as yf

# =============================================================================
# Constants
# =============================================================================
SYMBOLS = 'AAPL', 'AMZN', 'GOOGL', 'META', 'MSFT', 'NVDA', 'TSLA'
T_PERIOD = '1d'
T_INTERVAL = '1h'

# =============================================================================
# Timestamp
# =============================================================================
c_datetime = pd.to_datetime('today')
c_date = c_datetime.date()

# =============================================================================
# Make csv directory if it does not exist.
# =============================================================================
if not os.path.isdir("csv"):
    os.makedirs("csv")

# =============================================================================
# Filter constants so filesystem friendly, i.e. no spaces and commas.
# ft = "friendly tickers"
# =============================================================================
ft = '-'.join(SYMBOLS)

# =============================================================================
# OHLC + Volumme Price Data
# =============================================================================
df_index = yf.download(f"{SYMBOLS}", group_by='ticker',
                       period=f"{T_PERIOD}", interval=f"{T_INTERVAL}",
                       rounding=True)

# =============================================================================
# Alternative Fetch by date range instead of the above offset.
# S_DATE = '2000-01-01'
# E_DATE = '2025-01-01'
#
# ds_df_index = yf.download(yf_fetcher, group_by='ticker', start=f"{S_DATE}",
#                           end=f"{E_DATE}", rounding=True)
# =============================================================================

# =============================================================================
# Export DataFrame to .csv and make file name string
# =============================================================================
ft = '-'.join(SYMBOLS)
df_index.to_csv(
    f"csv/{ft}_INDEX_{T_PERIOD}_{T_INTERVAL}_from_{c_datetime}.csv")

# =============================================================================
# A Collection Of Financial fetches.
# =============================================================================
# =============================================================================
# Single Ticker Variables And Constants
# =============================================================================
F_SYM = 'SPY'
S_SYM = 'TSLA'

df_stat_f = yf.Ticker(f"{F_SYM}")
df_stat = yf.Ticker(f"{S_SYM}")

# =============================================================================
# Multiple Ticker Variables And Constants
# =============================================================================
# =============================================================================
# F_SYM = 'SPY', 'VTI'
# S_SYM = 'TSLA', 'AAPL'
#
# df_stat_f = yf.Tickers(f"{F_SYM}")
# df_stat = yf.Tickers(f"{S_SYM}")
# =============================================================================

# =============================================================================
# Clean tickers to be file name friendly
# =============================================================================
cfft = '-'.join(F_SYM)
cft = '-'.join(S_SYM)

# =============================================================================
# Info
# =============================================================================
df_stat_i = df_stat.info
df_stat_i.to_csv(f"csv/{cft}-info-{c_datetime}.csv")

# =============================================================================
# ISIN (International Securities Identification Number)
# =============================================================================
df_stat_isin = df_stat.isin
df_stat_isin.to_csv(f"csv/{cft}-isin-{c_datetime}.csv")

# =============================================================================
# Analyst Price Targets
# =============================================================================
df_stat_apt = df_stat.analyst_price_targets
df_stat_apt.to_csv(f"csv/{cft}-analyst_price_targets-{c_datetime}.csv")

# =============================================================================
# Calendar
# =============================================================================
df_stat_cal = df_stat.calendar
df_stat_cal.to_csv(f"csv/{cft}-cal-{c_datetime}.csv")

# =============================================================================
# Financials
# =============================================================================
df_stat_fin = df_stat.financials
df_stat_fin.to_csv(f"csv/{cft}-financials-{c_datetime}.csv")

# =============================================================================
# Balance Sheet
# =============================================================================
df_stat_bs = df_stat.balance_sheet
df_stat_bs.to_csv(f"csv/{cft}-balance_sheet-{c_datetime}.csv")

# =============================================================================
# Income Statement
# =============================================================================
df_stat_stmt = df_stat.income_stmt
df_stat_stmt.to_csv(f"csv/{cft}-income_statement-{c_datetime}.csv")

# =============================================================================
# Cash Flow
# =============================================================================
df_stat_cf = df_stat.cash_flow
df_stat_cf.to_csv(f"csv/{cft}-cash_flow-{c_datetime}.csv")

# =============================================================================
# EPS Revisions
# =============================================================================
df_stat_e_rv = df_stat.eps_revisions
df_stat_e_rv.to_csv(f"csv/{cft}-eps_revisions-{c_datetime}.csv")

# =============================================================================
# EPS Trend
# =============================================================================
df_stat_et = df_stat.eps_trend
df_stat_et.to_csv(f"csv/{cft}-eps_trend-{c_datetime}.csv")

# =============================================================================
# SEC Filings
# =============================================================================
df_stat_sf = df_stat.sec_filings
df_stat_sf.to_csv(f"csv/{cft}-sec_filings-{c_datetime}.csv")

# =============================================================================
# Insider Transactions
# =============================================================================
df_stat_ins_t = df_stat.insider_transactions
df_stat_ins_t.to_csv(f"csv/{cft}-insider_transactions-{c_datetime}.csv")

# =============================================================================
# Insider Roster Holders
# =============================================================================
df_stat_rh = df_stat.insider_roster_holders
df_stat_rh.to_csv(f"csv/{cft}-inside_roster_holders-{c_datetime}.csv")

# =============================================================================
# Insider Pruchases
# =============================================================================
df_stat_ins_p = df_stat.insider_purchases
df_stat_ins_p.to_csv(f"csv/{cft}-insider_purchases-{c_datetime}.csv")

# =============================================================================
# Major Holders
# =============================================================================
df_stat_mh = df_stat.major_holders
df_stat_mh.to_csv(f"csv/{cft}-major_holders-{c_datetime}.csv")

# =============================================================================
# Institutional Holders
# =============================================================================
df_stat_ih = df_stat.institutional_holders
df_stat_ih.to_csv(f"csv/{cft}-instituional_holders-{c_datetime}.csv")

# =============================================================================
# Mutual Fund Holders
# =============================================================================
df_stat_mfh = df_stat.mutualfund_holders
df_stat_mfh.to_csv(f"csv/{cft}-mutualfund_holders-{c_datetime}.csv")

# =============================================================================
# Top Holdings -Funds
# =============================================================================
df_stat_th = df_stat_f.top_holdings
df_stat_th.to_csv(f"csv/{cfft}-top_holdings-funds-{c_datetime}.csv")
