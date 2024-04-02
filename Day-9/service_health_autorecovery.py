while true; do
if ! check_service_health; then
restart_service
fi
sleep 30
done