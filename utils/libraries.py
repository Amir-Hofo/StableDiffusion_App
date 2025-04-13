from flask import Flask, render_template, request
from PIL import Image
import secrets
import shutil
import platform
import subprocess
import requests
from io import BytesIO
import time
import os