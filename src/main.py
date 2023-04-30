# Display: ssd1306
# Interface: I2C port 1
# Address: 0x3C
# Screen Dimensions: 128 x 64

import time

from demo_opts import get_device
from stats_text import display_stats
from stats_histogram import (
    init_histogram,
    display_histogram,
    histogramData,
    histogramTime,
)


def main():
    wait_time = 15
    while True:
        for _ in range(wait_time):
            display_stats(device)
            time.sleep(1)
        for _ in range(wait_time):
            display_histogram(device, histogramData, histogramTime)
            time.sleep(1)


if __name__ == "__main__":
    try:
        device = get_device()
        histogramData, histogramTime = init_histogram()
        main()
    except KeyboardInterrupt:
        pass
