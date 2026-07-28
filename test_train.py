from src.model.train_vae import VAETrainer

if __name__ == "__main__":

    trainer = VAETrainer()

    trainer.train(
        epochs=10,
        batch_size=16,
        learning_rate=1e-4
    )