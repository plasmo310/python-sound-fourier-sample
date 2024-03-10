import numpy as np


# 波形関数の生成
class WaveFuncUtil:
    # シヌソイド関数を生成
    @staticmethod
    def make_sinusoid(freq=441, amplitude=8000):
        # 振幅 * sin(周波数 * 2πt)
        def f(t):
            return amplitude * np.sin(2 * np.pi * freq * t)

        return f

    # 短形波の関数を生成
    @staticmethod
    def make_square():
        def f(t):
            if (t % 1) < 0.5:
                return 1
            else:
                return -1

        return f

    # sin2nπの関数を生成
    @staticmethod
    def make_sin_2npi(n):
        def f(t):
            return np.sin(2 * n * np.pi * t)

        return f

    # cos2nπの関数を生成
    @staticmethod
    def make_cos_2npi(n):
        def f(t):
            return np.cos(2 * n * np.pi * t)
        return f
