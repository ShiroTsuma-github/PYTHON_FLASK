import subprocess

# Check if the image exists
result = subprocess.run(['docker', 'images', '-q', 'flasknovelki'], capture_output=True)
if not result.stdout.strip():
    # If the image doesn't exist, build it
    subprocess.run(['docker', 'build', '-t', 'flasknovelki', '.'])