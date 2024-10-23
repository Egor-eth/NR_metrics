from skimage.metrics import peak_signal_noise_ratio as psnr

def psnr_wrapper(img, img_gt):
    return psnr(img, img_gt), None
