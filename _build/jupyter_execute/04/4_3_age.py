# Временски зависно $\alpha$
*** 
## Болнички ресурси 
Слично како $R_0$, стапката на смртност е доста нереалистично да се моделира како сценаријата до сега, бидејќи не е реално смртноста да е иста кај население кое е повозрасно и кај помлади тинејџери. Оваа стапка (параметар) зависи од повеќе работи меѓутоа во оваа тетратка се фокусираме на возраста на популацијата и на ресурсите. 


Прво, да го разгледаме параметарот како зависен од ресурси. Сакаме стапката да биде поголема кога повеќе луѓе се заразени (инфицирани). Појдуваме од точка, *како ова може да се формулира фо функција?* Ни треба оптимална (некоја средна) стапка на смртност за случајот каде само неколкумина се заразени (и во исто време тие да се стекнат со оптимално лекување) и некој фактор што го зима во предвид која порција од популацијата е моментално заразена. 

Ова е еден пример за таква функција која ги имплементира овие идеи: 

\begin{align*}
\alpha(t) &= f \cdot \frac{I(t)}{N} + \alpha_{base}
\end{align*}

<br>
Во формулата, $f$ е некој произволен фактор за скалирање кој е откако ќе го поставиме на почетокот од моделот, останува константен низ целото моделирање; $alpha_{base}$ е оптималната стапка на смртност. 

<br>
<br>

**Пример сценарио** <br> 
Доколку факторот $s=\frac{1}{2}=0.5$ и нека половина од популацијата е заразена на $t$ ден, тогаш $s\cdot \frac{I(t)}{N} = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}=25\%$, што посочува дека $\alpha(t)$ на тој ден е всушност $25 \% + \alpha_{base}$. Или можеби повеќето луѓе едвај имаат некакви симптоми и поради тоа големиот број на заразени не ги преполовува болниците. Сепак ова моделирање е попримитивно бидејќи не го зима во предвид бројот на кревети, респиратори и сл. Незаивсно, доколку го разгледаме  истото сценарио но со фактор од $s=0.1$, ратата ќе ни биде попристојна и $\alpha(t)$ би било само $5 \% + \alpha_{base}$. 



## Старост на население; SEIRD за различни популации
Да се моделира возраста на населението можеби беше еден од поголемите предвизици. За да се имплементира целосно би требало да има помали возрасни групи и повеќе на број што многу ни ги направи равенките тријвијални. Поедноставен пристап ни беше да го поделиме наслението во **4 групи** каде секоја група има соодведен дел (изразен во %) од вкупната популација и за секоја група да дефинираме стапка на смртност $\alpha$: 

- **1 Група:** *0-29*
- **2 Група:** *30-59*
- **3 Група:** *60-89*
- **4 Група:** *90+*

Пример би можеле да го поделиме населението на следниот начин: 

import plotly.graph_objects as go
import plotly.tools as tls
from plotly.offline import plot, iplot, init_notebook_mode
from IPython.core.display import display, HTML
from plotly.subplots import make_subplots

init_notebook_mode(connected = True)
config={'showLink': False, 'displayModeBar': False}


colors1 = ['lightslategray',] * 5
colors1[3] = '#0066CC'

colors2 = ['lightslategray',] * 5
colors2[2] = 'crimson'

alpha_by_agegroup = {"0-29": 0.01, "30-59": 0.05, "60-89": 0.2, "89+": 0.3}
proportion_of_agegroup = {"0-29": 10, "30-59": 30, "60-89": 40, "89+": 20}



fig = make_subplots(rows=1, 
                    cols=2,
                    horizontal_spacing = 0.15,
                    subplot_titles=("&#120572; по ворзасни групи","Распределба на население"))

fig.add_trace(
    go.Bar(
    x=["0-29", 
       "30-59", 
       "60-89",
       "89+"],
    y=[alpha_by_agegroup["0-29"],
       alpha_by_agegroup["30-59"],
       alpha_by_agegroup["60-89"],
       alpha_by_agegroup["89+"]],
    marker_color=colors1, 
    hovertemplate = '%{x} група, &#120572;: %{y} ',
    name = '',
    showlegend = False, 
    hoverlabel = dict(bgcolor='white', 
                      bordercolor='black')),
    row=1, col=1
)

fig.add_trace(
    go.Bar(
    x=["0-29", 
       "30-59", 
       "60-89",
       "89+"],
    y=[proportion_of_agegroup["0-29"],
       proportion_of_agegroup["30-59"],
       proportion_of_agegroup["60-89"],
       proportion_of_agegroup["89+"]],
    marker_color=colors2, 
    hovertemplate = '%{x} група, %{y} %',
    name = '',
    showlegend = False, 
    hoverlabel = dict(bgcolor='white', 
                      bordercolor='black')),
    row=1, col=2
)

fig.update_layout(title_text = "SIERD",
                  title_x = 0.5, 
                  xaxis_title = 'Возрасна група',
                  xaxis=dict(mirror=False,
                             showline=True,
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  yaxis_title = '&#120572;',
                  yaxis=dict(mirror=False,
                             showline=True,
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  xaxis2_title = 'Возрасна група',
                  xaxis2=dict(mirror=False,
                             showline=True,
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  yaxis2_title = '%',
                  yaxis2=dict(mirror=False,
                             showline=True,
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  plot_bgcolor='#fff', 
                  hovermode = 'closest',
                  width = 700, 
                  height = 350,
                  font = dict(size = 10),
                  margin=go.layout.Margin(l=50,
                                         r=50,
                                         b=60,
                                         t=55))

plot(fig, filename = 'fig9_1_alpha_age.html', config = config)
display(HTML('fig9_1_alpha_age.html'))

Оваа поделба резултира со доста повозрасно население со 60% од населението да е постаро од 60 години. Пример, доколку за ова население би ја пресметале просечната стапка на смртност би добиле: 

\begin{align*}
\alpha &= 0.01 \cdot 0.1 \cdot + 0.05 \cdot 0.3 + 0.2 \cdot 0.4 + \cdot 0.3\cdot 0.2 = 15.6 \% 
\end{align*}


Имајќи во предвид сите дополнителни параметри, не менуваме ништо во главните равенки. Го дефинираме само $\alpha$ внатре во равенките бидејќи ни е потребна моменталната вредност од $I(t)$ за ден $t$, фактор $s = 0.01$; 

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

def deriv(y, t, N, beta, gamma, delta, alpha_opt, rho):
    S, E, I, R, D = y
    def alpha(t):
        return s * I/N + alpha_opt

    dSdt = -beta(t) * S * I / N
    dEdt = beta(t) * S * I / N - delta * E
    dIdt = delta * E - (1 - alpha(t)) * gamma * I - alpha(t) * rho * I
    dRdt = (1 - alpha(t)) * gamma * I
    dDdt = alpha(t) * rho * I
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

alpha_by_agegroup = {"0-29": 0.01, "30-59": 0.05, "60-89": 0.2, "89+": 0.3}
proportion_of_agegroup = {"0-29": 0.1, "30-59": 0.3, "60-89": 0.4, "89+": 0.2}
s = 0.01
alpha_opt = sum(alpha_by_agegroup[i] * proportion_of_agegroup[i] for i in list(alpha_by_agegroup.keys()))

rho = 1/9  # 9 days from infection until death
S0, E0, I0, R0, D0 = N-1, 1, 0, 0, 0  # initial conditions: one exposed

t = np.linspace(0, 99, 100) # Grid of time points (in days)
y0 = S0, E0, I0, R0, D0 # Initial conditions vector

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma, delta, alpha_opt, rho))
S, E, I, R, D = ret.T
R0 = [logistic_R_0(i) for i in range(len(t))]  # to plot R_0 over time: get function values
Alpha = [s * I[i]/N + alpha_opt for i in range(len(t))]  # to plot alpha over time

colors1 = ['lightslategray',] * 5
colors1[3] = '#0066CC'

colors2 = ['lightslategray',] * 5
colors2[2] = 'crimson'

alpha_by_agegroup = {"0-29": 0.01, "30-59": 0.05, "60-89": 0.2, "89+": 0.3}
proportion_of_agegroup = {"0-29": 10, "30-59": 30, "60-89": 40, "89+": 20}

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

data_R0 = [dict(visible = False,
                    x = t,
                    y = R0,
                    name = 'R<sub>0</sub>',
                    hoverinfo = "all",
                    hovertemplate = "%{y: .3f}",
                    line=dict(width=1.5,
                              dash = 'dash',
                              color = 'rgb(0, 204, 150)'),
                    xaxis='x2',
                    yaxis='y2',
                    showlegend = False
               )]

data_alpha = [dict(visible = True,
                    x = t,
                    y = Alpha,
                    name = '&#120572;',
                    hoverinfo = "all",
                    hovertemplate = "%{y: .4f}",
                    line=dict(width=1.5,
                              dash = 'dash',
                              color = 'rgb(238,144,238)'),
                    xaxis='x2',
                    yaxis='y2',
                    showlegend = False,
               )]

data_bar_alpha = [go.Bar(
    x=["0-29", 
       "30-59", 
       "60-89",
       "89+"],
    y=[alpha_by_agegroup["0-29"],
       alpha_by_agegroup["30-59"],
       alpha_by_agegroup["60-89"],
       alpha_by_agegroup["89+"]],
    marker_color=colors1, 
    hovertemplate = '%{x} група, &#120572;: %{y} ',
    name = '',
    xaxis='x2',
    yaxis='y2',
    showlegend = False, 
    hoverlabel = dict(bgcolor='white', 
                      bordercolor='black'))]

data_bar_population = [go.Bar(
    x=["0-29", 
       "30-59", 
       "60-89",
       "89+"],
    y=[proportion_of_agegroup["0-29"],
       proportion_of_agegroup["30-59"],
       proportion_of_agegroup["60-89"],
       proportion_of_agegroup["89+"]],
    marker_color=colors2, 
    hovertemplate = '%{x} група, %{y} %',
    name = '',
    xaxis='x2',
    yaxis='y2',
    showlegend = False, 
    visible = False,
    hoverlabel = dict(bgcolor='white', 
                      bordercolor='black'))]

    
data = data_com + data_alpha + data_R0  + data_bar_alpha + data_bar_population

# Setup the layout of the figure
layout = go.Layout(
    updatemenus=[
        dict(
            active = 0, 
            x=0.2,
            y=1.09,
            yanchor="top",
            buttons=list([
                dict(label="(1) &#120572; преку време",
                             method="update",
                             args=[{"visible": [True, True, True, True, True, True, True, False, False, False]},
                                   {'annotations':[
                                               dict(text="Прикажи: ", 
                                                     showarrow=False,
                                                     x=0.25, 
                                                     y=1.15, 
                                                     yref="paper", 
                                                     align="left"),
                                               dict(x=0.15,
                                                    y=0.82,
                                                    showarrow=False,
                                                    text='&#120572; преку време',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                               dict(x=0.228,
                                                    y=0.13,
                                                    showarrow=False,
                                                    text='t',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper')],
                                    'xaxis2': dict(range = [0,100],
                                                   tickvals = [0, 20, 40, 60, 80, 100],
                                                   linecolor='#000',
                                                   domain=[0.09, 0.38],
                                                   anchor='y2',
                                                   mirror = True,
                                                   side='bottom',
                                                   ticks='',
                                                   showline=True),
                                  'yaxis2': dict(autorange=False,
                                                 range=[0.1558, 0.1578],
                                                 tickvals = [0.1560, 0.1562, 0.1564, 0.1566, 0.1568, 0.1570, 0.1572, 0.1574, 0.1576],
                                                 linecolor='#000',
                                                 domain=[0.25, 0.75],
                                                 anchor='x2',
                                                 mirror = True,
                                                 ticks='',
                                                 showline=True)}]),
                
                dict(label="(2) R<sub>0</sub> преку време",
                             method="update",
                             args=[{"visible": [True, True, True, True, True, True, False, True, False, False]},
                                   {'annotations': [
                                               dict(text="Прикажи: ", 
                                                     showarrow=False,
                                                     x=0.25, 
                                                     y=1.15, 
                                                     yref="paper", 
                                                     align="left"),
                                               dict(x=0.15,
                                                    y=0.82,
                                                    showarrow=False,
                                                    text='R<sub>0</sub> преку време',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                                dict(x=0.228,
                                                    y=0.13,
                                                    showarrow=False,
                                                    text='t',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                                dict(x=0.01,
                                                    y=0.5,
                                                    showarrow=False,
                                                    textangle = -90,
                                                    text='R<sub>0</sub>',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper')   ],
                                    'xaxis2': dict(range = [0,100],
                                                   tickvals = [0, 20, 40, 60, 80, 100],
                                                   linecolor='#000',
                                                   domain=[0.08, 0.38],
                                                   anchor='y2',
                                                   mirror = True,
                                                   side='bottom',
                                                   ticks='',
                                                   showline=True),
                                   'yaxis2': dict(autorange=False,
                                                  range=[0, 5.5],
                                                  tickvals = [0, 1, 2, 3, 4, 5],
                                                  linecolor='#000',
                                                  domain=[0.25, 0.75],
                                                  anchor='x2',
                                                  mirror = True,
                                                  ticks='',
                                                  showline=True)}
                                  ]) ,
                
                dict(label="(3) &#120572; по група",
                             method="update",
                             args=[{"visible": [True, True, True, True, True, True, False, False, True, False]},
                                   {'annotations': [
                                               dict(text="Прикажи: ", 
                                                     showarrow=False,
                                                     x=0.25, 
                                                     y=1.15, 
                                                     yref="paper", 
                                                     align="left"),
                                               dict(x=0.172,
                                                    y=0.82,
                                                    showarrow=False,
                                                    text='&#120572; по група',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                               dict(x=0.128,
                                                    y=0.133,
                                                    showarrow=False,
                                                    text='Возрасна група',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                               dict(x=0.01,
                                                    y=0.5,
                                                    showarrow=False,
                                                    textangle = -90,
                                                    text='&#120572;',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper')],
                                    'xaxis2': dict(autorange = True,
                                                   linecolor='#000',
                                                   domain=[0.08, 0.38],
                                                   anchor='y2',
                                                   mirror = True,
                                                   side='bottom',
                                                   ticks='',
                                                   showline=True,
                                                   tickfont = dict(size=9)),
                                   'yaxis2': dict(autorange = True,
                                                  linecolor='#000',
                                                  domain=[0.25, 0.75],
                                                  anchor='x2',
                                                  mirror = True,
                                                  ticks='',
                                                  showline=True)}
                                  ]) , 
                dict(label="(4) Популација",
                             method="update",
                             args=[{"visible": [True, True, True, True, True, True, False, False, False, True]},
                                   {'annotations': [
                                               dict(text="Прикажи: ", 
                                                     showarrow=False,
                                                     x=0.25, 
                                                     y=1.15, 
                                                     yref="paper", 
                                                     align="left"),
                                               dict(x=0.077,
                                                    y=0.82,
                                                    showarrow=False,
                                                    text='Распределба на популација',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                               dict(x=0.13,
                                                    y=0.133,
                                                    showarrow=False,
                                                    text='Возрасна група',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                               dict(x=0.01,
                                                    y=0.5,
                                                    showarrow=False,
                                                    textangle = -90,
                                                    text='%',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper')],
                                    'xaxis2': dict(autorange = True,
                                                   linecolor='#000',
                                                   domain=[0.08, 0.38],
                                                   anchor='y2',
                                                   mirror = True,
                                                   side='bottom',
                                                   ticks='',
                                                   showline=True,
                                                  tickfont = dict(size=9)),
                                   'yaxis2': dict(autorange = True,
                                                  linecolor='#000',
                                                  domain=[0.25, 0.75],
                                                  anchor='x2',
                                                  mirror = True,
                                                  ticks='',
                                                  showline=True)}
                                  ]) 
                ]),
            direction="down"
            )],
                  title = "SIERD; Повозрасно население",
                  title_x = 0.5, 
                  xaxis_title='t',
                  annotations=[
                              dict(text="Прикажи: ", 
                                         showarrow=False,
                                         x=0.25, 
                                         y=1.15, 
                                         yref="paper", 
                                         align="left"),
                              dict(x=0.15,
                                    y=0.82,
                                    showarrow=False,
                                    text='&#120572; преку време',
                                    font=dict(size=10),
                                    xref='paper',
                                    yref='paper'),
                               dict(x=0.228,
                                    y=0.13,
                                    showarrow=False,
                                    text='t',
                                    font=dict(size=10),
                                    xref='paper',
                                    yref='paper')],
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
                                domain=[0.09, 0.38],
                                anchor='y2',
                                mirror = True,
                                side='bottom',
                                ticks='',
                                showline=True),
                  yaxis2=dict(autorange=False,
                            range=[0.1558, 0.1578],
                            tickvals = [0.1560, 0.1562, 0.1564, 0.1566, 0.1568, 0.1570, 0.1572, 0.1574, 0.1576],
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
fig9_2 = dict(data=data, layout=layout)
plot(fig9_2, filename = 'fig9_old.html', config = config)
display(HTML('fig9_old.html'))

Пример друг, доколку би имале помладо население: 

import plotly.graph_objects as go
import plotly.tools as tls
from plotly.offline import plot, iplot, init_notebook_mode
from IPython.core.display import display, HTML
from plotly.subplots import make_subplots

init_notebook_mode(connected = True)
config={'showLink': False, 'displayModeBar': False}


colors1 = ['lightslategray',] * 5
colors1[3] = '#0066CC'

colors2 = ['lightslategray',] * 5
colors2[0] = 'crimson'

alpha_by_agegroup = {"0-29": 0.01, "30-59": 0.05, "60-89": 0.2, "89+": 0.3}
proportion_of_agegroup = {"0-29": 50, "30-59": 30, "60-89": 10, "89+": 10}



fig = make_subplots(rows=1, 
                    cols=2,
                    horizontal_spacing = 0.15,
                    subplot_titles=("&#120572; по ворзасни групи","Распределба на население"))

fig.add_trace(
    go.Bar(
    x=["0-29", 
       "30-59", 
       "60-89",
       "89+"],
    y=[alpha_by_agegroup["0-29"],
       alpha_by_agegroup["30-59"],
       alpha_by_agegroup["60-89"],
       alpha_by_agegroup["89+"]],
    marker_color=colors1, 
    hovertemplate = '%{x} група, &#120572;: %{y} ',
    name = '',
    showlegend = False, 
    hoverlabel = dict(bgcolor='white', 
                      bordercolor='black')),
    row=1, col=1
)

fig.add_trace(
    go.Bar(
    x=["0-29", 
       "30-59", 
       "60-89",
       "89+"],
    y=[proportion_of_agegroup["0-29"],
       proportion_of_agegroup["30-59"],
       proportion_of_agegroup["60-89"],
       proportion_of_agegroup["89+"]],
    marker_color=colors2, 
    hovertemplate = '%{x} група, %{y} %',
    name = '',
    showlegend = False, 
    hoverlabel = dict(bgcolor='white', 
                      bordercolor='black')),
    row=1, col=2
)

fig.update_layout(title_text = "SIERD",
                  title_x = 0.5, 
                  xaxis_title = 'Возрасна група',
                  xaxis=dict(mirror=False,
                             showline=True,
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  yaxis_title = '&#120572;',
                  yaxis=dict(mirror=False,
                             showline=True,
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  xaxis2_title = 'Возрасна група',
                  xaxis2=dict(mirror=False,
                             showline=True,
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  yaxis2_title = '%',
                  yaxis2=dict(mirror=False,
                             showline=True,
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  plot_bgcolor='#fff', 
                  hovermode = 'closest',
                  width = 700, 
                  height = 350,
                  font = dict(size = 10),
                  margin=go.layout.Margin(l=50,
                                         r=50,
                                         b=60,
                                         t=55))

plot(fig, filename = 'fig9_2alpha_age.html', config = config)
display(HTML('fig9_2alpha_age.html'))

Со ваква поделба би имале стапка на смрност $\alpha<10\%$! 

За да ги искористиме овие поделби и доделување на вредности, можеме да го користиме истиот модел дефиниран погоре, за болнички ресурси со тоа што ќе го пресметување $\alpha_{base}$ имајќи ги овие вредности. 

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

def deriv(y, t, N, beta, gamma, delta, alpha_opt, rho):
    S, E, I, R, D = y
    def alpha(t):
        return s * I/N + alpha_opt

    dSdt = -beta(t) * S * I / N
    dEdt = beta(t) * S * I / N - delta * E
    dIdt = delta * E - (1 - alpha(t)) * gamma * I - alpha(t) * rho * I
    dRdt = (1 - alpha(t)) * gamma * I
    dDdt = alpha(t) * rho * I
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

alpha_by_agegroup = {"0-29": 0.01, "30-59": 0.05, "60-89": 0.2, "89+": 0.3}
proportion_of_agegroup = {"0-29": 0.4, "30-59": 0.3, "60-89": 0.2, "89+": 0.1}
s = 0.01
alpha_opt = sum(alpha_by_agegroup[i] * proportion_of_agegroup[i] for i in list(alpha_by_agegroup.keys()))

rho = 1/9  # 9 days from infection until death
S0, E0, I0, R0, D0 = N-1, 1, 0, 0, 0  # initial conditions: one exposed

t = np.linspace(0, 99, 100) # Grid of time points (in days)
y0 = S0, E0, I0, R0, D0 # Initial conditions vector

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma, delta, alpha_opt, rho))
S, E, I, R, D = ret.T
R0 = [logistic_R_0(i) for i in range(len(t))]  # to plot R_0 over time: get function values
Alpha = [s * I[i]/N + alpha_opt for i in range(len(t))]  # to plot alpha over time

colors1 = ['lightslategray',] * 5
colors1[3] = '#0066CC'

colors2 = ['lightslategray',] * 5
colors2[0] = 'crimson'

alpha_by_agegroup = {"0-29": 0.01, "30-59": 0.05, "60-89": 0.2, "89+": 0.3}
proportion_of_agegroup = {"0-29": 40, "30-59": 30, "60-89": 20, "89+": 10}

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

data_R0 = [dict(visible = False,
                    x = t,
                    y = R0,
                    name = 'R<sub>0</sub>',
                    hoverinfo = "all",
                    hovertemplate = "%{y: .3f}",
                    line=dict(width = 1.5,
                              dash = 'dash',
                              color = 'rgb(0, 204, 150)'),
                    xaxis='x2',
                    yaxis='y2',
                    showlegend = False
               )]

data_alpha = [dict(visible = True,
                    x = t,
                    y = Alpha,
                    name = '&#120572;',
                    hoverinfo = "all",
                    hovertemplate = "%{y: .4f}",
                    line=dict(width=1.5,
                              dash = 'dash',
                              color = 'rgb(238,144,238)'),
                    xaxis='x2',
                    yaxis='y2',
                    showlegend = False,
               )]

data_bar_alpha = [go.Bar(
    x=["0-29", 
       "30-59", 
       "60-89",
       "89+"],
    y=[alpha_by_agegroup["0-29"],
       alpha_by_agegroup["30-59"],
       alpha_by_agegroup["60-89"],
       alpha_by_agegroup["89+"]],
    marker_color=colors1, 
    hovertemplate = '%{x} група, &#120572;: %{y} ',
    name = '',
    xaxis='x2',
    yaxis='y2',
    showlegend = False, 
    hoverlabel = dict(bgcolor='white', 
                      bordercolor='black'))]

data_bar_population = [go.Bar(
    x=["0-29", 
       "30-59", 
       "60-89",
       "89+"],
    y=[proportion_of_agegroup["0-29"],
       proportion_of_agegroup["30-59"],
       proportion_of_agegroup["60-89"],
       proportion_of_agegroup["89+"]],
    marker_color=colors2, 
    hovertemplate = '%{x} група, %{y} %',
    name = '',
    xaxis='x2',
    yaxis='y2',
    showlegend = False, 
    visible = False,
    hoverlabel = dict(bgcolor='white', 
                      bordercolor='black'))]

    
data = data_com + data_alpha + data_R0  + data_bar_alpha + data_bar_population

# Setup the layout of the figure
layout = go.Layout(
    updatemenus=[
        dict(
            active = 0, 
            x=0.2,
            y=1.09,
            yanchor="top",
            buttons=list([
                dict(label="(1) &#120572; преку време",
                             method="update",
                             args=[{"visible": [True, True, True, True, True, True, True, False, False, False]},
                                   {'annotations':[
                                               dict(text="Прикажи: ", 
                                                     showarrow=False,
                                                     x=0.25, 
                                                     y=1.15, 
                                                     yref="paper", 
                                                     align="left"),
                                               dict(x=0.15,
                                                    y=0.82,
                                                    showarrow=False,
                                                    text='&#120572; преку време',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                               dict(x=0.228,
                                                    y=0.13,
                                                    showarrow=False,
                                                    text='t',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper')],
                                    'xaxis2': dict(range = [0,100],
                                                   tickvals = [0, 20, 40, 60, 80, 100],
                                                   linecolor='#000',
                                                   domain=[0.09, 0.38],
                                                   anchor='y2',
                                                   mirror = True,
                                                   side='bottom',
                                                   ticks='',
                                                   showline=True),
                                  'yaxis2': dict(autorange=False,
                                                 range=[0.0890, 0.0905],
                                                 tickvals = [0.0890, 0.0892, 0.0894, 0.0896, 0.0898, 0.0900, 0.0902, 0.0904],
                                                 linecolor='#000',
                                                 domain=[0.25, 0.75],
                                                 anchor='x2',
                                                 mirror = True,
                                                 ticks='',
                                                 showline=True)}]),
                
                dict(label="(2) R<sub>0</sub> преку време",
                             method="update",
                             args=[{"visible": [True, True, True, True, True, True, False, True, False, False]},
                                   {'annotations': [
                                               dict(text="Прикажи: ", 
                                                     showarrow=False,
                                                     x=0.25, 
                                                     y=1.15, 
                                                     yref="paper", 
                                                     align="left"),
                                               dict(x=0.15,
                                                    y=0.82,
                                                    showarrow=False,
                                                    text='R<sub>0</sub> преку време',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                                dict(x=0.228,
                                                    y=0.13,
                                                    showarrow=False,
                                                    text='t',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                                dict(x=0.01,
                                                    y=0.5,
                                                    showarrow=False,
                                                    textangle = -90,
                                                    text='R<sub>0</sub>',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper')   ],
                                    'xaxis2': dict(range = [0,100],
                                                   tickvals = [0, 20, 40, 60, 80, 100],
                                                   linecolor='#000',
                                                   domain=[0.08, 0.38],
                                                   anchor='y2',
                                                   mirror = True,
                                                   side='bottom',
                                                   ticks='',
                                                   showline=True),
                                   'yaxis2': dict(autorange=False,
                                                  range=[0, 5.5],
                                                  tickvals = [0, 1, 2, 3, 4, 5],
                                                  linecolor='#000',
                                                  domain=[0.25, 0.75],
                                                  anchor='x2',
                                                  mirror = True,
                                                  ticks='',
                                                  showline=True)}
                                  ]) ,
                
                dict(label="(3) &#120572; по група",
                             method="update",
                             args=[{"visible": [True, True, True, True, True, True, False, False, True, False]},
                                   {'annotations': [
                                               dict(text="Прикажи: ", 
                                                     showarrow=False,
                                                     x=0.25, 
                                                     y=1.15, 
                                                     yref="paper", 
                                                     align="left"),
                                               dict(x=0.172,
                                                    y=0.82,
                                                    showarrow=False,
                                                    text='&#120572; по група',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                               dict(x=0.128,
                                                    y=0.133,
                                                    showarrow=False,
                                                    text='Возрасна група',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                               dict(x=0.01,
                                                    y=0.5,
                                                    showarrow=False,
                                                    textangle = -90,
                                                    text='&#120572;',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper')],
                                    'xaxis2': dict(autorange = True,
                                                   linecolor='#000',
                                                   domain=[0.08, 0.38],
                                                   anchor='y2',
                                                   mirror = True,
                                                   side='bottom',
                                                   ticks='',
                                                   showline=True,
                                                   tickfont = dict(size=9)),
                                   'yaxis2': dict(autorange = True,
                                                  linecolor='#000',
                                                  domain=[0.25, 0.75],
                                                  anchor='x2',
                                                  mirror = True,
                                                  ticks='',
                                                  showline=True)}
                                  ]) , 
                dict(label="(4) Популација",
                             method="update",
                             args=[{"visible": [True, True, True, True, True, True, False, False, False, True]},
                                   {'annotations': [
                                               dict(text="Прикажи: ", 
                                                     showarrow=False,
                                                     x=0.25, 
                                                     y=1.15, 
                                                     yref="paper", 
                                                     align="left"),
                                               dict(x=0.077,
                                                    y=0.82,
                                                    showarrow=False,
                                                    text='Распределба на популација',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                               dict(x=0.13,
                                                    y=0.133,
                                                    showarrow=False,
                                                    text='Возрасна група',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper'),
                                               dict(x=0.01,
                                                    y=0.5,
                                                    showarrow=False,
                                                    textangle = -90,
                                                    text='%',
                                                    font=dict(size=10),
                                                    xref='paper',
                                                    yref='paper')],
                                    'xaxis2': dict(autorange = True,
                                                   linecolor='#000',
                                                   domain=[0.08, 0.38],
                                                   anchor='y2',
                                                   mirror = True,
                                                   side='bottom',
                                                   ticks='',
                                                   showline=True,
                                                  tickfont = dict(size=9)),
                                   'yaxis2': dict(autorange = True,
                                                  linecolor='#000',
                                                  domain=[0.25, 0.75],
                                                  anchor='x2',
                                                  mirror = True,
                                                  ticks='',
                                                  showline=True)}
                                  ]) 
                ]),
            direction="down"
            )],
                  title = "SIERD; Помладо население",
                  title_x = 0.5, 
                  xaxis_title='t',
                  annotations=[
                              dict(text="Прикажи: ", 
                                   showarrow=False,
                                   x=0.25,
                                   y=1.15, 
                                   yref="paper",
                                   align="left"),
                              dict(x=0.15,
                                   y=0.82,
                                   showarrow=False,
                                   text='&#120572; преку време',
                                   font=dict(size=10),
                                   xref='paper',
                                   yref='paper'),
                               dict(x=0.228,
                                    y=0.13,
                                    showarrow=False,
                                    text='t',
                                    font=dict(size=10),
                                    xref='paper',
                                    yref='paper')],
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
                                domain=[0.09, 0.38],
                                anchor='y2',
                                mirror = True,
                                side='bottom',
                                ticks='',
                                showline=True),
                  yaxis2=dict(autorange=False,
                            range=[0.0890, 0.0905],
                            tickvals = [0.0890, 0.0892, 0.0894, 0.0896, 0.0898, 0.0900, 0.0902, 0.0904],
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
fig9_4 = dict(data=data, layout=layout)
plot(fig9_4, filename = 'fig9_young.html', config = config)
display(HTML('fig9_young.html'))

Имплементациите до сега ни дозволуваат да дизајнираме некои поедноставни SIR модели што би се приближиле до некои реални сценарија. Со појавата на COVID-19 вирусот информациите за ваквите модели се зачестија меѓутоа некои [статии/трудови](https://scholar.google.de/scholar?as_vis=1&q=coronavirus+SIR&hl=en&as_sdt=1,5&as_ylo=2020) се доста комплексни гледајќи дека е игра со модели. 


Следните неколку поглавја ќе се обидеме да дизајнираме и да моделираме вистински податоци (real-world data), каде тема на истражување е [Coronavirus - COVID19](https://www.who.int/emergencies/diseases/novel-coronavirus-2019) пандемијата што започна на почеток од 2020 година. 