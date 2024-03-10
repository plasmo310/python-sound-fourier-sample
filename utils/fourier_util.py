import numpy as np
from .wave_func_util import *


# フーリエ処理関連
class FourierUtil:
    # フーリエ級数による関数を生成
    # a0: 定数関数
    # a_array: sin関数の定数項
    # b_array: cos関数の定数項
    @staticmethod
    def make_fourier_series_function(a0, a_array, b_array, freq=441):
        def result(t):
            cos_terms = []
            for (n, an) in enumerate(a_array):
                cos_terms.append(an * np.cos(2 * np.pi * (n + 1) * freq * t))
            sin_terms = []
            for (n, bn) in enumerate(b_array):
                sin_terms.append(bn * np.sin(2 * np.pi * (n + 1) * freq * t))
            return a0 * FourierUtil.const() + sum(cos_terms) + sum(sin_terms)
        return result

    # フーリエ解析
    # N回分sin、cos波の積分を行い周波数成分を抽出する
    # a0: f(x)、1/√2の内積
    # an: f(x)、cos2nπの内積
    # bn: f(x)、sos2nπの内積
    @staticmethod
    def fourier_coefficients(f, N):
        a0 = FourierUtil.dot_function(f, FourierUtil.const)
        an_array = []
        for n in range(1, N + 1):
            an_array.append(FourierUtil.dot_function(f, WaveFuncUtil.make_cos_2npi(n)))
        bn_array = []
        for n in range(1, N + 1):
            bn_array.append(FourierUtil.dot_function(f, WaveFuncUtil.make_sin_2npi(n)))
        return a0, an_array, bn_array

    # フーリエ解析の定数
    # dot(const, const)の結果が1となるような値を返却する
    @staticmethod
    def const(n=0):
        return 1 / np.sqrt(2)

    # 関数同士の内積
    # 2 * ∮[0→1]f(t)g(t)
    @staticmethod
    def dot_function(f, g, N=100):
        dt = 1 / N
        array = []
        for t in np.arange(0, 1, dt):
            array.append(f(t) * g(t) * dt)
        return 2 * sum(array)
