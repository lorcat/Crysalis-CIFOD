import os
import sys
import time
import re
import copy

import logging

import threading

from IPython.display import display
from ipywidgets import Button, Layout, Textarea, HBox, VBox, FileUpload, Output, Label, GridBox, HTML
h1 = HTML()

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

import asyncio
import numpy as np
from numpy import linalg as npla

from .keys import *

import plotly.graph_objects as go
from scipy.spatial.transform import Rotation as R