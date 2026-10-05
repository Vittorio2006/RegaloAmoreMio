import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Impostazioni della pagina
st.set_page_config(page_title="Proposta", layout="centered")

# CSS per un'estetica minimale, seria e formale (con font della formula ridotto)
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
        margin-bottom: 30px;
        line-height: 1.3;
    }
    
    .formula-paragrafo {
        text-align: center;
        margin-top: 10px;
        padding: 15px;
        font-family: 'Montserrat', sans-serif;
        font-size: 16px; /* Font ridotto */
        color: #2b2b2b;
    }
    </style>
    """, unsafe_allow_html=True)

# Titolo formale, grande e in grassetto
st.markdown("<div class='titolo-serio'>Un piccolo regalo per il mio infinito amore verso di te</div>", unsafe_allow_html=True)

# Preparazione della figura e degli assi
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

# Creazione dell'animazione gestita direttamente via JavaScript nel browser
anim = FuncAnimation(fig, animate, init_func=init, frames=np.linspace(1, 30, 160), interval=25, blit=True)

# Mostra l'animazione fluida direttamente nel browser tramite componente HTML di Streamlit
st.components.v1.html(anim.to_jshtml(), height=480)
plt.close(fig)

# Formula matematica sotto al grafico con font ridotto
st.markdown(r"""
<div class="formula-paragrafo">

$$ \text{Regalo} = dx, \quad \int_{\text{te}}^{\text{me}} \text{Amore} \, dx = +\infty $$

</div>
""", unsafe_allow_html=True)