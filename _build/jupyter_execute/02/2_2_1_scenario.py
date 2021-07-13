# Програмирање на моделот
*** 
Сега со користејќи Python ќе го програмираме моделот и ќе претставиме еден едноставен модел. Со користење на формулите од [претходната тетратка](https://zelenkastiot.github.io/COVID-19_book/01_equations/1_equations.html) ќе ги дефинираме следните параметри кои ќе ги користеме во кодовите: 

Ги добиваме нашите вредности за $S(t)$, $I(t)$ и $R(t)$ со функцијата [<code>odeint</code>](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html) од библиотеката [<code>scipy</code>](https://www.scipy.org/). Оваа функција на влез ги добива поставените вредности од корисникот за какво сценарио сака. 

## Сценарио 1 
Зададени од корисник: 
 - $N=1000$  &#x2192; популација од 1000 луѓе 
 - $\beta=1.0$ &#x2192; заразен човек заразува 1 друг човек на ден
 - $D=10.0$ &#x2192; личноста ја чува во себе и може да ја шири болеста 5 дена
 - $\gamma=\frac{1}{D}=\frac{1}{10}$ &#x2192; 10% од бројот на заразени личности заздравуваат на ден
 - $t \in (0,50)$ &#x2192; изминати денови од започнување на заразата
 
Функцијата [<code>odeint</code>](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html) на влез ги прима овие вредности и ни враќа соодветни вредности за $S(t), I(t), R(t)$ каде $t$ е изминати денови од започнување на заразата. 

Резултат од сценарио 1: 

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
    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return dS, dI, dR

# N: total number of people considered in model
N = 1000

# D: infections lasts four days
D = 10.0 

# gamma: recovery rate 
gamma = 1.0 / D

# beta: infected person infects 1 other person per day
beta = 1.0

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
figa = go.Figure()

figa.add_trace(go.Scatter(x = t, 
                         y = S, 
                         mode = 'lines',
                         line=dict(color="blue",
                                   width=2),
                         name = "Подлежни; <i>S(t)</i>",
                         hovertemplate = '<i> %{y:.0f} </i> луѓе'))

figa.add_trace(go.Scatter(x = t, 
                         y = I, 
                         mode = 'lines',
                         line=dict(color="red",
                                   width=2),
                         name = "Заразени; <i>I(t)</i>",
                         hovertemplate = '<i> %{y:.0f} </i> луѓе'))

figa.add_trace(go.Scatter(x = t, 
                         y = R, 
                         mode = 'lines',
                         line=dict(color="green",
                                   width=2),
                         name = "Излекувани; <i>R(t)</i>",
                         hovertemplate = '<i> %{y:.0f} </i> луѓе'))


figa.update_layout(title = 'Сценарио 1',
                  title_x = 0.5, 
                  xaxis_title='<i>t</i>',
                  xaxis=dict(range=[0,50], 
                             mirror=False,
                             ticks='outside',
                             showline=True,
                             tickvals = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
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
                  plot_bgcolor='#fff', 
                  hovermode = 'x unified',
                  width = 640, 
                  height = 320,
                  font = dict(size = 10),
                  margin=go.layout.Margin(l=50,
                                         r=50,
                                         b=60,
                                         t=35))

plot(figa, filename = 'fig1_a.html', config = config)
display(HTML('fig1_a.html'))

Од графикот може да се види дека по изминување на 23-25 дена скоро целата популација од 1000 луѓе се заразува, бројот на <i style="color:blue">подлежни</i> = 0. Поради големата вредност за за $R_0=\beta \cdot D = 10$ во ова сценарио **врвот** на <i style="color:red">заразени</i> е досигнат на 10-иот ден:
***
> **Сценарио 1**<br>*10-ти ден* <br><br> <i style="color:blue">Подлежни</i> &#x2192; $S(21)=124$ <br> <i style="color:red">Заразени</i> &#x2192; $I(21)=667$<br> <i style="color:green">Излекувани</i> &#x2192; $R(21)=208$

***
## Сценарио 2

Во ова сценарио се истите вредности од **Сценарио 1**, само се заменува *очекуваниот број на луѓе на кои заразена личност на пренесува болеста на* 0.5, т.е. $\beta = 0.5$. 

Резултат од **Сценарио 2**: 

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
    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return dS, dI, dR

# N: total number of people considered in model
N = 1000

# D: infections lasts four days
D = 10.0 

# gamma: recovery rate 
gamma = 1.0 / D

# beta: infected person infects 1 other person per day
beta = 0.5

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
figb = go.Figure()

figb.add_trace(go.Scatter(x = t, 
                         y = S, 
                         mode = 'lines',
                         line=dict(color="blue",
                                   width=2),
                         name = "Подлежни; <i>S(t)</i>",
                         hovertemplate = '<i> %{y:.0f} </i> луѓе'))

figb.add_trace(go.Scatter(x = t, 
                         y = I, 
                         mode = 'lines',
                         line=dict(color="red",
                                   width=2),
                         name = "Заразени; <i>I(t)</i>",
                         hovertemplate = '<i> %{y:.0f} </i> луѓе'))

figb.add_trace(go.Scatter(x = t, 
                         y = R, 
                         mode = 'lines',
                         line=dict(color="green",
                                   width=2),
                         name = "Излекувани; <i>R(t)</i>",
                         hovertemplate = '<i> %{y:.0f} </i> луѓе'))


figb.update_layout(title = 'Сценарио 2',
                  title_x = 0.5, 
                  xaxis_title='<i>t</i>',
                  xaxis=dict(range=[0,50], 
                             mirror=False,
                             ticks='outside',
                             showline=True,
                             tickvals = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
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
                  plot_bgcolor='#fff', 
                  hovermode = 'x unified',
                  width = 640, 
                  height = 320,
                  font = dict(size = 10),
                  margin=go.layout.Margin(l=50,
                                         r=50,
                                         b=60,
                                         t=35))

plot(figb, filename = 'fig1_b.html', config = config)
display(HTML('fig1_b.html'))

Со оваа мала промена и по изминување на 50-тиот ден сеуште има <i style="color:blue">подлежни</i> луѓе, воедно и бројот на <i style="color:red">заразени</i> го достигнува својот **врв** некаде околу 20-иот ден: 

***

> **Сценарио 2**<br>*21-ви ден* <br><br> <i style="color:blue">Подлежни</i> &#x2192; $S(21)=208$ <br> <i style="color:red">Заразени</i> &#x2192; $I(21)=478$<br> <i style="color:green">Излекувани</i> &#x2192; $R(21)=314$

***

Од оваа мала промена на параметарот $\beta$ комплетно го смени исходот на сценариото, скоро за 200 луѓе врвот на <i style="color:red">заразени</i> е помал во второто сценарио и бројот на <i style="color:green">излекувани</i> е скоро колку тоталната популација на крајот од 50-иот ден.  


Почетните параметри имаат голем удел во овие **едноставни диференцијални равенки** (ODEs), бидејќи самите равенки се многу чувствителни (sensitive) на своите почетни параметри. Токму поради оваа чувстивелност, моделирање на вакви заразни болести е исклучително тешко бидејќи мали промени во параметрите може да резултираат со тотално различни исходи. 


Следните три тетратки се интерактивни графици каде со променување на некои од овие почетни параметри се менува и исходот во текот на сите 50 денови. 


```{toctree}
:hidden:
:titlesonly:


Интерактивен график 1 <2_2_2_D>
Интерактивен график 2 <2_2_3_gamma>
Интерактивен график 3 <2_2_4_beta>
```
