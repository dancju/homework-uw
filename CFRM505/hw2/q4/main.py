#!/usr/bin/env python3
import numpy as np


def sample_rejection_(gen_y, pdf_x, pdf_y, f_ratio):
    global i_iter
    i_iter += 1
    y = gen_y()
    if np.random.rand() * f_ratio * pdf_y(y) < pdf_x(y):
        return y
    else:
        return sample_rejection_(gen_y, pdf_x, pdf_y, f_ratio)


def sample_rejection(gen_y, pdf_x, pdf_y, f_ratio, i_size):
    return np.array(
        [sample_rejection_(gen_y, pdf_x, pdf_y, f_ratio) for i in range(i_size)]
    )


i_size = 100000
i_iter = 0
ar = sample_rejection(np.random.rand, lambda x: 2 - 2 * x, lambda x: 1, 2, i_size)
print(i_iter / i_size)
