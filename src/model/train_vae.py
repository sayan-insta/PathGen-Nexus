"""
Train Variational AutoEncoder
"""

from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset

from src.logger.logger import logger
from src.model.vae import VAE


DATA_PATH = Path("data/processed/selected_features.csv")
MODEL_PATH = Path("models/vae_model.pth")
LATENT_PATH = Path("data/processed/latent_features.csv")

MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)


class VAETrainer:

    def train(
        self,
        epochs=10,
        batch_size=16,
        learning_rate=1e-4,
        beta=0.1
    ):

        logger.info("Loading Feature Matrix")

        df = pd.read_csv(DATA_PATH, index_col=0)

        print("\nBefore Cleaning")
        print("Shape :", df.shape)
        print("NaN :", df.isna().sum().sum())

        # ---------------------------------
        # Remove empty columns
        # ---------------------------------

        df = df.dropna(axis=1, how="all")

        # ---------------------------------
        # Replace remaining NaN with column median
        # ---------------------------------

        df = df.apply(lambda c: c.fillna(c.median()))

        # ---------------------------------
        # Safety
        # ---------------------------------

        df = df.replace([np.inf, -np.inf], 0)

        # ---------------------------------
        # Remove zero variance columns
        # ---------------------------------

        variance = df.var()

        df = df.loc[:, variance > 0]

        print("\nAfter Cleaning")
        print("Shape :", df.shape)
        print("NaN :", df.isna().sum().sum())

        # ---------------------------------
        # Log Transform
        # ---------------------------------

        df = np.log1p(df)

        # ---------------------------------
        # Standardize
        # ---------------------------------

        scaler = StandardScaler()

        x = scaler.fit_transform(df)

        x = np.nan_to_num(x)

        x = torch.tensor(
            x,
            dtype=torch.float32
        )

        print("\nTensor")
        print("NaN :", torch.isnan(x).any().item())
        print("Inf :", torch.isinf(x).any().item())
        print("Shape :", x.shape)

        dataset = TensorDataset(x)

        loader = DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=True
        )

        model = VAE(
            input_dim=x.shape[1]
        )

        optimizer = torch.optim.Adam(
            model.parameters(),
            lr=learning_rate
        )

        model.train()

        logger.info("Training Started")

        for epoch in range(epochs):

            total_loss = 0

            for (batch,) in loader:

                optimizer.zero_grad()

                reconstructed, mu, logvar = model(batch)

                recon_loss = F.mse_loss(
                    reconstructed,
                    batch,
                    reduction="mean"
                )

                kl_loss = -0.5 * torch.mean(
                    1 + logvar - mu.pow(2) - logvar.exp()
                )

                loss = recon_loss + beta * kl_loss

                if torch.isnan(loss):
                    print("NaN detected!")
                    return

                loss.backward()

                torch.nn.utils.clip_grad_norm_(
                    model.parameters(),
                    1.0
                )

                optimizer.step()

                total_loss += loss.item()

            print(
                f"Epoch {epoch+1:02d}/{epochs}  Loss={total_loss:.6f}"
            )

        torch.save(
            model.state_dict(),
            MODEL_PATH
        )

        logger.info("Model Saved")

        model.eval()

        with torch.no_grad():

            hidden = model.encoder(x)

            latent = model.mu(hidden)

        latent_df = pd.DataFrame(
            latent.numpy(),
            index=df.index
        )

        latent_df.to_csv(
            LATENT_PATH
        )

        print("\nTraining Completed")
        print("Model :", MODEL_PATH)
        print("Latent :", LATENT_PATH)