import requests
import pandas as pd


def foo(sym, tf):
    url = 'https://api.binance.com/api/v1/klines'
    pare = sym + 'USDT'
    param = {'symbol': pare, 'interval': tf}
    r = requests.get(url, params=param)
    if r.status_code == 200:
        df = pd.DataFrame(r.json())
        m = pd.DataFrame()
        m['date'] = df.iloc[:, 0]
        m['date'] = pd.to_datetime(m['date'], unit='ms')
        m['high'] = df.iloc[:, 2].astype(float)
        m['low'] = df.iloc[:, 3].astype(float)
        m['proc'] = ((m['high'] - m['low']) / m['low']) * 100
        m1 = m.loc[(m['proc'] > 1)]
        return m1
    else:
        return print('проверьте исходные данные')


print(foo('XRP', '1h'))





