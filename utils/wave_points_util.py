import numpy as np


# 波形値配列の生成
class WavePointsUtil:

    # 波形: ノイズ
    @staticmethod
    def make_noise(size=44100):
        return np.random.randint(-10000, 10000, size=size)

    # 波形: 短形波
    # freq: 周波数 (441:A、350:F)
    @staticmethod
    def make_rect(size=44100, freq=441):
        interval = size / freq
        form = np.repeat([10000, -10000], interval / 2)
        return np.tile(form, freq)

    # 関数の指定範囲から値を生成
    @staticmethod
    def make_from_function(f, start, end, size=44100):
        mapf = np.vectorize(f)
        times = np.arange(start, end, (end - start) / size)
        values = mapf(times)
        return values.astype(np.int16)
