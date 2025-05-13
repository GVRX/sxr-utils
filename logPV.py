import epics
import time
from datetime import datetime

pv_name = "YOUR:PV:NAME"  # Replace with actual PV name
log_filename = "pv_log.txt"

def read_and_log_pv(pvname, log_file):
    pv = epics.PV(pvname)
    with open(log_file, 'a') as f:
        while True:
            value = pv.get()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}, {value}\n")
            f.flush()
            time.sleep(1)

if __name__ == "__main__":
    try:
        print(f"Logging PV '{pv_name}' every second. Output file: {log_filename}")
        read_and_log_pv(pv_name, log_filename)
    except KeyboardInterrupt:
        print("\nLogging stopped by user.")
