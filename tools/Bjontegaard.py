import numpy as np
import scipy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class Bjontegaard_Model:
    def __init__(self, bitrates, psnr_values):
        self.bitrates = bitrates
        self.psnr_values = psnr_values

        self.parameters = [0, 0, 0, 0]
        self.__update_model()

    def __update_model(self):
        def bj_model(R, a, b, c, d):
            value =  a * np.power(np.log(R), 3)
            value += b * np.power(np.log(R), 2)
            value += c * np.log(R)
            value += d 
            return value

        self.parameters, _ = curve_fit(
                bj_model,
                self.bitrates,
                self.psnr_values,
                p0=self.parameters)

    def evaluate(self, R):
        value =  self.parameters[0] * np.power(np.log(R), 3)
        value += self.parameters[1] * np.power(np.log(R), 2)
        value += self.parameters[2] * np.log(R)
        value += self.parameters[3] 
        return value

    def plot(self, ax):
        def bj_model(R, a, b, c, d):
            value =  a * np.power(np.log(R), 3)
            value += b * np.power(np.log(R), 2)
            value += c * np.log(R)
            value += d 
            return value
        xdata = np.linspace(np.min(self.bitrates), np.max(self.bitrates), 100)
        ax.scatter(self.bitrates, self.psnr_values)
        ax.plot(xdata, bj_model(xdata,*self.parameters))


if __name__ == "__main__":
    # Results of Zhu et al. ," View-Dependent Dynamic Point Cloud Compression"
    # on soldier, D1
    bitrates = [24.35, 13.93, 9.27, 6.53]
    d1 = [71.17, 69.54, 67.62, 65.77]
    metric = Bjontegaard_Model(bitrates, d1)
    print(metric.evaluate(24.35))
    print(metric.evaluate(19))
    print(metric.evaluate(18))
    print(metric.evaluate(13.93))
    fig, ax = plt.subplots()
    metric.plot(ax)
    plt.show()
