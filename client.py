import socket

def start_echo_client(host='127.0.0.1', port=3000, message="Hello, Server!"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        
        client_socket.sendall(message.encode())
        print(f"Sent: {message}")
        
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    print("Test1")
    start_echo_client(message="Hello, Echo Server!")
    print("Test2")
    start_echo_client(message="Hello, Echo Server again!")
    print("Test3")
    start_echo_client(message="Hello, Echo Server again and again!")
