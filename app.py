import gradio as gr
import subprocess

def run_command(cmd):
    if not cmd.strip():
        return "Escribe aquí tu comando..."
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        out = res.stdout + res.stderr
        return out if out else "✅ Ejecutado"
    except Exception as e:
        return f"❌ Error: {e}"

css = """
body {
    background: #121212;
    color: #00ffff !important;
    font-family: 'Courier New', monospace;
}
.gr-textbox, textarea {
    background: #1e1e1e !important;
    color: #00ffff !important;
    border: 2px solid #00ffff !important;
    box-shadow: 0 0 10px #00ffff55 !important;
    border-radius: 12px !important;
}
.gr-button-primary {
    background: #333333 !important;
    color: #00ffff !important;
    border: 2px solid #00ffff !important;
    border-radius: 12px !important;
    box-shadow: 0 0 12px #00ffff44 !important;
    font-weight: bold !important;
}
h1, h2, h3, label {
    color: #00ffff !important;
    text-align: center !important;
    text-shadow: 0 0 8px #00ffff, 0 0 15px #00ccff !important;
}
"""

with gr.Blocks(title="KALI LINUX — NACHO CORONEL", css=css) as demo:
    gr.Markdown("""
# 🐉 KALI LINUX · TERMINAL NEÓN
## ✦ NACHO CORONEL ✦
### ⚡ Elegua me cuida el camino | SISTEMA ACTIVO
""")
    
    with gr.Row():
        entrada = gr.Textbox(label="💻 COMANDO", placeholder="Escribe aquí tu comando...", lines=1)
        ejecutar = gr.Button("▶ EJECUTAR", variant="primary")
    
    salida = gr.Textbox(label="📤 SALIDA DEL SISTEMA", lines=16, interactive=False)
    
    gr.Markdown("---\n### ✨ *INVICTO · NO PERDONO, NO OLVIDO* ✨")
    
    ejecutar.click(run_command, entrada, salida)
    entrada.submit(run_command, entrada, salida)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7862)

