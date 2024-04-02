while ! aws ec2 describe-instance-status --instance-ids i-1234567890abcdef0 | grep -q "running"; do
echo "Waiting for the EC2 instance to be running..."
sleep 10
done