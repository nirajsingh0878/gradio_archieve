import gradio as gr

def greet(name):
    return f"Hello,___ {name}________!!"


demo = gr.Interface(
    fn = greet,
    inputs="text",
    outputs = "text",
    title = "My First Gradio App",
    description="Enter you name and get a greeting"
)


demo.launch()
