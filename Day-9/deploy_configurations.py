environments=("dev" "staging" "prod")
for env in "${environments[@]}"; do
deploy_configuration "$env"
done