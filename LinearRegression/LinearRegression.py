class SimpleRegressor():
    def __init__(self, m=0, c=0, L=0.0001):
        self.fitted = False
        self.m = m
        self.c = c
        self.L = L

        self._d_m = 0
        self._d_c = 0

    def fit(self, X, y, epochs=1000):
        self.X = X
        self.y = y
        self.epochs = epochs

        if self.fitted:
            raise Exception("This regressor is already fitted")

        if self.X.size != self.y.size:
            raise Exception("X and y are of differing sizes")
        else:
            self.n = self.X.size

        for i in range(epochs):
            y_pred = self.m*self.X + self.c

            self._d_m = (-2/self.n) * sum(self.X * (self.y - y_pred))
            self._d_c = (-2/self.n) * sum(self.y - y_pred)

            self.m = self.m - (self.L * self._d_m)
            self.c = self.c - (self.L * self._d_c)

            #  print("================")
            #  print(self.m)
            #  print(self._d_m)
            #  print(self.c)
            #  print(self._d_c)
            #  print("================")

        self.fitted = True

    def predict_point(self, x_i):
        return self.m*x_i + self.c

    def predict_points(self, X):
        return self.m*X + self.c
