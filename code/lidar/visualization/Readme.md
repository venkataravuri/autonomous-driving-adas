
# Introduction to AV Datasets


## KITTI Dataset Visualization


### Prerequisites

1. Download KITTI Dataset.
2. Mount KITTI Dataset at `/data/kitti' folder.

### Setup Environment

Install python 3.11,
```
sudo apt install -y python3.10
sudo apt install -y python3.10-venv
sudo update-alternatives --install /usr/bin/python3 python /usr/bin/python3.10 1
sudo update-alternatives --list python
```


Create virtual environment,
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt



export ETS_TOOLKIT='null'
export DISPLAY=:1