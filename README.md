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
For constracting the model, FastAI was used with DenseNet121 as backbone feature extractor. The model was trained on 20 epoch. <br>
At first the model was trained on raw data that resulted a poor performance. The notebook can be found [here](https://www.kaggle.com/code/naifislam/painting-classification-with-fastai?scriptVersionId=135915170) <br>
After that, the data was manually cleaned. The data cleaning process can be found [in this notebook](https://github.com/NifulIslam/Painting-Classifier/blob/main/notebooks/Data%20Clean.ipynb) <br>
Later, the model was again trained on the cleaned dataset that resulted in imporved performance. The updated moel is available in [this notebook](https://www.kaggle.com/code/naifislam/painting-classification-with-fastai?scriptVersionId=136266989).

# Model Deployment
The model was deployed on hugging face. [hugging face app url](https://huggingface.co/spaces/NifulIslam/Painting-Classification). 
# API integration with GitHub Pages
Lastly, the hugging face api was integrated on github. Do check the github page [here](https://nifulislam.github.io/Painting-Classifier/).

