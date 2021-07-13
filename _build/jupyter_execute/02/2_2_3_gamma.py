# Интерактивен график параметар $\gamma$
***
$\gamma$**:**  бројот на заразени личности што заздравуваат на ден

# Python3 imports 
from scipy.integrate import odeint
import numpy as np
import math
import plotly.graph_objects as go
import plotly.tools as tls
from plotly.offline import plot, iplot, init_notebook_mode
from IPython.core.display import display, HTML
init_notebook_mode(connected = True)
config={'showLink': False, 'displayModeBar': False}
 

# Function for calculating diff equations
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


# Create list of Scatter plots
data = []
for i in range(1, 51, 1):
    N = 1000 
    beta = 1.0
    D = i 
    gamma = 1.0 / D
    # initial conditions: one infected, rest susceptible
    S0, I0, R0 = 999, 1, 0  
    # t: time points from begining of desiase 
    t = np.linspace(0, 49, 50) 
    # Initial conditions vector
    y0 = S0, I0, R0 
    # Integrate the SIR equations over the time grid, t.
    ret = odeint(deriv, y0, t, args=(N, beta, gamma))
    S, I, R = ret.T
    # Plot Model using plotly 
    
    data_1 = go.Scatter(x = t, 
                        y = S, 
                        mode = 'lines',
                        visible = False,
                        line = dict(color="blue", 
                                  width=2),
                        name = "Подлежни; <i>S(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')
    
    data_2 = go.Scatter(x = t, 
                        y = I, 
                        mode = 'lines',
                        visible = False,
                        line = dict(color="red",
                                  width=2),
                        name = "Заразени; <i>I(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')
    
    data_3 = go.Scatter(x = t, 
                        y = R, 
                        mode = 'lines',
                        visible = False,
                        line = dict(color="green",
                                    width=2),
                        name = "Излекувани; <i>R(t)</i>",
                        hovertemplate = '<i> %{y: .0f} </i> луѓе')
    data.append(data_1)
    data.append(data_2)
    data.append(data_3)


# Toggle frist slice to be visible
data[3]['visible'] = True
data[4]['visible'] = True
data[5]['visible'] = True

# Create steps and slider
steps = []
for i in range(0, 50, 1):
    step = dict(
        method = 'restyle',  
        args = ['visible', [False]*150],
        label = str(i+1))
    for j in range(0,3):
        step['args'][1][i*3+j] = True # Toggle i, i+1, i+2 trace to "visible"
    
    steps.append(step)

sliders = [dict(
    active = 1,
    currentvalue = {'prefix':
                    "Бројот на заразени личности што заздравуваат на ден  &#x2192; &#120574; = <b>1</b>/<b>"},
    pad = {"t": 90, "b": 10},
    steps = steps
)]

# Setup the layout of the figure
layout = go.Layout(title = 'SIR модел (1000 луѓе); \t  &#120574; = 1/<i>D</i>',
                  title_x = 0.5, 
                  xaxis_title='<i>t</i>',
                  xaxis=dict(range=[0,50], 
                             mirror=False,
                             ticks='outside',
                             tickvals = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                             showline=True,
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  yaxis_title='Број на луѓе',
                  yaxis=dict(range=[0,1000], 
                             mirror=False,
                             ticks='outside', 
                             showline=True, 
                             showspikes = True, 
                             linecolor='#000',
                             tickvals = list(range(0, 1001, 100)), 
                             tickfont = dict(size=11)),
                  hovermode = "x unified",
                  plot_bgcolor='#fff', 
                  width = 640, 
                  height = 400,
                  sliders = sliders,
                  font = dict(size = 10),
                  margin=go.layout.Margin(l=50,
                                         r=50,
                                         b=60,
                                         t=35))

# Plot function saves as html or with ipplot
fig1_1_b = dict(data=data, layout=layout)
plot(fig1_1_b, filename = 'fig1_1_b.html', config = config)
display(HTML('fig1_1_b.html'))