server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

def get_server_status(server_name):
    return server_config.get(server_name,{}).get("status","not found")


server = input("Enter server name: \n")

#server_name = 'server1'

get_details = get_server_status(server)
print(f"{server} Status: {get_details}")


#thanks a lot to abhishek veeramala for this 