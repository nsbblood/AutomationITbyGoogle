import csv

hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

# Open the file
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write a row
    writer.writerow(['Name', 'Age', 'City'])
    
    # Write multiple rows
    writer.writerows([['Alice', 30, 'New York'], ['Bob', 25, 'Los Angeles']])
