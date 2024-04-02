while true; do
replication_lag=$(mysql -e "SHOW SLAVE STATUS\G" | grep "Seconds_Behind_Master" | awk '{print $2}')
if [ "$replication_lag" -gt 60 ]; then
trigger_data_sync
fi
sleep 60
done