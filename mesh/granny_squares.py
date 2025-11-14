# Granny Squares: Basic mesh node idea
import socket  # For talking to neighbors

def join_mesh(my_ip):
    print(f"Node at {my_ip} joining mesh...")
    # Fake relay boost
    boost = "Signal stronger by 20%!"
    return boost

# Test
my_ip = "192.168.1.100"  # Your fake IP
print(join_mesh(my_ip))
