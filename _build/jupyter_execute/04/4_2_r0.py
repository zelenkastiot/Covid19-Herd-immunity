# Временски зависно $R_0$
*** 
Во реалноста, $R_0$ веројатно никогаш не "скока" од една вредност на друга. Меѓутоа, повеќе или помалку постојано се менува (со можност да варира нагоре надоле со вредноста повеќе пати, на пр. ако мерките за социјално дистанцирање се олабавуваат или зајакнуваат). Може да се избере било која функција за $R_0$, ние избравме модел кој често за користи за презентирање на влијанието од социјални дистанцирање: **logistic function**

Формулата која ние ја користиме изгледа вака: 


\begin{align*}
R_0(t) &= \frac{R_{0_{start}}-R_{0_{end}}}{1+e^{-k\cdot (-x+x_0)}} + R_{0_{end}}
\end{align*}

Параметрите се: 

- $R_{0_{start}}$ и $R_{0_{end}}$ се вредностите за $R_0$ за првиот и последниот ден 

- $x_0$ е вредноста на x-оска за која $R_0$ има најстрмниот пад (**inflection point**, може да биде "главниот" ден кога е воведен карантин) 

- $k$ контролира колку брзо паѓа $R_0$


График со различни вредности за $k$: 

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

N = 1_000_000
D = 4.0 # infections lasts four days
gamma = 1.0 / D
delta = 1.0 / 5.0  # incubation period of five days

R_0_start, k, x0, R_0_end = 2.0, 0.5, 50, 0.5

def logistic_R_0(t, k):
    return (R_0_start-R_0_end) / (1 + np.exp(-k*(-t+x0))) + R_0_end

def beta(t):
    return logistic_R_0(t) * gamma

alpha = 0.2  # 20% death rate
rho = 1/9  # 9 days from infection until death
S0, E0, I0, R0, D0 = N-1, 1, 0, 0, 0  # initial conditions: one exposed

t = np.linspace(0, 99, 100) # Grid of time points (in days)

R_list = []
R_range = [.05, .09, 0.5, 1.5]
for k in R_range:
    R0 = [logistic_R_0(i, k) for i in range(len(t))]  # to plot R_0 over time: get function values
    R_list.append(R0)

data_0 = [dict(visible = True,
                x = t,
                y = R_list[0],
                name = 'R<sub>0</sub>, k = '+str(R_range[0]),
                hoverinfo = "all",
                line=dict(width=2),
                showlegend = True,
                hovertemplate = "%{y: .3f}"
           )]

data_1 = [dict(visible = True,
                x = t,
                y = R_list[1],
                name = 'R<sub>0</sub>, k = '+str(R_range[1]),
                hoverinfo = "all",
                line=dict(width=2),
                showlegend = True,
                hovertemplate = "%{y: .3f}"
           )]

data_2 = [dict(visible = True,
                x = t,
                y = R_list[2],
                name = 'R<sub>0</sub>, k = '+str(R_range[2]),
                hoverinfo = "all",
                line=dict(width=2),
                showlegend = True,
                hovertemplate = "%{y: .3f}"
           )]

data_3 = [dict(visible = True,
                x = t,
                y = R_list[3],
                name = 'R<sub>0</sub>, k = '+str(R_range[3]),
                hoverinfo = "all",
                line=dict(width=2),
                showlegend = True,
                hovertemplate = "%{y: .3f}"
           )]

data = data_0 + data_1 + data_2 + data_3

# Setup the layout of the figure
layout = go.Layout(title = "Logistic R<sub>0</sub>; Почетно R<sub>0</sub>=2, различни k",
                  title_x = 0.5, 
                  xaxis_title='t',
                  xaxis=dict(range = [0,100],
                            tickvals = [0, 20, 40, 60, 80, 100],
                            linecolor='#000',
                            mirror = True,
                            side='bottom',
                            ticks='inside',
                            showline=True),
                  yaxis_title='R<sub>0</sub>',
                  yaxis=dict(autorange=False,
                            range=[.5, 2],
                            tickvals = [.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2],
                            linecolor='#000',
                            mirror = True,
                            ticks='inside',
                            showline=True),
                  plot_bgcolor='#fff', 
                  hovermode = 'x',
                  width = 700, 
                  height = 350,
                  font = dict(size = 10),
                  margin=go.layout.Margin(l=50,
                                         r=50,
                                         b=60,
                                         t=35))

# Plot function saves as html or with ipplot
fig5 = dict(data=data, layout=layout)
plot(fig5, filename = 'fig4.html', config = config)
display(HTML('fig4.html'))

Може да се заклучи од графикот дека независно од почетната вредност на $R_0$, вредноста на $k$ доколку е поголема тогаш $R_0$ побрзо опаѓа. Во случајот каде <b style='color: rgb(99, 110, 250)'>k = 0.05</b> вредноста на $R_0$ преку време поспоро опаѓа (ден 40: <i style='color: rgb(99, 110, 250)'>1.43</i>, ден 60: <i style='color: rgb(99, 110, 250)'>1.06</i>), доколку за најголемата вредност <b style='color: rgb(171, 99, 250)'>k = 1.5</b> опаѓа екстремно брзо (ден 40: <i style='color: rgb(171, 99, 250)'>2</i>, ден 60: <i style='color: rgb(171, 99, 250)'>0.5</i>).

Следниот график е пример за како се менува бројот на $S(t), I(t), R(t), D(t)$ доколку $R_0$ почнува од 5 и некаде на ден 50 опаѓа на 0.5: 

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

N = 1_000_000
D = 4.0 # infections lasts four days
gamma = 1.0 / D
delta = 1.0 / 5.0  # incubation period of five days

R_0_start, k, x0, R_0_end = 5.0, 0.5, 50, 0.5

def logistic_R_0(t):
    return (R_0_start-R_0_end) / (1 + np.exp(-k*(-t+x0))) + R_0_end

def beta(t):
    return logistic_R_0(t) * gamma

alpha = 0.2  # 20% death rate
rho = 1/9  # 9 days from infection until death
S0, E0, I0, R0, D0 = N-1, 1, 0, 0, 0  # initial conditions: one exposed


t = np.linspace(0, 99, 100) # Grid of time points (in days)
y0 = S0, E0, I0, R0, D0 # Initial conditions vector

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma, delta, alpha, rho))
S, E, I, R, D = ret.T
R0 = [logistic_R_0(i) for i in range(len(t))]  # to plot R_0 over time: get function values

data_com = []

data_1 = go.Scatter(x = t, 
                  y = S, 
                  mode = 'lines',
                  visible = True,
                  line=dict(color="blue",
                            width=2),
                  name = "Подлежни; <i>S(t)</i>",
                  hovertemplate = '<i> %{y:.0f} </i> луѓе')


data_2 = go.Scatter(x = t, 
                  y = E, 
                  mode = 'lines',
                  visible = True,
                  line=dict(color="#CCCC00",
                            width=2),
                  name = "Изложени; <i>E(t)</i>",
                  hovertemplate = '<i> %{y:.0f} </i> луѓе')


data_3 = go.Scatter(x = t, 
                  y = I,
                  mode = 'lines',
                  visible = True, 
                  line=dict(color="red",
                            width=2),
                  name = "Заразени; <i>I(t)</i>",
                  hovertemplate = '<i> %{y:.0f} </i> луѓе')


data_4 = go.Scatter(x = t,
                  y = R, 
                  mode = 'lines',
                  visible = True,
                  line=dict(color="green",
                            width=2),
                  name = "Оздравени; <i>R(t)</i>",
                  hovertemplate = '<i> %{y:.0f} </i> луѓе')


data_5 = go.Scatter(x = t,
                  y =  D, 
                  visible = True, 
                  mode = 'lines',
                  line=dict(color="#696969",
                            width=2),
                  name = "Починати; <i>D(t)</i>",
                  hovertemplate = '<i> %{y:.0f} </i> луѓе')


data_6 = go.Scatter(x = t, 
                  y =  list(S+E+I+R+D), 
                  mode = 'lines',
                  visible = True, 
                  line=dict(color="#ade6e6",
                            width=2,
                            dash="dash"),
                  name = "Вкупно",
                  hovertemplate = '<i> %{y:.0f} </i> луѓе')
data_com.append(data_1)
data_com.append(data_2)
data_com.append(data_3)
data_com.append(data_4)
data_com.append(data_5)
data_com.append(data_6)

data_R0 = [dict(visible = True,
                    x = t,
                    y = R0,
                    name = 'R<sub>0</sub>',
                    hoverinfo = "all",
                    hovertemplate = "%{y: .3f}",
                    line=dict(width=2,
                              dash="dash",
                              color = 'rgb(0, 204, 150)'),
                    xaxis='x2',
                    yaxis='y2',
                    showlegend = False
               )]

data = data_com + data_R0

# Setup the layout of the figure
layout = go.Layout(title = "SIERD; Почетно R<sub>0</sub>=5.0 со k=0.5",
                  title_x = 0.5, 
                  xaxis_title='t',
                  annotations=[dict(x=0.121,
                                    y=0.82,
                                    showarrow=False,
                                    text='R<sub>0</sub> преку време',
                                    font=dict(size=10),
                                    xref='paper',
                                    yref='paper'),
                               dict(x=0.195,
                                    y=0.14,
                                    showarrow=False,
                                    text='t',
                                    font=dict(size=10),
                                    xref='paper',
                                    yref='paper')
                            ],
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
                  xaxis2=dict(range = [0,100],
                              tickvals = [0, 20, 40, 60, 80, 100],
                              linecolor='#000',
                                domain=[0.05, 0.35],
                                anchor='y2',
                                mirror = True,
                                side='bottom',
                                ticks='',
                                showline=True),
                  yaxis2=dict(autorange=False,
                            range=[0, 5.5],
                            tickvals = [0, 1, 2, 3, 4, 5],
                            linecolor='#000',
                            domain=[0.25, 0.75],
                            anchor='x2',
                            mirror = True,
                            ticks='',
                            showline=True),
                  plot_bgcolor='#fff', 
                  hovermode = 'x unified',
                  width = 700, 
                  height = 350,
                  font = dict(size = 10),
                  margin=go.layout.Margin(l=50,
                                         r=50,
                                         b=60,
                                         t=35))

# Plot function saves as html or with ipplot
fig6 = dict(data=data, layout=layout)
plot(fig6, filename = 'fig6.html', config = config)
display(HTML('fig6.html'))