SELECT id, NETWORK(ip_address) AS first_address, BROADCAST(ip_address) AS last_address
FROM connections
ORDER BY id