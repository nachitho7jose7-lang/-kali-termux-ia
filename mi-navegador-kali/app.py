import gradio as gr
import subprocess

historial = []

def ejecutar_comando(cmd):
    if not cmd.strip(): return ""
    historial.append(f"root@kali:~# {cmd}")
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        out = (r.stdout + r.stderr).strip() or "✓ Comando ejecutado"
        return f"{historial[-1]}\n{out}"
    except Exception as e:
        return f"{historial[-1]}\n✗ Error: {str(e)}"

def asistente(txt):
    t = txt.lower().strip()
    if "hola" in t: return "¡Hola Nachito! 🐉✨ Sistema NEÓN activo."
    if "quién eres" in t: return "Tu asistente — tú me creaste."
    if "ayuda" in t: return "Comandos: ls / pwd / whoami / clear"
    if "gracias" in t: return "¡De nada, carnal! 💪🔥"
    if "nombre" in t: return "Nachito Corral 👑"
    return f"📋 Dijiste: {txt}"

estilo = """
html, body {
    margin: 0 !important;
    padding: 0 !important;
    background: #000 !important;
    color: #00e5ff !important;
    font-family: 'Courier New', monospace !important;
}
.gradio-container {
    max-width: 100% !important;
    padding: 15px !important;
    background: radial-gradient(circle at top left, rgba(0,229,255,0.08), transparent 35%),
                radial-gradient(circle at bottom right, rgba(128,128,128,0.12), transparent 35%),
                linear-gradient(180deg, #050505 0%, #101010 50%, #080808 100%) !important;
}
.dragon-icon {
    font-size: 32px !important;
    text-align: center !important;
    margin-bottom: 5px !important;
    text-shadow: 0 0 10px #00e5ff, 0 0 20px rgba(128,128,128,0.8) !important;
}
.titulo {
    color: #00e5ff !important;
    text-align: center !important;
    font-size: 22px !important;
    font-weight: bold !important;
    letter-spacing: 2px !important;
    text-shadow: 0 0 8px #00e5ff, 0 0 15px #00e5ff, 0 0 25px rgba(0,229,255,0.8) !important;
    margin-bottom: 5px !important;
}
.subtitulo {
    color: #c8c8c8 !important;
    text-align: center !important;
    font-size: 13px !important;
    letter-spacing: 1px !important;
    text-shadow: 0 0 6px rgba(200,200,200,0.8), 0 0 12px rgba(0,229,255,0.6) !important;
    margin-bottom: 20px !important;
}
.fila {
    display: flex !important;
    flex-direction: row !important;
    gap: 15px !important;
    width: 100% !important;
}
.panel {
    flex: 1 !important;
}
.etiqueta {
    color: #00e5ff !important;
    font-weight: bold !important;
    font-size: 15px !important;
    margin-bottom: 8px !important;
    letter-spacing: 2px !important;
    text-shadow: 0 0 8px #00e5ff, 0 0 15px rgba(0,229,255,0.8) !important;
}
.caja-entrada {
    background: rgba(10,10,10,0.85) !important;
    border: 1px solid #808080 !important;
    color: #00e5ff !important;
    font-family: 'Courier New', monospace !important;
    box-shadow: 0 0 8px rgba(128,128,128,0.6), inset 0 0 6px rgba(0,229,255,0.15) !important;
}
.caja-entrada::placeholder {
    color: #a0a0a0 !important;
    opacity: 0.75 !important;
}
.caja-salida {
    background: rgba(8,8,8,0.9) !important;
    border: 1px solid #808080 !important;
    color: #00e5ff !important;
    font-family: 'Courier New', monospace !important;
    height: 300px !important;
    overflow-y: auto !important;
    box-shadow: 0 0 10px rgba(128,128,128,0.7), inset 0 0 8px rgba(0,229,255,0.2) !important;
}
.boton-neon {
    background: linear-gradient(135deg, #00e5ff, #00ccff) !important;
    color: #000 !important;
    font-weight: bold !important;
    border: none !important;
    margin-top: 8px !important;
    letter-spacing: 2px !important;
    box-shadow: 0 0 12px #00e5ff, 0 0 20px rgba(128,128,128,0.5), 0 0 30px rgba(0,229,255,0.4) !important;
}
.boton-neon:hover {
    background: linear-gradient(135deg, #33f0ff, #00e5ff) !important;
    box-shadow: 0 0 18px #00e5ff, 0 0 30px rgba(128,128,128,0.7), 0 0 45px rgba(0,229,255,0.6) !important;
}
@media (max-width: 767px) {
    .fila { flex-direction: column !important; }
}
"""

with gr.Blocks(css=estilo, title="KALI NEÓN — Nachito Corral") as demo:
    gr.Markdown("""
    <div class="dragon-icon">🐉</div>
    <div class="titulo">KALI LINUX • TERMINAL NEÓN</div>
    <div class="subtitulo">Gira el teléfono de lado ✦ NACHO CORRAL SYSTEM</div>
    """)

    with gr.Row(elem_classes="fila"):
        with gr.Column(elem_classes="panel"):
            gr.Markdown('<div class="etiqueta">◈ TERMINAL</div>')
            entrada = gr.Textbox(
                label="",
                placeholder="root@kali:~# escribe tu comando...",
                lines=1,
                elem_classes="caja-entrada"
            )
            btn1 = gr.Button("▶ EJECUTAR", elem_classes="boton-neon")
            salida = gr.Textbox(
                label="",
                lines=12,
                interactive=False,
                elem_classes="caja-salida"
            )

        with gr.Column(elem_classes="panel"):
            gr.Markdown('<div class="etiqueta">◈ ASISTENTE</div>')
            pregunta = gr.Textbox(
                label="",
                placeholder="Pregúntame lo que quieras...",
                lines=2,
                elem_classes="caja-entrada"
            )
            btn2 = gr.Button("💬 ENVIAR", elem_classes="boton-neon")
            resp = gr.Textbox(
                label="",
                lines=12,
                interactive=False,
                elem_classes="caja-salida"
            )

    btn1.click(ejecutar_comando, entrada, salida)
    entrada.submit(ejecutar_comando, entrada, salida)
    btn2.click(asistente, pregunta, resp)
    pregunta.submit(asistente, pregunta, resp)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
