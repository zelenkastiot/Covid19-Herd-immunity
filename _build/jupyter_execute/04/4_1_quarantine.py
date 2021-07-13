# Воведување на карантин
***
Во ова поглавје ќе имплементираме минимална промена: да речеме дека повторно го користиме [SEIRD](https://zelenkastiot.github.io/COVID-19_book/03_beyondSIR/subsection/3_2.html) моделот, на кој дополнуваме ден $L$ ден; ден од кој се воведува строг **карантин**, во кој $R_0$ се редуцира од почетната вредност на помала. 

Во овие пресметки го користиме $\beta$ за согледување на промената наместо $R_0$, но знаеме дека $R_0 = \frac{\beta}{\gamma}$, од која следува дека 
\begin{align*}
\beta &= R_0 \cdot \gamma
\end{align*}


Еве неколку графикони со различни вредности за $L$ со почетни вредности: 

- $R_0 = 5\rightarrow$ се почнува со почетно $R_0$ да е 5 меѓутоа при промена на вредноста за карантинот ($L$) се менува вредноста од 5 на 1 после $L-$иот ден
- $N = 1  000  000 \rightarrow$ 1 милион вкупна популација
- $D = 4 \rightarrow$  една заразена личност може 4 денови да ја чува во себе заразата и истата да ја шири 
- $\gamma = \frac{1}{D} = \frac{1}{4} \rightarrow$  четвртина од заразени личности заздравуваат на ден
- $\delta = \frac{1}{5} \rightarrow$  инкубациски период од 5 дена 
- $\alpha = 0.2 \rightarrow$ 20% смрттна стапка (лошо за модел бидејќи се разликува за возрасти, повеќе за ова подоцна) 
- $\rho = \frac{1}{9} \rightarrow$ 9 денови од заразата до смрт
- $S(0)=N-1, E(0)=1, I(0)=0, R(0)=0, D(0)=0 \rightarrow$  една личност изложена на заразата на 0 ден

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


def deriv(y, t, N, beta, gamma, delta, alpha, rho):
    S, E, I, R, D = y
    dSdt = -beta(t) * S * I / N
    dEdt = beta(t) * S * I / N - delta * E
    dIdt = delta * E - (1 - alpha) * gamma * I - alpha * rho * I
    dRdt = (1 - alpha) * gamma * I
    dDdt = alpha * rho * I
    return dSdt, dEdt, dIdt, dRdt, dDdt

data = []
for i in range(40, 80, 1):
    L = i
    N = 1_000_000
    D = 4.0 # infections lasts four days
    gamma = 1.0 / D
    delta = 1.0 / 5.0  # incubation period of five days

    def R_0(t):
        return 5.0 if t < L else 1.0
    def beta(t):
        return R_0(t) * gamma

    alpha = 0.2  # 20% death rate
    rho = 1/9  # 9 days from infection until death
    S0, E0, I0, R0, D0 = N-1, 1, 0, 0, 0  # initial conditions: one exposed

    t = np.linspace(0, 99, 100) # Grid of time points (in days)
    y0 = S0, E0, I0, R0, D0 # Initial conditions vector

    # Integrate the SIR equations over the time grid, t.
    ret = odeint(deriv, y0, t, args=(N, beta, gamma, delta, alpha, rho))
    S, E, I, R, D = ret.T
    # Plot Model using plotly 
    figc = go.Figure()

    data_1 = go.Scatter(x = t, 
                              y = S, 
                              mode = 'lines',
                              visible = False,
                              line=dict(color="blue",
                                        width=2),
                              name = "Подлежни; <i>S(t)</i>",
                              hovertemplate = '<i> %{y:.0f} </i> луѓе')


    data_2 = go.Scatter(x = t, 
                              y = E, 
                              mode = 'lines',
                              visible = False,
                              line=dict(color="#CCCC00",
                                        width=2),
                              name = "Изложени; <i>E(t)</i>",
                              hovertemplate = '<i> %{y:.0f} </i> луѓе')


    data_3 = go.Scatter(x = t, 
                              y = I,
                              mode = 'lines',
                              visible = False, 
                              line=dict(color="red",
                                        width=2),
                              name = "Заразени; <i>I(t)</i>",
                              hovertemplate = '<i> %{y:.0f} </i> луѓе')


    data_4 = go.Scatter(x = t,
                              y = R, 
                              mode = 'lines',
                              visible = False,
                              line=dict(color="green",
                                        width=2),
                              name = "Оздравени; <i>R(t)</i>",
                              hovertemplate = '<i> %{y:.0f} </i> луѓе')


    data_5 = go.Scatter(x = t,
                              y =  D, 
                              visible = False, 
                              mode = 'lines',
                              line=dict(color="#696969",
                                        width=2),
                              name = "Починати; <i>D(t)</i>",
                              hovertemplate = '<i> %{y:.0f} </i> луѓе')


    data_6 = go.Scatter(x = t, 
                              y =  list(S+E+I+R+D), 
                              mode = 'lines',
                              visible = False, 
                              line=dict(color="#ade6e6",
                                        width=2,
                                        dash="dash"),
                              name = "Вкупно",
                              hovertemplate = '<i> %{y:.0f} </i> луѓе')
    data.append(data_1)
    data.append(data_2)
    data.append(data_3)
    data.append(data_4)
    data.append(data_5)
    data.append(data_6)


# Toggle frist slice to be visible
data[0]['visible'] = True
data[1]['visible'] = True
data[2]['visible'] = True
data[3]['visible'] = True
data[4]['visible'] = True
data[5]['visible'] = True

# Create steps and slider
steps = []
for i in range(0, 40, 1):
    step = dict(
        method = 'restyle',  
        args = ['visible', [False]*240],
        label = str(i+40))
    for j in range(0,6):
        step['args'][1][i*6+j] = True # Toggle i, i+1, i+2 trace to "visible"
    
    steps.append(step)

sliders = [dict(
    active = 0,
    currentvalue = {'prefix':
                    "<i>L</i> = <b>",
                    'suffix':
                    " денови"},
    pad = {"t": 80, "b": 10},
    steps = steps
)]

# Setup the layout of the figure
layout = go.Layout(title = "Карантин после <i>L</i> денови",
                  title_x = 0.5, 
                  xaxis_title='<i>Време (t)</i>',
                  xaxis=dict(range=[0,100], 
                             mirror=False,
                             ticks='outside',
                             showline=True,
                             tickvals = [0, 20, 40, 60, 80, 100],
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  yaxis_title='Број на луѓе',
                  yaxis=dict(range=[0,1100000], 
                             mirror=False,
                             ticks='outside', 
                             showline=True,
                             showspikes = True,
                             linecolor='#000',
                             tickvals = [0, 200000, 400000, 600000, 800000, 1000000], 
                             tickfont = dict(size=11)),
                  plot_bgcolor='#fff', 
                  hovermode = 'x unified',
                  width = 700, 
                  height = 350,
                  sliders = sliders,
                  font = dict(size = 10),
                  margin=go.layout.Margin(l=50,
                                         r=50,
                                         b=60,
                                         t=35))

# Plot function saves as html or with ipplot
fig4 = dict(data=data, layout=layout)
plot(fig4, filename = 'fig4.html', config = config)
display(HTML('fig4.html'))

Од графикот може да се заклучи дека неколку денови прават енормна разлика во ширењето на заразата доколку мерките се спроведат на време! 

Меѓутоа и ова програмирање на $R_0$, да скока од една вредност на друга (да скока од 5 на 1 во денот кога е спроведен карантинот) е повоторнод далеку од реално сценарио.  