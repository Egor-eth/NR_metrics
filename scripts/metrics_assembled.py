import numpy as np
from metrics.psnr import psnr_wrapper as psnr
from metrics.ssim import ssim_wrapper as ssim
from metrics.lpips import get_lpips_wrapper as get_lpips

METRICS = [("PSNR", psnr), ("SSIM", ssim), ("LPIPS", get_lpips())]

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
