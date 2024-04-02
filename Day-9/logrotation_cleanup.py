log_files=("app.log" "access.log" "error.log")
for log_file in "${log_files[@]}"; do
rotate_and_cleanup_logs "$log_file"
done