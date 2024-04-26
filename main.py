import logging
import logging.handlers
from ping3 import ping
import time
import yaml

def main():
    # Load configuration from YAML file
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Set up logging
    logging.basicConfig(filename='ping.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()

    # Get printer IP and port from config
    ip = config['resource']['ip']
#    port = config['resource']['port']

    # Ping the device and log the results
    while True:
        try:
            result = ping(ip, timeout=3)
            if result is not None:
                logger.info(f'Ping successful. Response time: {result:.4f} ms')
            else:
                logger.warning('** No Ping response **')
        except Exception as e:
            logger.error(f'Error pinging the resource: {e}')

        # Wait before the next ping
        time.sleep(5)

if __name__ == '__main__':
    main()
