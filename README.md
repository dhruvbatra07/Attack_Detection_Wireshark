# Attack Detection Using Wireshark

## Overview

This project focuses on detecting network attacks using Wireshark, a powerful network protocol analyzer. The system is designed to identify SYN Flood, Port Scan, and ARP Spoofing attacks through packet analysis. The implementation leverages Python and the Pyshark library to automate the detection of these attacks in network traffic.

## Features

- *SYN Flood Detection*: Identifies SYN packets without corresponding ACKs to detect SYN Flood attacks.
- *Port Scan Detection*: Detects port scanning attempts by analyzing SYN/ACK packets.
- *ARP Spoofing Detection*: Detects malicious ARP replies indicative of ARP Spoofing.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.6+
- Pyshark library
- Wireshark (optional, for manual analysis)

## Installation

1. *Clone the Repository*
   bash
   git clone https://github.com/dhruvbatra07/Attack_Detection_Wireshark.git
   cd attack-detection-wireshark
   

2. *Install Required Packages*
   bash
   pip install -r requirements.txt
   

   Note: Make sure you have the necessary permissions to capture packets if running on a live network.

## Usage

1. *Running the Detection Script*
   To analyze a pcap file and detect attacks, use the following command:
   bash
   python main.py /path/to/your/pcapfile.pcapng
   

   Replace /path/to/your/pcapfile.pcapng with the actual path to your PCAP file.

2. *Output*
   The script will output detected attacks to the console. Each detected attack will include the type of attack and relevant packet information.

## How It Works

The system uses Pyshark, a Python wrapper for the TShark network protocol analyzer, to read packet captures. The script analyzes the packets and checks for patterns indicative of specific network attacks:

- *SYN Flood Detection*: Checks for TCP packets with the SYN flag set and no corresponding ACK.
- *Port Scan Detection*: Looks for a series of SYN packets to different ports.
- *ARP Spoofing Detection*: Monitors ARP packets for suspicious activity, such as unsolicited ARP replies.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: git checkout -b feature-branch-name.
3. Make your changes and commit them: git commit -m 'Add new feature'.
4. Push to the branch: git push origin feature-branch-name.
5. Submit a pull request.
