import lpips
import torch

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
