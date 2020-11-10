import numpy as np
import matplotlib.pyplot as plt

import LinearRegression

# Shitty test data
test_X = np.random.rand(100)
test_y = test_X

plt.scatter(test_X, test_y)
plt.savefig("no_trend.png")

r = LinearRegression.SimpleRegressor()
# r.fit(dates_epoch.to_numpy(), opening_prices.to_numpy(), 30)
r.fit(test_X, test_y, 30)
predict_X = np.array([0, 1])
predict_y = r.predict_points(predict_X)
plt.plot(predict_X, predict_y)

plt.savefig("trend.png")

print("m: " + str(r.m))
print("c: " + str(r.c))
