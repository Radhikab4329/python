databases=("db1" "db2" "db3")
for db in "${databases[@]}"; do
create_backup "$db"
done