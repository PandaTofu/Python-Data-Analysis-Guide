from sklearn.linear_model import LinearRegression

import numpy as np
import numpy as np

x = np.linspace(0, 10, 10).reshape(-1, 1)

noise = np.random.uniform(-2, 2, size=10).reshape(-1, 1)

y = 5 * x + 6 + noise

liner1 = LinearRegression()

liner1.fit(x, y)

liner1.coef_, liner1.intercept_

from sklearn.linear_model import Ridge

liner2 = Ridge(alpha = 0.5)

liner2.fit(x, y)

liner2.coef_, liner2.intercept_

import matplotlib.pylab as plt

plt.scatter(x, y)

y_reg1 = liner1.coef_ * x + liner1.intercept_

plt.plot(x, y_reg1, color='k')

plt.show()

