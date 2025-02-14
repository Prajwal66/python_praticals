def update_server_config(file_path,key,value):

    with open(file_path,'r') as file:
        lines = file.readlines()

    with open(file_path,'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)


server_config_files = 'server.conf'
# Key and new value for updating the server configuration
key = 'MAX_CONNECTIONS'
value = '1000'  # New maximum connections allowed

update_server_config(server_config_files,key,value)