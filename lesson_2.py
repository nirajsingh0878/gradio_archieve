# Multiple Inputs and Outputs

import gradio as gr

def calculate(num1,num2,operation):
    if operation=="Add":
        return num1+num2
    elif operation=='Subtract':
        return num1- num2
    elif operation=='Multiply':
        return num1* num2
    elif operation=='Divide':
        return num1/num2
    

demo = gr.Interface(
    fn = calculate,
    inputs=[
        gr.Number(label="First Number"),
        gr.Number(label="Second Number"),
        gr.Dropdown(["Add","Subtract","Multiply","Divide"],label='operation')
    ],
    outputs = gr.Textbox(label='Result'),
    title = 'Simple Calculator',
    examples = [
        [10,5,'Add'],
        [20,4,'Subtract'],
        [7,3,'Multiply'],
        
    ]       
)

demo.launch()