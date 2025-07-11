#Text Processing with Multiple Features

import gradio as gr


def analyze_text(text):
    word_count = len(text.split())
    char_count = len(text)
    char_count_no_space = len(text.replace(" ",""))

    return {
        "Word_count":word_count,
        "Character Count":char_count,
        "Character Count(no space)":char_count_no_space,
        "Uppercase":text.upper(),
        "Lowercase":text.lower(),
        "Reversed":text[::-1]
    }


def process_text(text):
    stats = analyze_text(text)
    
    return (
        f"Words: {stats['Word_count']}\nChars: {stats['Character Count']}\nChars (no spaces): {stats['Character Count(no space)']}",
        stats['Uppercase'],
        stats['Lowercase'],
        stats['Reversed']
    )

demo = gr.Interface(
    fn=process_text,
    inputs=gr.Textbox(label="Enter your text", lines=3),
    outputs=[
        gr.Textbox(label="Statistics"),
        gr.Textbox(label="Uppercase"),
        gr.Textbox(label="Lowercase"),
        gr.Textbox(label="Reversed")
    ],
    title="Text Analyzer",
    description="Analyze and transform your text in multiple ways!"
)

demo.launch()