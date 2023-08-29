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
    printer_ip = config['device']['ip']
    printer_port = config['device']['port']

    # Ping the printer and log the results
    while True:
        try:
            result = ping(printer_ip, timeout=3)
            if result is not None:
                logger.info(f'Device is online. Response time: {result:.4f} ms')
            else:
                logger.warning('Device is offline')
        except Exception as e:
            logger.error(f'Error pinging the device: {e}')

        # Wait before the next ping
        time.sleep(5*60)

if __name__ == '__main__':
    main()