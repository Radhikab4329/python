servers=("server1" "server2" "server3")
for server in "${servers[@]}"; do
check_resource_utilization "$server"
done