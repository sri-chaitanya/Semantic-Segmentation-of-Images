import streamlit as st
import mxnet as mx
from mxnet import image
from mxnet.gluon.data.vision import transforms
import gluoncv
from PIL import Image
from matplotlib import pyplot as plt
from gluoncv.data.transforms.presets.segmentation import test_transform
from gluoncv.utils.viz import get_color_pallete
import matplotlib.image as mpimg
import cv2
import numpy as np
ctx = mx.cpu(0)


def main():
	st.title("Semantic Segmentation App for Images")
	st.text("Built with gluoncv and Streamlit")
	st.markdown("### [Semantic Segmentation](https://towardsdatascience.com/semantic-segmentation-with-deep-learning-a-guide-and-code-e52fc8958823)\
     `            `[PSPNet](https://towardsdatascience.com/review-pspnet-winner-in-ilsvrc-2016-semantic-segmentation-scene-parsing-e089e5df177d) \
	 `			  `[[Paper]](https://arxiv.org/abs/1612.01105)\
	 `			  `[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/Hardly-Human/Semantic-Segmentation-of-Images)\
	 `            `[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://lbesson.mit-license.org/)")



if __name__ == "__main__":
	main()