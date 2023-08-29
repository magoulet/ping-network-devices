# Ping Network Devices

Ping Netowrk Devices is a Python program that pings a device at predefined intervals and logs the results to a file. The target device IP and port information are stored in a configuration YAML file, and the log file is created using the logging library.

## Features

- Pings a device at a specified interval
- Logs the ping results to a log file
- Supports configuration via a YAML file
- Uses the `ping3` library for pinging the device
- Utilizes the `logging` library for creating log files

## Prerequisites

- Python 3.x
- `ping3` library: `pip install ping3`
- `pyyaml` library: `pip install pyyaml`

## Installation

1. Clone or download the repository to your local machine.

2. Install the required libraries by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Open the `config.yaml` file.

2. Update the `device` section with the IP address and port of your network device.

   ```yaml
   device:
     ip: <printer_ip>
     port: <printer_port>
   ```

3. Save and close the `config.yaml` file.

## Usage

1. Run the program using the following command:
   ```
   python main.py
   ```

2. The program will continuously ping the device at the specified interval (default: 5 minutes) and write the results to the log file (`ping.log`).

## Customization

- You can modify the ping interval by changing the `time.sleep()` function call in the `main.py` script.
- To change the log file name or logging level, modify the `basicConfig()` function call in the `main.py` script.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize this README file according to your specific needs.