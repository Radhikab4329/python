while true; do
if tail -n 1 /var/log/app.log | grep -q "ERROR"; then
send_alert "Error detected in the log."
fi
sleep 5
done