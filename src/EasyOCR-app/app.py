"""
Credits: This code is adapted from official Easy OCR : https://huggingface.co/spaces/tomofi/EasyOCR and https://github.com/JaidedAI/EasyOCR
"""

import easyocr
import gradio as gr
import lightning as L
import pandas as pd
import requests
import torch
from lightning.app.components.serve import ServeGradio
from PIL import Image, ImageDraw

choices = [
    "abq",
    "ady",
    "af",
    "ang",
    "ar",
    "as",
    "ava",
    "az",
    "be",
    "bg",
    "bh",
    "bho",
    "bn",
    "bs",
    "ch_sim",
    "ch_tra",
    "che",
    "cs",
    "cy",
    "da",
    "dar",
    "de",
    "en",
    "es",
    "et",
    "fa",
    "fr",
    "ga",
    "gom",
    "hi",
    "hr",
    "hu",
    "id",
    "inh",
    "is",
    "it",
    "ja",
    "kbd",
    "kn",
    "ko",
    "ku",
    "la",
    "lbe",
    "lez",
    "lt",
    "lv",
    "mah",
    "mai",
    "mi",
    "mn",
    "mr",
    "ms",
    "mt",
    "ne",
    "new",
    "nl",
    "no",
    "oc",
    "pi",
    "pl",
    "pt",
    "ro",
    "ru",
    "rs_cyrillic",
    "rs_latin",
    "sck",
    "sk",
    "sl",
    "sq",
    "sv",
    "sw",
    "ta",
    "tab",
    "te",
    "th",
    "tjk",
    "tl",
    "tr",
    "ug",
    "uk",
    "ur",
    "uz",
    "vi",
]


class LitGradio(ServeGradio):
    inputs = [
        gr.components.Image(type="file", label="Input"),
        gr.components.CheckboxGroup(
            choices, type="value", default=["en"], label="language"
        ),
    ]
    outputs = [
        gr.components.Image(type="file", label="Output"),
        gr.components.Dataframe(headers=["text", "confidence"]),
    ]
    examples = [
        ["english.png", ["en"]],
        ["chinese.jpg", ["ch_sim", "en"]],
        ["Hindi.jpeg", ["hi", "en"]],
    ]

    def draw_boxes(self, image, bounds, color="yellow", width=2):
        draw = ImageDraw.Draw(image)
        for bound in bounds:
            p0, p1, p2, p3 = bound[0]
            draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
        return image

    def inference(self, img, lang):
        reader = easyocr.Reader(lang)
        bounds = reader.readtext(img.name)
        im = Image.open(img.name)
        self.draw_boxes(im, bounds)
        im.save("result.jpg")
        return ["result.jpg", pd.DataFrame(bounds).iloc[:, 1:]]

    def predict(self, image, text):
        return self.model(image, text)

    def build_model(self):
        torch.hub.download_url_to_file(
            "https://github.com/JaidedAI/EasyOCR/raw/master/examples/english.png",
            "english.png",
        )
        torch.hub.download_url_to_file(
            "https://github.com/JaidedAI/EasyOCR/raw/master/examples/chinese.jpg",
            "chinese.jpg",
        )
        torch.hub.download_url_to_file("https://i.imgur.com/mwQFd7G.jpeg", "Hindi.jpeg")
        return self.inference


class RootFlow(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.lit_gradio = LitGradio()

    def run(self):
        self.lit_gradio.run()

    def configure_layout(self):
        return [{"name": "home", "content": self.lit_gradio.url}]


app = L.LightningApp(RootFlow())
