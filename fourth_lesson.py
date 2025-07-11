# Lesson 4: Introduction to Blocks (Custom Layout)
import gradio as gr

def process_text(text, operation):
    if operation == "upper":
        return text.upper()
    elif operation == "lower":
        return text.lower()
    elif operation == "reverse":
        return text[::-1]
    elif operation == "count":
        return f"Words: {len(text.split())}, Characters: {len(text)}"

with gr.Blocks(title="Text Processor") as demo:
    gr.Markdown("# Text Processing Tool")
    gr.Markdown("Choose an operation and process your text!")
    
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(label="Enter text", lines=3)
            
            with gr.Row():
                upper_btn = gr.Button("UPPERCASE")
                lower_btn = gr.Button("lowercase")
                reverse_btn = gr.Button("Reverse")
                count_btn = gr.Button("Count Words")
        
        with gr.Column():
            output = gr.Textbox(label="Result", lines=3)
    
    # this is where event is handled
    upper_btn.click(fn=lambda text: process_text(text, "upper"), inputs=text_input, outputs=output)
    lower_btn.click(fn=lambda text: process_text(text, "lower"), inputs=text_input, outputs=output)
    reverse_btn.click(fn=lambda text: process_text(text, "reverse"), inputs=text_input, outputs=output)
    count_btn.click(fn=lambda text: process_text(text, "count"), inputs=text_input, outputs=output)

demo.launch()