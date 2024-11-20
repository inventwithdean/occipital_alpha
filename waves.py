import mne
import numpy as np
import matplotlib.pyplot as plt

from scipy import signal

raw_eyes_open = mne.io.read_raw_edf("./S001R01.edf", preload=True)
raw_eyes_closed = mne.io.read_raw_edf("./S001R02.edf", preload=True)

data_eyes_open = raw_eyes_open.get_data()
data_eyes_closed = raw_eyes_closed.get_data()
sampling_rate = 160


region_name = "Oz"
region_index = 61
region_data_eyes_open = data_eyes_open[region_index]
region_data_eyes_closed = data_eyes_closed[region_index]

duration = 5


def plot(raw_axes, power_axes, spectrogram_axes, data, name="Oz"):
    samples = duration * sampling_rate
    time = np.arange(samples) / sampling_rate
    # 1. Raw Signal
    raw_axes.plot(time, data[:samples])
    raw_axes.set_title(f"Raw {name} Signal (Eyes Open)")
    raw_axes.set_xlabel("Time (seconds)")
    raw_axes.set_ylabel("Voltage (μV)")

    # 2. Power Spectrum using Welch's Method
    # (more robust than raw FFT for real EEG data)
    freqs, psd = signal.welch(data, sampling_rate, nperseg=sampling_rate * 2)

    power_axes.plot(freqs, psd)
    power_axes.set_title(f"Power Spectrum of {name}")
    power_axes.set_xlabel("Frequency (Hz)")
    power_axes.set_ylabel("Power Spectral Density")
    power_axes.set_xlim(0, 30)

    bands = {"Delta": (0.5, 4), "Theta": (4, 8), "Alpha": (8, 13), "Beta": (13, 30)}
    colors = ["r", "g", "b", "y"]
    for (band, (low, high)), color in zip(bands.items(), colors):
        mask = (freqs >= low) & (freqs <= high)
        power_axes.fill_between(
            freqs[mask], psd[mask], alpha=0.2, color=color, label=band
        )
    power_axes.set_ylim(0)

    power_axes.legend()

    # Spectrogram (time-frequency plot)
    f, t, Sxx = signal.spectrogram(
        data[: samples * 2],
        fs=sampling_rate,
        nperseg=sampling_rate,
        noverlap=sampling_rate // 2,
    )

    c = spectrogram_axes.pcolormesh(t, f, 10 * np.log10(Sxx), shading="gouraud")
    spectrogram_axes.set_title(f"Spectrogram of {name}")
    spectrogram_axes.set_xlabel("Time (s)")
    spectrogram_axes.set_ylabel("Frequency (Hz)")
    plt.colorbar(c, label="Power(dB)")


fig, ax = plt.subplots(3, 2, figsize=(12, 12))
plot(ax[0][0], ax[1][0], ax[2][0], region_data_eyes_open, region_name)
plot(ax[0][1], ax[1][1], ax[2][1], region_data_eyes_closed, region_name)

ax[0][0].set_title(f"Raw {region_name} Signal (Eyes Open)")
ax[0][1].set_title(f"Raw {region_name} Signal (Eyes Closed)")

plt.tight_layout()

plt.show()
fig.savefig("./visualization.png", dpi=150)
