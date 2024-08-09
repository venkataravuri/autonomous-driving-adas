import logging.config
import yaml

from visualization.mayavi_viz.visualizer import dataset_viz

# Load the config file
with open('logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

# Configure the logging module with the config file
logging.config.dictConfig(config)


if __name__ == '__main__':
    dataset_viz()