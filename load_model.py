import onnx

def load_model(model_path):
    try:
        model = onnx.load(model_path)
        onnx.checker.check_model(model)
        print(f"Model {model_path} is valid.")
        return model
    except onnx.onnx_cpp2py_export.checker.ValidationError as e:
        print(f"Model validation failed: {e}")
        return None

if __name__ == "__main__":
    model = load_model("path_to_your_model.onnx")
