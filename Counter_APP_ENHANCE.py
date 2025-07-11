import gradio as gr
import math

def update_counter(change, current_count):
    new_count = current_count + change
    if new_count < 0: 
        new_count = 0
    
    size = 200 + abs(new_count) * 2
    color = f"hsl({new_count % 360}, 70%, 60%)"
    shadow = f"0 0 {min(50, new_count)}px {color}"
    
    # create html visualization
    html = f"""
    <div style="
        width: {size}px;
        height: {size}px;
        background: {color};
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 60px;
        font-weight: bold;
        box-shadow: {shadow};
        transition: all 0.3s ease;
        margin: 20px auto;
    ">
        {new_count}
    </div>
    """
    return new_count, html

def increment(current_count):
    return update_counter(1, current_count)

def decrement(current_count):
    return update_counter(-1, current_count)

def reset():
    return 0, """
    <div style="
        width: 200px;
        height: 200px;
        background: #4285F4;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 60px;
        font-weight: bold;
        margin: 20px auto;
    ">
        0
    </div>
    """

with gr.Blocks(title="Amazing Counter") as demo:
    count_state = gr.State(value=0)
    
    gr.Markdown("# Visual Counter App")
    gr.Markdown("Click buttons to change the counter value!")
    
    visual_display = gr.HTML("""
    <div style="
        width: 200px;
        height: 200px;
        background: #4285F4;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 60px;
        font-weight: bold;
        margin: 20px auto;
    ">
        0
    </div>
    """)
    
    with gr.Row():
        plus_btn = gr.Button("➕ Add One", variant="primary")
        minus_btn = gr.Button("➖ Subtract One", variant="secondary")
        reset_btn = gr.Button("🔄 Reset", variant="stop")
    
    # this is event handlers
    plus_btn.click(
        fn=increment,
        inputs=count_state,
        outputs=[count_state, visual_display]
    )
    
    minus_btn.click(
        fn=decrement,
        inputs=count_state,
        outputs=[count_state, visual_display]
    )
    
    reset_btn.click(
        fn=reset,
        inputs=None,
        outputs=[count_state, visual_display]
    )

demo.launch()