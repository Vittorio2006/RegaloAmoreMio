import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import matplotlib.animation as animation

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
        margin-top: 5px;
        padding: 10px;
        font-family: 'Montserrat', sans-serif;
        font-size: 16px; /* Font ridotto */
        color: #2b2b2b;
    }
    </style>
    """, unsafe_allow_html=True)

# Titolo formale, grande e in grassetto
st.markdown("<div class='titolo-serio'>Un piccolo regalo per il mio infinito amore verso di te</div>", unsafe_allow_html=True)

# Funzione per generare il video HTML5 dell'animazione in memoria
@st.cache_resource
def genera_video_cuore():
    fig, ax = plt.subplots(figsize=(6, 5))
    fig.patch.set_alpha(0.0) 
    ax.patch.set_alpha(0.0)  
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-1.5, 3.5)
    ax.axis('off')  

    x = np.linspace(-np.sqrt(3.3), np.sqrt(3.3), 1000)
    linea, = ax.plot([], [], color='#7a0010', linewidth=1.75)

    def init():
        linea.set_data([], [])
        return linea,

    def animate(a):
        y = np.cbrt(x**2) + 0.9 * np.sqrt(3.3 - x**2) * np.sin(a * np.pi * x)
        linea.set_data(x, y)
        return linea,

    frames = np.linspace(1, 30, 100)
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=30, blit=True)
    
    # Salviamo in formato mp4 usando il writer 'ffmpeg' se disponibile, altrimenti fallback su html5 video string
    buf = io.BytesIO()
    try:
        anim.save(buf, writer='ffmpeg', fps=30, format='mp4')
        video_encoded = base64.b64encode(buf.getvalue()).decode('utf-8')
        video_tag = f'<video width="100%" autoplay loop muted playsinline><source src="data:video/mp4;base64,{video_encoded}" type="video/mp4"></video>'
    except Exception:
        # Se ffmpeg non è installato nel cloud, usiamo il codec HTML5 nativo generato da matplotlib
        video_tag = anim.to_html5_video()
        
    plt.close(fig)
    return video_tag

# Mostriamo il video animato in modo pulito e centrato
video_html = genera_video_cuore()

st.markdown(f"""
<div style="display: flex; justify-content: center; align-items: center;">
    <div style="width: 450px;">
        {video_html}
    </div>
</div>
""", unsafe_allow_html=True)

# Formula matematica statica e fissa posizionata esattamente sotto l'animazione
st.markdown(r"""
<div class="formula-paragrafo">

$$ \text{Regalo} = dx, \quad \int_{\text{te}}^{\text{me}} \text{Amore} \, dx = +\infty $$

</div>
""", unsafe_allow_html=True)