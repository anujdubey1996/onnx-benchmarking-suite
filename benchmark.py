import time
import numpy as np
import onnxruntime as ort
from load_model import load_model

def generate_dummy_input(input_shape):
    return np.random.randn(*input_shape).astype(np.float32)

def measure_performance(model_path, input_shape, runs=100):
    session = ort.InferenceSession(model_path)
    input_name = session.get_inputs()[0].name
    dummy_input = generate_dummy_input(input_shape)
    
    start_time = time.time()
    for _ in range(runs):
        session.run(None, {input_name: dummy_input})
    end_time = time.time()
    
    latency = (end_time - start_time) / runs
    throughput = runs / (end_time - start_time)
    return latency, throughput

if __name__ == "__main__":
    model_path = "path_to_your_model.onnx"
    input_shape = (1, 3, 224, 224)  # Example shape, adjust according to your model
    latency, throughput = measure_performance(model_path, input_shape)
    print(f"Latency: {latency:.6f} seconds")
    print(f"Throughput: {throughput:.2f} requests/second")
