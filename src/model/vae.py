"""
Variational AutoEncoder (VAE)

Author: PathGen-Nexus
"""

import torch
import torch.nn as nn


class VAE(nn.Module):
    """
    Variational AutoEncoder for RNA Gene Expression Data
    """

    def __init__(
        self,
        input_dim: int,
        latent_dim: int = 128
    ):
        super(VAE, self).__init__()

        # -------------------------
        # Encoder
        # -------------------------

        self.encoder = nn.Sequential(

            nn.Linear(input_dim, 2048),
            nn.BatchNorm1d(2048),
            nn.ReLU(),
            nn.Dropout(0.20),

            nn.Linear(2048, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(),
            nn.Dropout(0.20),

            nn.Linear(1024, 512),
            nn.BatchNorm1d(512),
            nn.ReLU()
        )

        # Mean Layer
        self.mu = nn.Linear(512, latent_dim)

        # Log Variance Layer
        self.logvar = nn.Linear(512, latent_dim)

        # -------------------------
        # Decoder
        # -------------------------

        self.decoder = nn.Sequential(

            nn.Linear(latent_dim, 512),
            nn.ReLU(),

            nn.Linear(512, 1024),
            nn.ReLU(),

            nn.Linear(1024, 2048),
            nn.ReLU(),

            nn.Linear(2048, input_dim)
        )

    def encode(self, x):
        """
        Encode input into latent distribution
        """

        hidden = self.encoder(x)

        mu = self.mu(hidden)

        logvar = self.logvar(hidden)

        return mu, logvar

    def reparameterize(self, mu, logvar):
        """
        Reparameterization Trick
        """

        std = torch.exp(0.5 * logvar)

        eps = torch.randn_like(std)

        return mu + eps * std

    def decode(self, z):
        """
        Decode latent representation
        """

        return self.decoder(z)

    def forward(self, x):
        """
        Forward Pass
        """

        mu, logvar = self.encode(x)

        z = self.reparameterize(mu, logvar)

        reconstruction = self.decode(z)

        return reconstruction, mu, logvar

    def get_latent(self, x):
        """
        Return latent representation (Mean Vector)
        """

        self.eval()

        with torch.no_grad():

            mu, _ = self.encode(x)

        return mu