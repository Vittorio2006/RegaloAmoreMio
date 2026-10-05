import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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

# Inizializziamo i fotogrammi dell'animazione nello stato di Streamlit
if 'frame_index' not in st.session_state:
    st.session_state.frame_index = 0

# Lista dei valori di 'a' che determinano l'animazione del cuore
valori_a = np.linspace(1, 30, 100)

# Contenitori per grafico e formula
plot_placeholder = st.empty()

# Preparazione del grafico
fig, ax = plt.subplots(figsize=(6, 5))
fig.patch.set_alpha(0.0) 
ax.patch.set_alpha(0.0)  
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.5, 3.5)
ax.axis('off')  

x = np.linspace(-np.sqrt(3.3), np.sqrt(3.3), 1000)
linea, = ax.plot([], [], color='#7a0010', linewidth=1.75)

# Disegniamo il fotogramma corrente basato sullo stato
idx = st.session_state.frame_index
a = valori_a[idx]
y = np.cbrt(x**2) + 0.9 * np.sqrt(3.3 - x**2) * np.sin(a * np.pi * x)
linea.set_data(x, y)

with plot_placeholder:
    st.pyplot(fig)

plt.close(fig)

# Formula matematica sotto al grafico
st.markdown(r"""
<div class="formula-paragrafo">

$$ \text{Regalo} = dx, \quad \int_{\text{te}}^{\text{me}} \text{Amore} \, dx = +\infty $$

</div>
""", unsafe_allow_html=True)

# Se l'animazione non è ancora finita, avanziamo al fotogramma successivo e ricarichiamo la pagina
if st.session_state.frame_index < len(valori_a) - 1:
    st.session_state.frame_index += 1
    # Piccola pausa tra un fotogramma e l'altro per regolare la velocità dell'animazione
    import time
    time.sleep(0.03)
    st.rerun()