class Server:
    def __init__(self, host, ip_address, status):
        self.host = host
        self.ip_address = ip_address
        self.status = status
dev_server = Server("DEV", "192.168.1.100", "running")
qa_server = Server("QA", "192.168.1.101", "running")
prod_server = Server("PROD", "192.168.1.102", "stopped")

print(f"Server: {dev_server.host}, IP: {dev_server.ip_address}, Status: {dev_server.status}")
print(f"Server: {qa_server.host}, IP: {qa_server.ip_address}, Status: {qa_server.status}")
print(f"Server: {prod_server.host}, IP: {prod_server.ip_address}, Status: {prod_server.status}")