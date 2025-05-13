import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


log_filename = "pv_log.txt"

def plot_pv_log(filename):
    # Read the file into a DataFrame
    df = pd.read_csv(filename, names=["timestamp", "value"], sep=", ", engine="python")

    # Convert timestamp column to datetime objects
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Calculate elapsed time in seconds
    start_time = df["timestamp"].iloc[0]
    df["elapsed_seconds"] = (df["timestamp"] - start_time).dt.total_seconds()

    # Plot
    plt.figure()
    plt.plot(df["elapsed_seconds"], df["value"], marker='o', linestyle='-')
    plt.xlabel("Time elapsed (s)")
    plt.ylabel("PV Value")
    plt.title("EPICS PV vs Time")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_pv_log(log_filename)
