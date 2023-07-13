from fastai import *
from fastai.vision.all import *
from fastai.vision.widgets import *
from PIL import ImageFile
import gradio as gr

root='paintings/data/'
dblock = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files,           
    splitter=RandomSplitter(valid_pct=0.1, seed=42),
    get_y=parent_label,                             
    item_tfms=Resize(128))   
dataloader=dblock.dataloaders(root, bs=8)

dblock = dblock.new(item_tfms=Resize(224, ResizeMethod.Squish), batch_tfms=aug_transforms(do_flip=True,
                                                                                         flip_vert=True,
                                                                                          max_rotate=10,
                                                                                          max_lighting=0.1,
                                                                                         )) 
dls = dblock.dataloaders(root)

model = cnn_learner(dls, densenet201, metrics=[error_rate,accuracy])
model.load('modelv2')


def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(model.dls.vocab, map(float, probs)))
    
image = gr.inputs.Image(shape=(224,224))
label = gr.outputs.Label(num_top_classes=10)

examples = [
    'test_img/still-life.jpeg',
    'test_img/landscape.jpeg',
    'test_img/abstract2.jpg',
    ]
    
    
iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)
