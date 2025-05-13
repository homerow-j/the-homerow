# Polygot Moving Averages (PMA)

## Description

This is essentially a source merger of Bollinger Bands by Trading View and Simple Moving Averages by stoxxinbox. My additions and subtractions are minimal. There is the BB MA, which I default at 5d, and the other 4 averages are the standard 21, 50, 100, 200, day moving averages. I default the averaging method to WMA (Weighted Moving Average). The method of averaging can be changed as also can the lengths of the inputs to match user preferences. This is what I wanted for an indicator and didn't find.

## Usage

The same as you would use any other BB or MA indicator. The benefit of this one is that it has 4 MAs, one MA with the Bollinger Bands attached, and the colours adjusted to be easy on the eyes when using high contrast themes, to be discernible yet sit quietly in the background with lines and candle sticks everywhere shouting for attention. I use it as a base first indicator which I can hide easily (imagine hiding five MA indicators individually constantly) when the more serious indicators come into play.

#### Source: https://www.tradingview.com/script/3vZk2XQO-Polygot-Moving-Averages/

```
// This Pine Script® code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © homerow_j, and the Trading View community I copied, mnodified and learnt from.
//@version=6
// Taken from the indicator sources of Bollinger Bands by Trading View and Simple Moving Averages by stoxxinbox, and
// modified (cut, copied, merged with a few changes) by homerow_j. 

indicator("Polygot Moving Averages", shorttitle="PMA", overlay=true, timeframe="", timeframe_gaps=true)
length = input.int(5, minval=1)
src = input(close, title="Source")
mult = input.float(1.5, minval=0.001, maxval=50, title="StdDev")
maType = input.string("WMA", "Moving Average Type", options = ["SMA", "EMA", "SMMA (RMA)", "WMA", "VWMA"])

ma(source, length, _type) =>
    switch _type
        "SMA" => ta.sma(source, length)
        "EMA" => ta.ema(source, length)
        "SMMA (RMA)" => ta.rma(source, length)
        "WMA" => ta.wma(source, length)
        "VWMA" => ta.vwma(source, length)

dev = mult * ta.stdev(src, length)
offset = input.int(0, "Offset", minval = -500, maxval = 500, display = display.data_window)

len1 = input.int(5, minval=1, title="BB MA Length")
src1 = input(close, title="BB MA Source")
out1 = ma(src1, len1, maType)
upper = out1 + dev
lower = out1 - dev
plot(out1, title="BB MA", color=#5e81ac)
p1 = plot(upper, "BB Upper", color=#8fbcbb, offset = offset)
p2 = plot(lower, "BB Lower", color=#88c0d0, offset = offset)
fill(p1, p2, title = "BB Fill Colour", color=color.rgb(53.3, 75.3, 81.6, 75))

len2 = input.int(21, minval=1, title="21d MA Length")
src2 = input(close, title="21d MA Source")
out2 = ma(src2, len2, maType)
plot(out2, title="21d MA", color=#a3b38c)

len3 = input.int(50, minval=1, title="50d MA Length")
src3 = input(close, title="50d MA Source")
out3 = ma(src3, len3, maType)
plot(out3, title="50d MA", color=#b48ead)

len4 = input.int(100, minval=1, title="100d MA Length")
src4 = input(close, title="100d MA Source")
out4 = ma(src4, len4, maType)
plot(out4, title="100d MA", color=#d08770) 

len5 = input.int(200, minval=1, title="200d MA Length")
src5 = input(close, title="200d MA Source")
out5 = ma(src5, len5, maType)
plot(out5, title="200d MA", color=#ebcb8b)
```

