instances=("instance1" "instance2" "instance3")
for instance in "${instances[@]}"; do
resize_instance "$instance"
done