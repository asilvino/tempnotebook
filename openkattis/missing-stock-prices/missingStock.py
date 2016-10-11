import math
import sys
import StringIO
import numpy as np
from scipy import interpolate
sys.stdin = StringIO.StringIO("250\n1/3/2012 16:00:00	26.96\n1/4/2012 16:00:00	27.47\n1/5/2012 16:00:00	27.728\n1/6/2012 16:00:00	28.19\n1/9/2012 16:00:00	28.1\n1/10/2012 16:00:00	28.15\n1/11/2012 16:00:00	27.98\n1/12/2012 16:00:00	28.02\n1/13/2012 16:00:00	28.25\n1/17/2012 16:00:00	28.65\n1/18/2012 16:00:00	28.4\n1/19/2012 16:00:00	28.435\n1/20/2012 16:00:00	29.74\n1/23/2012 16:00:00	29.95\n1/24/2012 16:00:00	29.5703\n1/25/2012 16:00:00	29.65\n1/26/2012 16:00:00	29.7\n1/27/2012 16:00:00	29.53\n1/30/2012 16:00:00	29.62\n1/31/2012 16:00:00	29.7\n2/1/2012 16:00:00	30.05\n2/2/2012 16:00:00	30.17\n2/3/2012 16:00:00	30.4\n2/6/2012 16:00:00	30.22\n2/7/2012 16:00:00	30.485\n2/8/2012 16:00:00	30.67\n2/9/2012 16:00:00	30.8\n2/10/2012 16:00:00	30.8\n2/13/2012 16:00:00	30.77\n2/14/2012 16:00:00	30.46\n2/15/2012 16:00:00	30.39\n2/16/2012 16:00:00	31.55\n2/17/2012 16:00:00	31.32\n2/21/2012 16:00:00	31.61\n2/22/2012 16:00:00	31.68\n2/23/2012 16:00:00	31.59\n2/24/2012 16:00:00	31.5\n2/27/2012 16:00:00	31.5\n2/28/2012 16:00:00	31.93\n2/29/2012 16:00:00	32\n3/1/2012 16:00:00	32.39\n3/2/2012 16:00:00	32.44\n3/5/2012 16:00:00	32.05\n3/6/2012 16:00:00	31.98\n3/7/2012 16:00:00	31.92\n3/8/2012 16:00:00	32.21\n3/9/2012 16:00:00	32.16\n3/12/2012 16:00:00	32.2\n3/13/2012 16:00:00	Missing_1\n3/14/2012 16:00:00	32.88\n3/15/2012 16:00:00	32.94\n3/16/2012 16:00:00	32.95\n3/19/2012 16:00:00	32.61\n3/20/2012 16:00:00	32.15\n3/21/2012 16:00:00	Missing_2\n3/22/2012 16:00:00	32.09\n3/23/2012 16:00:00	32.11\n3/26/2012 16:00:00	Missing_3\n3/27/2012 16:00:00	32.7\n3/28/2012 16:00:00	32.7\n3/29/2012 16:00:00	32.19\n3/30/2012 16:00:00	32.41\n4/2/2012 16:00:00	32.46\n4/3/2012 16:00:00	32.19\n4/4/2012 16:00:00	31.69\n4/5/2012 16:00:00	31.63\n4/9/2012 16:00:00	31.4\n4/10/2012 16:00:00	31.19\n4/11/2012 16:00:00	30.53\n4/12/2012 16:00:00	31.04\n4/13/2012 16:00:00	31.16\n4/16/2012 16:00:00	31.19\n4/17/2012 16:00:00	31.61\n4/18/2012 16:00:00	31.31\n4/19/2012 16:00:00	31.68\n4/20/2012 16:00:00	32.89\n4/23/2012 16:00:00	32.5\n4/24/2012 16:00:00	32.52\n4/25/2012 16:00:00	32.32\n4/26/2012 16:00:00	32.23\n4/27/2012 16:00:00	32.22\n4/30/2012 16:00:00	32.11\n5/1/2012 16:00:00	32.335\n5/2/2012 16:00:00	31.925\n5/3/2012 16:00:00	31.9\n5/4/2012 16:00:00	31.57\n5/7/2012 16:00:00	30.86\n5/8/2012 16:00:00	30.78\n5/9/2012 16:00:00	30.83\n5/10/2012 16:00:00	31.02\n5/11/2012 16:00:00	31.54\n5/14/2012 16:00:00	31.04\n5/15/2012 16:00:00	30.795\n5/16/2012 16:00:00	30.32\n5/17/2012 16:00:00	30.2084\n5/18/2012 16:00:00	29.81\n5/21/2012 16:00:00	29.79\n5/22/2012 16:00:00	29.88\n5/23/2012 16:00:00	29.4\n5/24/2012 16:00:00	Missing_4\n5/25/2012 16:00:00	29.36\n5/29/2012 16:00:00	29.72\n5/30/2012 16:00:00	29.479\n5/31/2012 16:00:00	29.42\n6/1/2012 16:00:00	Missing_5\n6/4/2012 16:00:00	Missing_6\n6/5/2012 16:00:00	28.75\n6/6/2012 16:00:00	29.37\n6/7/2012 16:00:00	29.7\n6/8/2012 16:00:00	29.68\n6/11/2012 16:00:00	29.81\n6/12/2012 16:00:00	29.3\n6/13/2012 16:00:00	29.44\n6/14/2012 16:00:00	29.46\n6/15/2012 16:00:00	30.08\n6/18/2012 16:00:00	30.03\n6/19/2012 16:00:00	31.11\n6/20/2012 16:00:00	31.05\n6/21/2012 16:00:00	31.14\n6/22/2012 16:00:00	30.73\n6/25/2012 16:00:00	30.32\n6/26/2012 16:00:00	30.27\n6/27/2012 16:00:00	30.5\n6/28/2012 16:00:00	30.05\n6/29/2012 16:00:00	30.69\n7/2/2012 16:00:00	30.62\n7/3/2012 16:00:00	30.76\n7/5/2012 16:00:00	30.78\n7/6/2012 16:00:00	30.7\n7/9/2012 16:00:00	30.23\n7/10/2012 16:00:00	30.22\n7/11/2012 16:00:00	29.735\n7/12/2012 16:00:00	29.18\n7/13/2012 16:00:00	29.48\n7/16/2012 16:00:00	29.53\n7/17/2012 16:00:00	29.86\n7/18/2012 16:00:00	30.45\n7/19/2012 16:00:00	30.8\n7/20/2012 16:00:00	Missing_7\n7/23/2012 16:00:00	Missing_8\n7/24/2012 16:00:00	29.36\n7/25/2012 16:00:00	29.33\n7/26/2012 16:00:00	Missing_9\n7/27/2012 16:00:00	29.85\n7/30/2012 16:00:00	29.82\n7/31/2012 16:00:00	29.71\n8/1/2012 16:00:00	29.65\n8/2/2012 16:00:00	29.525\n8/3/2012 16:00:00	29.94\n8/6/2012 16:00:00	30.11\n8/7/2012 16:00:00	30.35\n8/8/2012 16:00:00	30.47\n8/9/2012 16:00:00	30.65\n8/10/2012 16:00:00	30.62\n8/13/2012 16:00:00	30.46\n8/14/2012 16:00:00	30.39\n8/15/2012 16:00:00	30.28\n8/16/2012 16:00:00	30.94\n8/17/2012 16:00:00	30.92\n8/20/2012 16:00:00	30.85\n8/21/2012 16:00:00	30.96\n8/22/2012 16:00:00	30.76\n8/23/2012 16:00:00	30.4\n8/24/2012 16:00:00	30.63\n8/27/2012 16:00:00	30.96\n8/28/2012 16:00:00	30.8\n8/29/2012 16:00:00	30.75\n8/30/2012 16:00:00	30.61\n8/31/2012 16:00:00	30.96\n9/4/2012 16:00:00	30.66\n9/5/2012 16:00:00	30.53\n9/6/2012 16:00:00	31.36\n9/7/2012 16:00:00	31.07\n9/10/2012 16:00:00	Missing_10\n9/11/2012 16:00:00	30.91\n9/12/2012 16:00:00	31.18\n9/13/2012 16:00:00	31.18\n9/14/2012 16:00:00	31.25\n9/17/2012 16:00:00	Missing_11\n9/18/2012 16:00:00	31.21\n9/19/2012 16:00:00	31.19\n9/20/2012 16:00:00	Missing_12\n9/21/2012 16:00:00	31.61\n9/24/2012 16:00:00	31.07\n9/25/2012 16:00:00	31\n9/26/2012 16:00:00	30.6\n9/27/2012 16:00:00	30.4\n9/28/2012 16:00:00	30.26\n10/1/2012 16:00:00	29.98\n10/2/2012 16:00:00	29.89\n10/3/2012 16:00:00	29.99\n10/4/2012 16:00:00	30.03\n10/5/2012 16:00:00	30.25\n10/8/2012 16:00:00	29.92\n10/9/2012 16:00:00	Missing_13\n10/10/2012 16:00:00	Missing_14\n10/11/2012 16:00:00	29.25\n10/12/2012 16:00:00	29.32\n10/15/2012 16:00:00	Missing_15\n10/16/2012 16:00:00	29.74\n10/17/2012 16:00:00	29.64\n10/18/2012 16:00:00	29.73\n10/19/2012 16:00:00	29.08\n10/22/2012 16:00:00	28.83\n10/23/2012 16:00:00	28.2\n10/24/2012 16:00:00	28.2\n10/25/2012 16:00:00	28.2\n10/26/2012 16:00:00	28.34\n10/31/2012 16:00:00	Missing_16\n11/1/2012 16:00:00	29.56\n11/2/2012 16:00:00	29.77\n11/5/2012 16:00:00	29.74\n11/6/2012 16:00:00	Missing_17\n11/7/2012 16:00:00	29.825\n11/8/2012 16:00:00	29.37\n11/9/2012 16:00:00	29.19\n11/12/2012 16:00:00	29.01\n11/13/2012 16:00:00	Missing_18\n11/14/2012 16:00:00	27.29\n11/15/2012 16:00:00	26.97\n11/16/2012 16:00:00	Missing_19\n11/19/2012 16:00:00	26.8\n11/20/2012 16:00:00	26.8\n11/21/2012 16:00:00	27.1666\n11/23/2012 13:00:00	27.77\n11/26/2012 16:00:00	27.58\n11/27/2012 16:00:00	27.38\n11/28/2012 16:00:00	27.39\n11/29/2012 16:00:00	27.36\n11/30/2012 16:00:00	27.13\n12/3/2012 16:00:00	26.82\n12/4/2012 16:00:00	26.63\n12/5/2012 16:00:00	26.93\n12/6/2012 16:00:00	26.98\n12/7/2012 16:00:00	26.82\n12/10/2012 16:00:00	26.97\n12/11/2012 16:00:00	27.49\n12/12/2012 16:00:00	27.62\n12/13/2012 16:00:00	Missing_20\n12/14/2012 16:00:00	27.13\n12/17/2012 16:00:00	27.215\n12/18/2012 16:00:00	27.63\n12/19/2012 16:00:00	27.73\n12/20/2012 16:00:00	27.68\n12/21/2012 16:00:00	27.49\n12/24/2012 13:00:00	27.25\n12/26/2012 16:00:00	27.2\n12/27/2012 16:00:00	27.09\n12/28/2012 16:00:00	26.9\n12/31/2012 16:00:00	26.77\n")

n = int(raw_input())
stocks = []
for i in range(n):
	value = raw_input().split('\t')
	stocks.append(value[1])
stocksPrices = []
stocksPricesMissing = []
x = []
for i in range(len(stocks)):
	stock = stocks[i]
	x.append(i)
	if 'Miss' in stock:
		stocksPricesMissing.append(i)
		stocksPrices.append(np.nan)
	else:
		stocksPrices.append(float(stock))

y = np.array(stocksPrices)
w = np.isnan(y)
y[w] = 0.
f = interpolate.UnivariateSpline(x, y,w=~w,s=1)
for i in stocksPricesMissing:
   print f(i)

# xs = np.linspace(-3, 3, 1000)
# print xs