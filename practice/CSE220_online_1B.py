import numpy as np
import matplotlib.pyplot as plt

DT = 0.05  # sampling interval for the time axis
T_MIN, T_MAX = -np.pi, np.pi  # x(t) is defined only on this range


def generate_time_axis(t_min=T_MIN, t_max=T_MAX, dt=DT):
    return np.arange(t_min, t_max + dt / 2, dt)


def base_signal(t):
    x = np.sin(t)
    x[(t < T_MIN) | (t > T_MAX)] = 0
    return x


def interpolate_signal(x, index_float):
    n = len(x)
    # clamp instead of rejecting due to float error
    index_float = max(0.0, min(index_float, n - 1))
    left = int(np.floor(index_float))
    right = int(np.ceil(index_float))
    if left == right:
        return x[left]
    return 0.5 * (x[left] + x[right])


def transform_signal(t, x, alpha, beta):
    """
    Computes y(t) = x(alpha * t + beta)
    """
    dt = t[1] - t[0]
    n = len(t)
    y = np.zeros(n)

    for i in range(n):
        query_t = alpha * t[i] + beta  # the time we need to sample x at

        if T_MIN <= query_t <= T_MAX:
            # Convert the continuous query time into a fractional sample
            # index on the (T_MIN-based) time axis.
            index_float = (query_t - T_MIN) / dt
            y[i] = interpolate_signal(x, index_float)
        # else: outside x's support -> leave as 0, per "values outside range are 0"
    return y


def plot_signals(t, x, y, alpha, beta):
    plt.figure(figsize=(9, 5))
    plt.plot(t, x, label="x(t)", linewidth=2)
    plt.plot(t, y, label=f"y(t) = x({alpha}t + {beta})", linewidth=2, linestyle="--")
    plt.title("Time Scaling and Shifting of a Signal")
    plt.xlabel("t")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    t = generate_time_axis()
    x = base_signal(t)

    while True:
        alpha_in = input("Enter alpha (or 'q' to quit): ").strip()
        if alpha_in.lower() == 'q':
            break

        beta_in = input("Enter beta (or 'q' to quit): ").strip()
        if beta_in.lower() == 'q':
            break

        try:
            alpha = float(alpha_in)
            beta = float(beta_in)
        except ValueError:
            print("Please enter valid numbers (or 'q' to quit).")
            continue

        if alpha <= 0:
            print("alpha must be > 0.")
            continue

        y = transform_signal(t, x, alpha, beta)
        plot_signals(t, x, y, alpha, beta)

    print("Exiting.")


if __name__ == "__main__":
    main()