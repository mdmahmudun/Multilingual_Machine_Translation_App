import warnings
warnings.filterwarnings('ignore')

import gradio as gr
import langid
import langcodes
from transformers import pipeline
import torch
from languages import languages

# Initialize the translation pipeline
translator = pipeline(task='translation', model="facebook/nllb-200-distilled-600M", torch_dtype=torch.bfloat16)


# Define the translation function
def translate_text(text, tgt_lang):
    # Detect source language
    src_lang_code, _ = langid.classify(text)
    tgt_lang_code = languages[tgt_lang]
    src_language_name = langcodes.Language.get(src_lang_code).language_name()
    # Translate text
    text_translated = translator(text, src_lang=src_lang_code, tgt_lang=tgt_lang_code)
    return src_language_name, text_translated[0]['translation_text']


detected_lang = gr.Textbox(label="Detected Source Language")

# Create the Gradio interface
iface = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter text here...", label = "Input Text.."),
        gr.Dropdown(list(languages.keys()), label="Target Language")
    ],
    outputs=[
        detected_lang,
        gr.Textbox(label="Translation"),
        
    ],
    allow_flagging = 'never',
    description="Translates text from one language to another using the NLLB model with automatic source language detection."
)

# Add Markdown content
markdown_content_translation = gr.Markdown(
    """
    <div style='text-align: center; font-family: "Times New Roman";'>
        <h1 style='color: #FF6347;'>Multilingual Machine Translation</h1>
        <h3 style='color: #4682B4;'>Model: facebook/nllb-200-distilled-600M</h3>
        <h3 style='color: #32CD32;'>Made By: Md. Mahmudun Nabi</h3>
    </div>
    """
)

# Combine the Markdown content and the demo interface
translation_with_markdown = gr.Blocks()
with translation_with_markdown:
    markdown_content_translation.render()
    iface.render()
# Launch the Gradio app
if __name__ == "__main__":
    translation_with_markdown.launch()
