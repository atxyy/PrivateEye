import network
import socket
import errno

def do_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Network config:', wlan.ifconfig())

def manualwifi():
    ssid = 'NETWORKSSID'
    password = 'NETWORKPASSWORD'
    do_connect(ssid, password)

def send_to_server(server_ip, server_port, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((server_ip, server_port))
        s.send(message.encode())
    finally:
        s.close()

def scan_network(ip_base, start, end, port):
    for i in range(start, end + 1):
        ip = '{}.{}'.format(ip_base, i)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((ip, port))
            print('Device found at:', ip)
        except OSError as e:
            if e.args[0] not in (errno.ECONNREFUSED, errno.ETIMEDOUT):
                print('Error connecting to:', ip, 'with error:', e)
        finally:
            s.close()

def esp_server_mode(esp_port):
    esp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    esp_socket.bind(('', esp_port))  # Bind to all interfaces
    esp_socket.listen(1)
    print(f"ESP listening on port {esp_port}")

    while True:
        conn, addr = esp_socket.accept()
        print(f"Connection from {addr}")
        data = conn.recv(1024)
        if data:
            print("Received:", data.decode())
        conn.close()
        
def esp_server_mode_once(esp_port):
    esp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    esp_socket.bind(('', esp_port))  # Bind to all interfaces
    esp_socket.listen(1)
    print(f"ESP listening on port {esp_port}")

    conn, addr = esp_socket.accept()
    print(f"Connection from {addr}")
    data = conn.recv(1024)
    if data:
        print("Received:", data.decode())
    conn.close()
    esp_socket.close()  # Close the socket after receiving the response

    # Go back to the main function
    print("")
    main()


def main():
    server_ip = '10.0.222.225'  # Replace with your server's IP
    server_port = 9999
    esp_port = 9999  # The port the ESP will listen on

    manualwifi()  # Connect to Wi-Fi

    while True:
        print("""
send
listen
netscan""")
        choice = input(">>>")
        if choice == 'send':
            message = input("Enter message to send: ")
            send_to_server(server_ip, server_port, message)
            esp_server_mode_once(esp_port)
        elif choice == 'listen':
            esp_server_mode(esp_port)
        elif choice == 'scan':
            a = input("Type first 3 IP segments: ")
            scan_network(a, 1, 255, 80)   
        else:
            print("Invalid choice. Type 'send', 'listen', or 'scan'.")

main()
