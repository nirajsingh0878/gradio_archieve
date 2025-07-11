import gradio as gr

def increment(count):
    new_count = count + 1
    return new_count, new_count  

def decrement(count):
    new_count = count - 1
    return new_count, new_count  

def reset():
    return 0, 0  

with gr.Blocks() as demo:
    gr.Markdown("# counter app")
    
    # state to store the counter value
    counter_state = gr.State(value=0)
    
    with gr.Row():
        with gr.Column():
            counter_display = gr.Number(label="Current Count", value=0, interactive=False)
            
            with gr.Row():
                increment_btn = gr.Button(" + Add 1")
                decrement_btn = gr.Button(" - Subtract 1")
                reset_btn = gr.Button(" ~ Reset")
    
    # this is event handlers that update both state and display
    increment_btn.click(
        fn=increment,
        inputs=counter_state,
        outputs=[counter_state, counter_display]
    )
    
    decrement_btn.click(
        fn=decrement,
        inputs=counter_state,
        outputs=[counter_state, counter_display]
    )
    
    reset_btn.click(
        fn=reset,
        inputs=None,
        outputs=[counter_state, counter_display]
    )

demo.launch()