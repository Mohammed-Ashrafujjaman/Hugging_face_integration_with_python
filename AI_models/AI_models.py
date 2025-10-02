'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121   # Generative AI part
Al-Amin Dhaly - 395230   # Image Classifier part
'''

from transformers import pipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration 

class AIModels:
    def __init__(self):
        # Initialize image classifier model
        self._imgClassifier_modelName = "google/vit-base-patch16-224"
        self.ImgClassifier = self._image_classification_pipeline(self._imgClassifier_modelName)
        
    #Implementation
    def _image_classification_pipeline(self, modelName):
        #Create HuggingFace image classification pipeline
        return pipeline("image-classification", model=modelName)
        
    def get_ImageClassifierAI_model_name(self):
        #Return the name of the image classifier model
        return self._imgClassifier_modelName
    
    def run_image_classifier(self, imgPath):
        #Run classification on a given image path
        output = self.ImgClassifier(imgPath)
        return output
                
if __name__ == "__main__":
    AIs = AIModels()
    
    # Test with sample image
    img_path = "D:/software_now/Assignment_3/Hugging_face_integration_with_python/utils/cat.jpg"
    img_output = AIs.run_image_classifier(img_path)
    print(img_output[0]["label"])
    
    # End of Al-Amin’s part

"""
REFERENCES
[1] Hugging Face, “Image classification with pipelines,” Hugging Face Documentation, 2024. [Online]. 
    Available: https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.ImageClassificationPipeline, [Accessed: Oct. 1, 2025].

[2] Hugging Face, “T5: Text-To-Text Transfer Transformer,” Hugging Face Models, 2024. [Online]. 
    Available: https://huggingface.co/docs/transformers/model_doc/t5, [Accessed: Oct. 1, 2025].

"""