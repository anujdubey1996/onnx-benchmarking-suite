import matplotlib.pyplot as plt

def plot_performance(results):
    models, latencies, throughputs = zip(*results)
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Models')
    ax1.set_ylabel('Latency (s)', color=color)
    ax1.plot(models, latencies, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Throughput (req/s)', color=color)
    ax2.plot(models, throughputs, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example results
    results = [("Model1", 0.01, 100), ("Model2", 0.02, 50)]
    plot_performance(results)
