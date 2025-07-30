import paramiko
import os

# === CONFIGURATION ===
HOST = "localhost"
PORT = 2222
USERNAME = "luke"
PASSWORD = "admin"
LOCAL_DIR = "./source"  # Must be in the same folder as this script
REMOTE_DIR = "upload"          # Upload to user's home directory in SFTP jail

print("Starting SFTP upload process...")

try:
    # Create and connect transport
    transport = paramiko.Transport((HOST, PORT))
    transport.connect(username=USERNAME, password=PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)

    print(f"Connected to SFTP server at {HOST}:{PORT} as {USERNAME}")

    # list remote files (for debug purpose)
    print("Remote directory listing:")
    for item in sftp.listdir(REMOTE_DIR):
        print(f" - {item}")

    # loop through and upload each .txt file
    uploaded_count = 0
    for filename in os.listdir(LOCAL_DIR):
        if filename.casefold().endswith(".txt"):
            local_path = os.path.join(LOCAL_DIR, filename)
            remote_path = os.path.join(REMOTE_DIR, filename).replace("\\", "/")  # for Windows compatibility


            if not os.path.exists(local_path):
                print(f"Skipping missing file: {local_path}")
                continue

            print(f"Uploading: {local_path} → {remote_path}")
            sftp.put(local_path, remote_path)
            uploaded_count += 1

    print(f"Upload complete. {uploaded_count} file(s) uploaded.")

except Exception as e:
    print(f"SFTP error: {e}")

finally:
    try:
        sftp.close()
        transport.close()
        print("SFTP connection closed.")
    except Exception as close_err:
        print(f"Error closing connection: {close_err}")
