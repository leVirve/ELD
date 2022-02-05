import torch.nn as nn

from .Unet import UNetSeeInDark


def unet(in_channels, out_channels, **kwargs):
    return UNetSeeInDark(in_channels, out_channels)
