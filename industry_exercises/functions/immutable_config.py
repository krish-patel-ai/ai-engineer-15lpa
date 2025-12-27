def get_training_config():
    learning_rate = 0.01
    batch_size = 32
    epochs = 10

    return learning_rate, batch_size, epochs


# Test code (outside the function)
config = get_training_config()

lr, batch, epochs = config

print(lr)
print(batch)
print(epochs)