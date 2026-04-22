import os

os.makedirs("outputs/models", exist_ok=True)

globals().keys()
transfer_model.save("outputs/models/transfer_learning_model.keras")