import gradio as gr
import lightning as L
from lightning.app.storage import Drive
from lightning.app.components.serve import ServeGradio

class MasterpieceCreator(ServeGradio):
    inputs = [gr.inputs.Textbox(label="print your prompt here"), gr.inputs.Number(default=250, label="number of steps")]
    outputs = gr.outputs.Image(type="auto", label="Your masterpiece will be here")
    enable_queue = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.drive_1 = Drive("lit://drive_1")

    def predict(self, prompt, number_of_steps):
        results = self.model.create(
          text_prompts=prompt,
          width_height=[512, 448],
          n_batches=1,
          steps=number_of_steps,
          diffusion_model="watercolordiffusion",
          clip_models=["ViT-B-32::openai"],
          clip_guidance_scale=40000,
        )

        file_name = f"./img.png"
        result = results[0]
        result.load_uri_to_image_tensor()
        result.save_image_tensor_to_file(file_name)
        self.drive_1.put(file_name)
        return result.tensor

    def build_model(self):
      import discoart
      return discoart

class RootFlow(L.LightningFlow):
  def __init__(self):
     super().__init__()
     self.work = MasterpieceCreator(cloud_compute=L.CloudCompute("gpu"))
  
  def run(self, *args, **kwargs) -> None:
     self.work.run()
  
  def configure_layout(self):
     return {"name": "DiscoArt", "content": self.work.url}


app = L.LightningApp(RootFlow())
