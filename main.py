from setuptools import setup, find_packages

setup(
    name="signal_ICT_StudentName_EnrollmentNo",   # <-- replace this
    version="0.1.0",
    description="Basic signals and operations packagimport numpy as np
import matplotlib.pyplot as plt

# import from local package
from signal_ICT_SnehFaldu_92510133030 import unitary_signals, trigonometric_signals, operations

def demo():

    n = np.arange(0, 20)  # indices 0..19 (length 20)

    # unit step
    step = unitary_signals.unit_step(n)

    # unit impulse
    impulse = unitary_signals.unit_impulse(n)

    # ramp
    ramp = unitary_signals.ramp_signal(n)

    t = np.linspace(0, 1, 500)  # time vector for continuous signals

    # sine wave
    sine = trigonometric_signals.sine_wave(2, 5, 0, t)

    # cosine wave
    cosine = trigonometric_signals.cosine_wave(2, 5, 0, t)

    # exponential signal (plotted inside function already)
    t_exp = np.linspace(0, 1, 100)
    exp_signal = trigonometric_signals.exponential_signal(1, 2, t_exp)

    # time shift sine wave
    shifted_sine = operations.time_shift(sine, 5)
    plt.plot(t, sine, label="Original Sine")
    plt.plot(t, shifted_sine, label="Shifted Sine (+5 samples)", linestyle='--')
    plt.title("Time Shift of Sine Wave")
    plt.xlabel("Time (s)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # time scale sine wave
    k = 2
    scaled_signal = operations.time_scale(sine, k)
    scaled_time = t[::k]  # adjust time axis
    plt.plot(t, sine, label="Original Sine Wave")
    plt.plot(scaled_time, scaled_signal, label=f"Time Scaled Sine Wave (k={k})")
    plt.title("Time Scaling of Sine Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()

    # signal addition: unit step + ramp
    added = operations.signal_addition(step, ramp)
    plt.stem(n[:len(added)], added)
    plt.title("Unit Step + Ramp (Addition)")
    plt.xlabel("n")
    plt.grid(True)
    plt.show()

    # signal multiplication: sine × cosine
    product = operations.signal_multiplication(sine, cosine)
    plt.plot(t[:len(product)], product)
    plt.title("Sine × Cosine (Multiplication)")
    plt.xlabel("Time (s)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    demo()
e for Signals & Systems demo",
    author="StudentName",
    author_email="student@example.com",
    packages=find_packages(),
    install_requires=["numpy", "matplotlib"],
    python_requires=">=3.8",
)
