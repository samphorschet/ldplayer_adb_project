import subprocess

class ADBLogic:
    def __init__(self):
        self.adb_path = "adb"  # Change if adb is not in PATH

    def get_ldplayer_devices(self):
        try:
            result = subprocess.check_output([self.adb_path, "devices"], encoding="utf-8")
            lines = result.strip().split('\n')[1:]  # Skip header
            devices = []
            for line in lines:
                if line.strip():
                    parts = line.split()
                    if "emulator" in parts[0] or "127.0.0.1" in parts[0]:
                        devices.append(parts[0])
            return devices
        except Exception as e:
            print("Error getting devices:", e)
            return []

    def start_facebook(self, device_id):
        try:
            subprocess.run([
                self.adb_path, "-s", device_id,
                "shell", "am", "start", "-n", "com.facebook.katana/.LoginActivity",
                "--activity-clear-task"
            ])
        except Exception as e:
            print(f"Error starting Facebook on {device_id}: {e}")
