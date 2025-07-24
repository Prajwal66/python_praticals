import os 

#command to create env var 
# export dbport="3306"
DB_PORT = os.getenv("dbport")

print(DB_PORT)
