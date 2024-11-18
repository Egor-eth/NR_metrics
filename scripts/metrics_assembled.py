import numpy as np
from metrics.wrappers import psnr, ssim, get_lpips_wrapper, flip

METRICS = [("PSNR", psnr), ("SSIM", ssim), ("LPIPS", get_lpips_wrapper()), ("FLIP", flip)]

def metric_names():
    return [x[0] for x in METRICS]

def metrics_for(y : np.ndarray, gt: np.ndarray):
    res = []
    images = []
    for name, metric in METRICS:
        value, image = metric(y, gt)
        res.append((name, str(value)))
        images.append(image)
    print(res)
    return res, images
