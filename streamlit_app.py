import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Impostazioni della pagina
st.set_page_config(page_title="Proposta", layout="centered")

# CSS per un'estetica minimale, seria e formale
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&display=swap');

    .stApp {
        background-color: #fafafa;
    }
    
    .titolo-serio {
        font-family: 'Montserrat', sans-serif;
        color: #2b2b2b;
        font-size: 38px;
        font-weight: 800;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: 20px;
        margin-bottom: 20px;
        line-height: 1.3;
    }
    
    .formula-paragrafo {
        text-align: center;
        margin-top: 10px;
        padding: 15px;
        font-family: 'Montserrat', sans-serif;
        font-size: 16px;
        color: #2b2b2b;
    }
    </style>
    """, unsafe_allow_html=True)

# Titolo formale
st.markdown("<div class='titolo-serio'>Un piccolo regalo per il mio infinito amore verso di te</div>", unsafe_allow_html=True)

# Sfruttiamo un componente HTML/JS leggerissimo per fare il "true streaming" visivo del tracciato 
# calcolando i punti della curva direttamente nel browser o passandoli in blocco:
@st.cache_data
def precalcola_fotogrammi():
    x = np.linspace(-np.sqrt(3.3), np.sqrt(3.3), 800)
    frames_y = []
    for a in np.linspace(1, 30, 90):
        y = np.cbrt(x**2) + 0.9 * np.sqrt(3.3 - x**2) * np.sin(a * np.pi * x)
        frames_y.append(y.tolist())
    return x.tolist(), frames_y

x_vals, y_frames = precalcola_fotogrammi()

# Iniettiamo un piccolo script client-side (simile a un canvas in streaming) 
# che disegna l'animazione fluidamente a 30 FPS senza bloccare Python
import json
x_json = json.dumps(x_vals)
y_json = json.dumps(y_frames)

animazione_stream_html = f"""
<div style="display: flex; justify-content: center; align-items: center; width: 100%;">
    <canvas id="cuoreCanvas" width="450" height="400"></canvas>
</div>
<script>
const canvas = document.getElementById('cuoreCanvas');
const ctx = canvas.getContext('2d');

const xData = {x_json};
const framesY = {y_json};
let currentFrame = 0;

function draw() {{
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Configurazione scala e centro del grafico
    const xMin = -2.5, xMax = 2.5;
    const yMin = -1.5, yMax = 3.5;
    
    function scaleX(x) {{ return (x - xMin) / (xMax - xMin) * canvas.width; }}
    function scaleY(y) {{ return canvas.height - (y - yMin) / (yMax - yMin) * canvas.height; }}
    
    const yData = framesY[currentFrame];
    
    ctx.beginPath();
    ctx.strokeStyle = '#7a0010';
    ctx.lineWidth = 2.5;
    
    for (let i = 0; i < xData.length; i++) {{
        let px = scaleX(xData[i]);
        let py = scaleY(yData[i]);
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
    }}
    ctx.stroke();
    
    // Avanzamento fotogramma (effetto streaming continuo)
    currentFrame = (currentFrame + 1) % framesY.length;
}

// Loop di rendering a circa 30 fps
setInterval(draw, 35);
</script>
"""

# Mostriamo il canvas in streaming nel browser
st.components.v1.html(animazione_stream_html, height=420)

# Formula matematica statica posizionata sotto
st.markdown(r"""
<div class="formula-paragrafo">

$$ \text{Regalo} = dx, \quad \int_{\text{te}}^{\text{me}} \text{Amore} \, dx = +\infty $$

</div>
""", unsafe_allow_html=True)