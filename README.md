
<img align="center" height="500px" width="1000px" src="https://github.com/NifulIslam/Painting-Classifier/blob/main/photos/SamplePaintings.png" alt="Hugging face">

# Clsssifier
This image classifier can classify 10 tyepes of painging. The types are: <br>
1. Landscape
2. Portrait
3. Still Life
4. Abstract
5. Impressionist
6. Cubist
7. Surrealist
8. Expressionist
9. Realist
10. Pop Art
# Dataset Preparation
The images were collected from duckduckgo. The image collection code can be found [here](https://www.kaggle.com/code/naifislam/download-image-from-duckduckgo)
# Training and Data Cleaning
For constracting the model, FastAI was used with DenseNet121 as backbone feature extractor. DenseNet is comprised of dense blocks where features extracted from the previous layers are propagated to the subsequent layers. The figure of dense block is presented below. DenseNet performs better in painting image classification due to its dense connectivity, which allows for effective information propagation and feature reuse throughout the network. Due to the significant impact of high-level features on this problem, DenseNet yields impressive classification accuracy. The model was trained on 20 epoch. <br>
<img align="center" height="300px" width="400px" src="https://raw.githubusercontent.com/NifulIslam/Painting-Classifier/main/photos/densenet.png" alt="Dense block">

At first the model was trained on raw data that resulted a poor performance. The notebook can be found [here](https://www.kaggle.com/code/naifislam/painting-classification-with-fastai?scriptVersionId=135915170) <br>
After that, the data was manually cleaned. The data cleaning process can be found [in this notebook](https://github.com/NifulIslam/Painting-Classifier/blob/main/notebooks/Data%20Clean.ipynb) <br>
Later, the model was again trained on the cleaned dataset that resulted in imporved performance. The updated moel is available in [this notebook](https://www.kaggle.com/code/naifislam/painting-classification-with-fastai?scriptVersionId=136266989).

# Model Deployment
The model was deployed on hugging face. [hugging face app link](https://huggingface.co/spaces/NifulIslam/Painting-Classification). 

<img align="center" height="500px" width="800px" src="https://github.com/NifulIslam/Painting-Classifier/blob/main/photos/hugging-face.png" alt="Hugging face">

# API integration with GitHub Pages
Lastly, the hugging face api was integrated on github. Do check the github page [here](https://nifulislam.github.io/Painting-Classifier/).

<img align="center" height="500px" width="900px" src="https://github.com/NifulIslam/Painting-Classifier/blob/main/photos/github.png" alt="Github Page">

