import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

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
        font-size: 16px; /* Font ridotto come richiesto */
        color: #2b2b2b;
    }
    </style>
    """, unsafe_allow_html=True)

# Titolo formale, grande e in grassetto
st.markdown("<div class='titolo-serio'>Un piccolo regalo per il mio infinito amore verso di te</div>", unsafe_allow_html=True)

# Contenitori per grafico e formula
plot_placeholder = st.empty()
text_placeholder = st.empty()

# Formula matematica sotto al grafico
with text_placeholder:
    st.markdown(r"""
<div class="formula-paragrafo">

$$ \text{Regalo} = dx, \quad \int_{\text{te}}^{\text{me}} \text{Amore} \, dx = +\infty $$

</div>
""", unsafe_allow_html=True)

# Preparazione del grafico
fig, ax = plt.subplots(figsize=(6, 5))
fig.patch.set_alpha(0.0) 
ax.patch.set_alpha(0.0)  
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.5, 3.5)
ax.axis('off')  

linea, = ax.plot([], [], color='#7a0010', linewidth=1.75)
x = np.linspace(-np.sqrt(3.3), np.sqrt(3.3), 1000)

# Esecuzione dell'animazione frame per frame nel placeholder
for a in np.linspace(1, 30, 160):
    y = np.cbrt(x**2) + 0.9 * np.sqrt(3.3 - x**2) * np.sin(a * np.pi * x)
    linea.set_data(x, y)
    
    with plot_placeholder:
        st.pyplot(fig)
        
    time.sleep(0.02)

plt.close(fig)