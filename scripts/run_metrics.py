from metrics_assembled import *
import cv2
import os
from pathlib import Path

def y_gt_pair(file: str):
    p = Path(file)
    return (file, str(Path(str(p.with_suffix('')) + "_gt").with_suffix('.png')))


def run_for_each(dir: str, out_file: str):
    metrics = metric_names()
    with open(out_file, "w") as f:
        print('name,' + ','.join(metrics), file=f)
        for y_file, gt_file in [y_gt_pair(x) for x in os.listdir(dir) if "_gt." not in x]:
            print(y_file)
            img = cv2.imread(os.path.join(dir, y_file))
            img_gt = cv2.imread(os.path.join(dir, gt_file))

            res, _ = metrics_for(img, img_gt)
            print(y_file + ',' + ','.join([x[1] for x in res]), file=f)
    print("Done.")


if __name__ == "__main__":
    from sys import argv
    if argv[1] == "run-csv":
        run_for_each(argv[2], argv[3])

