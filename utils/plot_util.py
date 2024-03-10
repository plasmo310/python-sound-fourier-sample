import matplotlib.pyplot as plt
import numpy as np


# plot処理
class PlotUtil:
    # plot: 関数
    @staticmethod
    def plot_function(f, xmin, xmax, **kwargs):
        times = np.linspace(xmin, xmax, 1000)
        plt.plot(times, [f(t) for t in times], **kwargs)

    # plot: 点郡
    @staticmethod
    def plot_sequence(points, count=100, line=False, **kwargs):
        if line:
            plt.plot(range(0, count), points[0:count], **kwargs)
        else:
            plt.scatter(range(0, count), points[0:count], **kwargs)
