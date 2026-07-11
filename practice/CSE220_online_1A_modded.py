import numpy as np
import matplotlib.pyplot as plt


def base_signal(t):
    x = np.exp(-t) * np.cos(t)
    x[(t < -np.pi) | (t > np.pi)] = 0
    return x


def shift_signal(t, x, c):
    """
    Shifts x(t) to produce x(t - c), i.e. delays the signal by c.
    Positive c -> shift right (delay)
    Negative c -> shift left (advance)
    """
    dt = t[1] - t[0]
    shift_idx = int(round(c / dt))

    y = np.roll(x, shift_idx)

    # zero out the wrapped portion (signal is 0 outside [-pi, pi])
    if shift_idx > 0:
        y[:shift_idx] = 0
    elif shift_idx < 0:
        y[shift_idx:] = 0

    return y


def transform_signal(t, x, alpha, beta):
    """
    y(t) = alpha * x(-t + beta)

    Order: SHIFT first, then REVERSE, then SCALE.

    Step 1 (shift): w(t) = x(t - c). We want w(t) such that
                    reversing it gives x(-t + beta).
                    w(-t) = x(-t - c) should equal x(-t + beta)
                    => c = -beta
                    So: w(t) = x(t - (-beta)) = x(t + beta)

    Step 2 (reverse): z(t) = w(-t) = x(-t + beta)

    Step 3 (scale): y(t) = alpha * z(t)
    """
    x_shifted = shift_signal(t, x, -beta)   # Step 1: x(t + beta)
    x_reversed = x_shifted[::-1]            # Step 2: x(-t + beta)
    y = alpha * x_reversed                  # Step 3: scale
    return y


def main():
    t = np.linspace(-np.pi, np.pi, 1000)
    x = base_signal(t)

    while True:
        user_input = input("enter alpha (or 'q' to quit): ")
        if user_input.strip().lower() == 'q':
            break

        alpha = float(user_input)
        beta = float(input("enter beta: "))

        y = transform_signal(t, x, alpha, beta)

        plt.figure(figsize=(8, 5))
        plt.plot(t, x, label='x(t)')
        plt.plot(t, y, label=f'y(t) = {alpha} * x(-t + {beta})')
        plt.xlabel('t')
        plt.ylabel('Amplitude')
        plt.title('Shift, Reversal, and Amplitude Scaling of x(t)')
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    main()