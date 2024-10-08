import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr

METRICS = [("PSNR", psnr)]

def metric_names():
    return [x[0] for x in METRICS]

def metrics_for(y : np.ndarray, gt: np.ndarray):
    res = []
    for name, f in METRICS:
        res.append((name, str(f(y, gt))))
    return res
