from random import gauss
from random import seed
import numpy as np
import pandas as pd
from arch import arch_model
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import acf, pacf

seed(1)
prices = pd.read_csv('EOS.csv',header=0)
daily_return = prices['EOS'].pct_change(1)
daily_return = pd.Series(daily_return.dropna())
print(daily_return)

#daily_return = pd.Series(daily_return.to_numpy())
sqr = pd.Series([x**2 for x in daily_return])
pyplot.plot(sqr)
print(sqr)
# create acf plot
print("acf 1")
print(acf(pd.Series(daily_return),nlags=1,fft=False))
plot_acf(sqr)

pyplot.show()
garch11 = arch_model(daily_return, p=1, q=1)
res = garch11.fit(update_freq=10)
print(res.params)
# forecast the test set
yhat = res.forecast(horizon=30)
# plot the actual variance
#var = [i*0.01 for i in range(0,100)]
#pyplot.plot(var[-n_test:])
# plot forecast variance
pyplot.plot(yhat.variance.values[-1, :])
pyplot.show()
print(res.summary())
