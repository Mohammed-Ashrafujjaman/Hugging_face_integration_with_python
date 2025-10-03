


class information():
    
    def show_brief_gen_ai_info():
        info = (
                "Model: google/flan-t5-small\n\n"
                "Type: Generative Text-to-Text Transformer\n"
                "Description: A small variant of the FLAN-T5 model fine-tuned for various text generation tasks.\n"
                "Use Case: Performs tasks like summarization, translation, question answering, and more."
                "Limitations: Limited reasoning power compared to larger models, may produce biased or inaccurate text and cannot provide knowledge beyond its training data."
            )
        return info
    
    def show_brief_img_classifier_info():
        info = (
                "Model: google/vit-base-patch16-224\n\n"
                "Type: Image Classification\n"
                "Description: Vision Transformer (ViT) model trained on ImageNet-21k and fine-tuned on ImageNet-1k.\n"
                "Use Case: Classifies images into thousands of possible object categories."
                "Limitations: Requires significant compute resources, less effective on noisy/low-resolution images and limited to classification (not detection or segmentation)."
            )
        return info
    
    def show_Gen_AI_model_explanations():

            info = (
                    "Flan-T5-base Overview:\n"
                    "\n"
                    "Description:\n"
                    "An instruction-tuned text-to-text model by Google.\n"
                    "Strong at following prompts and general language tasks.\n"
                    "\n"
                    "Question Scope:\n"
                    "• Factual Q&A \n"
                    "• Instruction following \n"
                    "• Basic math and reasoning \n"
                    "• Translation (limited) \n"
                    "• Summarization \n"
                    "\n"
                    "Limitations:\n"
                    "• Weak at multi-step logic \n"
                    "• No memory or conversation context \n"
                    "• Limited context length (~1K tokens) \n"
                    "• Struggles with coding tasks \n"
                    "• Outdated knowledge (pre-2023) \n"
                    )
            return info
            
            
    
    def show_image_classifier_info():
         info = (
                    "ViT-Base (google/vit-base-patch16-224)\n"
                    "\n"
                    "Description:\n"
                    "A Vision Transformer model by Google that splits an image into 16x16 patches,\n"
                    "embeds them as tokens, and processes via a transformer encoder. :contentReference[oaicite:0]{index=0}\n"
                    "Pretrained on ImageNet-21k, fine-tuned on ImageNet-1k. :contentReference[oaicite:1]{index=1}\n"
                    "\n"
                    "Task Scope (What it can do):\n"
                    "• Image classification into ~1000 ImageNet classes :contentReference[oaicite:2]{index=2}\n"
                    "• Feature extraction / embedding for visual tasks (use as backbone) :contentReference[oaicite:3]{index=3}\n"
                    "• Transfer learning to downstream vision tasks (with additional head) :contentReference[oaicite:4]{index=4}\n"
                    "\n"
                    "Limitations:\n"
                    "• Not designed for tasks like object detection, segmentation, or dense prediction without adaptation\n"
                    "• Fixed input resolution (224x224) — may lose detail on very high-res images\n"
                    "• May misclassify if image has heavy occlusion, novel classes, or domain shift\n"
                    "• No inherent reasoning about spatial layout beyond learned embeddings\n"
                    "• Knowledge limited to what it saw during training (ImageNet domain)\n"
                )
         return info
     
    
    def show_OOP_explanations():
        explanation = (
            "Our Implementation shows Object-Oriented Programming (OOP):\n"

            "- Class: For GUI (MainWindow) and for model wrappers in AI_models.\n"
            "- Object: Instances are created when we run on the GUI or load model, e.g., bert = HuggingFaceModel('bert-base-uncased').\n"
            "- Attributes & Methods: Every class has attributes (model name, device) and methods (load, predict).\n"
            "- Inheritance: Various model classes inherit from a BaseModelWrapper so they have some of the same methods.\n"
            "- Polymorphism: The GUI rings model.predict(text) and it's model agnostic.\n"
            "- Encapsulation: Expose a simple interface and hide the complexity (e.g., the tokenizers, device configs) away from user methods.\n"
            "- Abstraction: The GUI works only with high-level methods (load_model, predict); it does not worry about Hugging Face internals.\n"
            "- Composition: The MainWindow is a container of other objects (such as ModelManager) and this separates parts from each other.\n"

            "OOP, all in all, makes our project modular, reusable, and very easy to extend.\n"
        )
        return explanation
    
    
    def show_required_packages():
        packages_info = (
        "Please install this packages for run this software.\n"
        "Packages needed:\n"
        "   transformers\n"
        "   huggingface_hub\n"
        "   Pillow\n"
        "   torch\n"
        "   Tkinter\n" 
        "   sentencepiece\n"
        "   protobuf\n\n"
        "pip install transformers huggingface_hub Pillow torch sentencepiece protobuf\n"
        "Upper command will install all the package needed to run this project."
        )
        return packages_info
    
    def show_initial_message():
        info = (
        "Hello Dear user!\n"
        "If you are running this project for the first time it will take sometime to download the models. You will see all the progress in terminal windows.\n"
        "We kindly request you to be patient.\n"
        "Note: Download speed may vary depending on your internet connection.\n\n"
        "pip install -r requirements.txt\n"
        "Type the upper line in terminal to install all the required packages."
        )
        return info