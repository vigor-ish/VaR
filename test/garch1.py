import numpy as np
import pandas as pd
from arch import arch_model
from statsmodels.tsa.stattools import acf, pacf
prices = pd.read_csv('EOS.csv',header=0)
daily_return = prices['EOS'].pct_change(1).dropna()
garch11 = arch_model(daily_return, p=1, q=1)
res = garch11.fit(update_freq=10)
print(res.params)
res.params.to_csv('EOS_params.csv',header=0)
print("acf 1")
acf_ = acf(pd.Series(daily_return),nlags=1,fft=False)
acf_.to_csv('EOS_params.csv',header=0)

