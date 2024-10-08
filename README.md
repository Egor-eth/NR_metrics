# NR_metrics

## Usage

Run

    $ source prepare.sh

to load dependencies and enter python venv.

To run metrics use

    $ python scripts/run_metrics.py run-csv [in_dir] [out_csv_file].

This will apply metrics to images in *in_dir* and save them to *out_csv_file*.
All files in *in_dir* must be images and have their "_gt" counterparts.
