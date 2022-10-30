# The Discoart App

Masterpiece creator uses the [discoart](https://github.com/jina-ai/discoartf) library to create Disco Diffusion artworks.

## Run on the cloud
```bash
lightning run app app.py --cloud
```
## Run locally
```bash
lightning run app app.py
```

## How does it work?

1. Type your prompt into the first input.
2.  Choose the model that suits your prompt best. For example, `portrait_generator_v1.5` and `portrait_generator_v001_ema_0.9999_1MM` are the best options if you want to get a portrait
3. Enter the number of steps (the default is 250; but some models perform best when you run them for way more steps).
4. Hit the Submit button and let it run. The average generation time is about 13 minutes.
