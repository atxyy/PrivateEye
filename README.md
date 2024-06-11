# Private Eye Walkthrough

## Setup

1. **Install Required Libraries**
2. **Run Server on PC**
3. **Choose Listening or Sending Options on Server**
4. **Plug in ESP and Begin Interactions**

## Features

### Send

The send option allows you to send messages and data from the ESP to the PC server.

- **GPT Requests:** If the letters "gpt" are typed before a message, the server knows that the ESP wants to send a query to GPT-4.
  - **Example Usage:** `gpt how many moons orbit earth`

### Listen 

The listen feature allows data to be received from the server to the ESP. Send mode must be running on the server to send the messages.

### Netscan

Netscan or "scan" is an ARP scan that runs on the ESP, pinging all potential devices on the ESP's subnet. If a response is received, a device is found and logged.
