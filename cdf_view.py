import cdflib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Load the CDF
cdf = cdflib.CDF(r"C:\Users\KALYAN\Downloads\AL1_ASW91_L2_TH2_20250624_UNP_9999_999999_V02 (1).cdf")  # Replace with your actual file path

# Extract variables
time_cdf = cdf.varget("epoch_for_cdf_mod")
flux = cdf.varget("integrated_flux_mod")

# Convert CDF epoch to human-readable datetime
time = cdflib.cdfepoch.to_datetime(time_cdf)

# Plot
plt.figure(figsize=(12, 5))
plt.plot(time, flux, color='orange')
plt.title("Solar Wind Particle Flux Over Time")
plt.xlabel("Time")
plt.ylabel("Integrated Flux")
plt.grid(True)
plt.tight_layout()
plt.show()
