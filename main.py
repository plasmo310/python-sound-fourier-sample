import pygame
import time
from utils.fourier_util import *
from utils.plot_util import *
from utils.wave_func_util import *
from utils.wave_points_util import *


# サンプリングレート
SAMPLE_RATE = 44100


# sin波の再生チェック
def check_sin_wave():
    # initialize
    pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=1)

    # make sin wave points
    func = WaveFuncUtil.make_sinusoid()
    points = WavePointsUtil.make_from_function(func, 0, 1)

    # plot
    plot_count = 300
    PlotUtil.plot_sequence(points, plot_count, True)
    plt.show()

    # play sound
    points = points.astype(np.int16)
    sound = pygame.sndarray.make_sound(points)
    sound.play()
    time.sleep(1)


# 短形波の関数のフーリエ級数チェック
def check_rect_fourier_series():
    # 短形波の関数生成: bの数を多くするほど近づく
    b_count = 10
    b_array = []
    for n in range(1, b_count):
        b = 4 / (n*np.pi) if n % 2 != 0 else 0
        b_array.append(b)
    f1 = FourierUtil.make_fourier_series_function(0, [], b_array)
    points = WavePointsUtil.make_from_function(f1, 0, 1)

    # plot
    plot_count = 300
    PlotUtil.plot_sequence(points, plot_count, True)
    plt.show()


# 関数同士の内積結果チェック
def check_dot_function():
    # どれも1に近い数字が出力される
    print(FourierUtil.dot_function(WaveFuncUtil.make_cos_2npi(1), WaveFuncUtil.make_cos_2npi(1)))
    print(FourierUtil.dot_function(WaveFuncUtil.make_sin_2npi(1), WaveFuncUtil.make_sin_2npi(1)))
    print(FourierUtil.dot_function(WaveFuncUtil.make_cos_2npi(3), WaveFuncUtil.make_cos_2npi(3)))


# フーリエ解析のチェック
def check_fourier_coefficients():
    # 解析する関数
    f1 = FourierUtil.make_fourier_series_function(0, [2, 3, 4], [5, 6, 7], 1)

    # フーリエ解析を行う
    (a0, a_array, b_array) = FourierUtil.fourier_coefficients(f1, 3, 1)
    f2 = FourierUtil.make_fourier_series_function(0, a_array, b_array, 1)
    print((a0, a_array, b_array))

    # 変換前後の差分を比較
    points_f1 = WavePointsUtil.make_from_function(f1, 0, 1)
    points_f2 = WavePointsUtil.make_from_function(f2, 0, 1)
    plot_count = 44100
    PlotUtil.plot_sequence(points_f1, plot_count, True)
    PlotUtil.plot_sequence(points_f2, plot_count, True)
    plt.show()


if __name__ == '__main__':
    check_fourier_coefficients()
