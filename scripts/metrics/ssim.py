from skimage.metrics import structural_similarity as ssim
import cv2

def ssim_wrapper(img, img_gt):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray_gt = cv2.cvtColor(img_gt, cv2.COLOR_BGR2GRAY)
    (score, diff) =  ssim(img_gray, img_gray_gt, full=True)
    return (float(score), diff)
