# BrainWave Explorer 🧠 ⚡

Exploring the fascinating world of EEG (Electroencephalography) data visualization! This project demonstrates how our brain's electrical activity changes when we simply close our eyes. 

## The Magic of Alpha Waves ✨

When you close your eyes, something amazing happens in your brain - particularly in the occipital region (the visual processing area). Neurons start synchronizing at around 10Hz, creating what we call "alpha waves". This project visualizes this phenomenon using EEG data!

## What's Inside 🎯

- `visualize_brain.py`: Main Python script for EEG visualization
- `S001R01.edf`: EEG recording with eyes open
- `S001R02.edf`: EEG recording with eyes closed
- Sample output showing the dramatic difference!

## The Results 📊

![Brain Wave Analysis](https://github.com/user-attachments/assets/9b0300e8-8029-4d1f-a262-6d8906bc7d7d)

What we're seeing here:
1. **Raw Signal**: 
   - Left: Eyes Open (more random)
   - Right: Eyes Closed (more rhythmic)

2. **Power Spectrum**: 
   - Left: No dominant frequency
   - Right: HUGE peak at 10Hz (alpha waves! 🎯)

3. **Spectrogram**:
   - Left: Scattered activity
   - Right: Strong band around 10Hz (yellow/green)

## Requirements 🛠️

```python
import mne
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
```

## Quick Start 🚀

1. Clone the repository:
```bash
git clone https://github.com/inventwithdean/occipital_alpha.git
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the visualization:
```bash
python waves.py
```

## Data Source 📚

The EEG data comes from the [EEG Motor Movement/Imagery Dataset](https://physionet.org/content/eegmmidb/1.0.0/) available on PhysioNet. This project uses:
- Subject: S001
- Recordings: 
  * R01 (eyes open)
  * R02 (eyes closed)

## Understanding the Code 🤓

The code uses:
- Fast Fourier Transform (FFT) to break down the signal into frequencies
- Welch's method for power spectrum estimation
- Spectrogram for time-frequency analysis

### Key Brain Wave Bands 🌊
| Band | Frequency | State |
|------|-----------|-------|
| Delta | 0.5-4 Hz | Deep Sleep 😴 |
| Theta | 4-8 Hz   | Drowsiness 🌙 |
| Alpha | 8-13 Hz  | Relaxed, Eyes Closed 👁️ |
| Beta  | 13-30 Hz | Alert, Focused 🏃 |

## Want to Contribute? 🤝

Feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License 📜

MIT License - feel free to use this for your own EEG adventures!

## Next Steps 🎯

Planning to:
- [ ] Add more brain regions
- [ ] Implement real-time visualization
- [ ] Add machine learning analysis
- [ ] Create interactive plots

## Acknowledgments 🙏

Special thanks to:
- [PhysioNet](https://physionet.org/) for the amazing dataset
- [MNE Python](https://mne.tools/stable/index.html) team for the excellent EEG tools
- The fascinating human brain for being so... fascinating!

## Citations 📚

This work utilizes the EEG Motor Movement/Imagery Dataset. If you use this code or data, please cite the following papers:

### Original Dataset Publication
```bibtex
@article{schalk2004bci,
 title={BCI2000: A General-Purpose Brain-Computer Interface (BCI) System},
 author={Schalk, G. and McFarland, D.J. and Hinterberger, T. and Birbaumer, N. and Wolpaw, J.R.},
 journal={IEEE Transactions on Biomedical Engineering},
 volume={51},
 number={6},
 pages={1034--1043},
 year={2004},
 publisher={IEEE}
}
```
### PhysioNet Citation
```bibtex
@article{goldberger2000physiobank,
  title={PhysioBank, PhysioToolkit, and PhysioNet: Components of a New Research Resource for Complex Physiologic Signals},
  author={Goldberger, A. and Amaral, L. and Glass, L. and Hausdorff, J. and Ivanov, P. C. and Mark, R. and others},
  journal={Circulation},
  volume={101},
  number={23},
  pages={e215--e220},
  year={2000}
}
```
---
Made with 🧠 and ❤️
