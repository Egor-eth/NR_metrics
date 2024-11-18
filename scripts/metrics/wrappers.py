from skimage.metrics import peak_signal_noise_ratio as base_psnr
from skimage.metrics import structural_similarity as base_ssim
import flip_evaluator as base_flip 
import cv2
import lpips
import torch

def ssim(img, img_gt):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray_gt = cv2.cvtColor(img_gt, cv2.COLOR_BGR2GRAY)
    (score, diff) =  base_ssim(img_gray, img_gray_gt, full=True)
    return (float(score), diff)


def psnr(img, img_gt):
    return base_psnr(img, img_gt), None

def get_lpips_wrapper(net="alex"):
    # net = "alex" | "vgg"
    metric = lpips.LPIPS(net)
    def lpips_wrapper(img, img_gt):
        img = torch.tensor(img).permute(2, 0, 1).unsqueeze(0)
        img_gt = torch.tensor(img_gt).permute(2, 0, 1).unsqueeze(0)
        print(img.shape)
        value = metric(img, img_gt)
        return float(value), None
    return lpips_wrapper

def flip(img, img_gt):
	return base_flip.evaluate(img, img_gt, "HDR")[1::-1]