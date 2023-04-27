import subprocess

# Check if the container already exists
result = subprocess.run(['docker', 'ps', '-a', '--filter', 'name=novelkiApp', '-q'], capture_output=True)
if not result.stdout.strip():
    # If the container doesn't exist, create it
    subprocess.run(['docker', 'create', '--name', 'novelkiApp', '-p', '8080:5000', 'flasknovelki'])
# Start the container
subprocess.run(['docker', 'start', 'novelkiApp']) 