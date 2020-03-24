pip install arch

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
%matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20, 6 

file = pd.ExcelFile(r"C:\Users\file_names.xlsx")
dataset = file.parse('Sheet1')

# parse strings to datetime type
dataset['Date'] = pd.to_datetime(dataset['Date'], infer_datetime_format= True)
indexedDataset = dataset.set_index(['Date'])

from datetime import datetime
indexedDataset.head()

import sys
from arch import arch_model
model=arch_model(returns, vol='Garch', p=4, o=1, q=3, dist='Normal')
results=model.fit()
print(results.summary())

forecasts = results.forecast(horizon=100, method='simulation', simulations=1000)
sims = forecasts.simulations
lines = plt.plot(sims.values[-1,:,:].T, color='blue', alpha=0.01)
lines[0].set_label('Simulated paths')
plt.show()

print(np.percentile(sims.values[-1,:,-1].T,5))
plt.hist(sims.values[-1, :,-1],bins=50)
plt.title('Distribution of Returns')
plt.show()
