raw_servers = [
    {"id": 1, "name": "Alpha-1", "status": "active", "ping": 12},
    {"id": 2, "name": "Beta-2", "ping": 45},  
    {"id": 3, "status": "active", "ping": 30}, 
    {"id": 4, "name": "Gamma-3", "status": "offline", "ping": 999},
    {"id": 5, "name": "Delta-4", "status": "active"}  
]

def clean_server_data(server_list):
    cleaned_data = []
    for server in server_list:
        if 'name' not in server:
            continue
        current_status = server.get('status', 'offline')
        current_ping = server.get('ping', '0')
        if current_status == 'active':
            cleaned_server = {
                "id": server.get('id'),
                "name": server.get('name'),
                "status": current_status,
                "ping": current_ping
            }
            cleaned_data.append(cleaned_server)

    return cleaned_data
print(clean_server_data(raw_servers))