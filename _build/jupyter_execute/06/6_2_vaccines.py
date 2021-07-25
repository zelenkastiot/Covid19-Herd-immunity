# Моделирање на вакцинација

Сега се за да ја илустирам комплексноста на колективниот имунитет ќе се свртивме кон контрамерки што можеме да ги преземеме за да ја намалиме големината на епидемијата.

Постојат неколку начини на кои можеме да пристапиме на ова. Во ова поглавје ќе разгледаме начини на кои можеме да ја промениме реакцијата на поединецот на потенцијална инфекција. Со тоа што поединците се со помала веројатност да бидат заразени, ги намалуваме шансите дека средбата ќе резултира во секундарна инфекција и, според тоа, ја намалуваме можноста за широко распространето заболување. Ќе видиме дека е важно колку чувствителност на поединци менуваме, и често кои индивидуи.

(Во подоцнежното поглавје - *Моделирање на физичко дистанцирање*, ќе разгледаме алтернативен пристап кој ги остава индивидуалните чувствителности сами, но ја менува топологијата на средбите на ниво на популација.)

**Вакцинацијата** ја менува чувствителноста на **биолошко ниво**, со промена на имунолошкиот одговор на поединецот и во ова поглавје ќе разговараме за начините на кои вакцините влијаат на ширењето на епидемијата кај популацијата. Но, важно е да се запамети дека истиот ефект може да се постигне на **физичко ниво**, без вакцини и всушност без биолошки интервенции, како што ќе видиме подоцна. Од перспектива на ширење епидемија, и биолошките и физичките пристапи се однесуваат во голема мера на ист начин.

## Што се вакцини?

Поголемиот дел од историјата не бевме во можност да влијаеме на напредокот на болестите со биолошки средства. Наместо тоа, ние сме ограничени на користење топологија - изолација и карантин - за да се намали ширењето на некоја болест или да се забави нејзиниот напредок. За многу болести, овие пристапи беа неефикасни со оглед на динамиката на болеста и условите од секојдневниот живот за поголемиот дел од населението, па дури и да се биде доволно богат за да се заклучи не беше гарантирано да се поштеди од инфекција.

Ова се промени на крајот на деветнаесеттиот век со воведување на **вакцини**. Вакцинацијата најпрво се обиде на скала од страна на Сер Едвард enенер, кој ги сфати сличностите помеѓу сипаници - разурнувачка болест и причина за огромно страдање - и кравјо сипаници, далеку поблага поплака која најчесто се среќава кај млекарите кои ја земаа од говеда. Ова се покажа како прво во долгата низа иновации што сега целосно ја искоренија сипаниците.

Вакцините дејствуваат со подготвување на имунолошкиот систем на една личност, така што, ако подоцна се заразат, тие веќе имаат имунолошки апарати потребни за борба против патогенот. Критично, ова го намалува времето помеѓу настанувањето на инфекцијата и започнувањето на имунолошкиот одговор, што значи дека има помалку патоген за борба против и затоа има поголеми шанси да се спречи заразувањето на инфекцијата кај таа личност. Понекогаш ова може да биде толку ефикасно што поединецот не е свесен дека дури бил заразен; почесто страдаат од поблага верзија на болеста, со помалку сериозни симптоми од кои закрепнуваат побрзо.

Постојат многу начини да се создаде вакцина. Некој може да стори како што стори Jener и да употреби **лесна варијанта** на болеста за која се интересира. Може да се земе вистинската болест и да се произведе **денатуриранаt** верзија што не може да предизвика инфекција, но сепак го подготвува имунитетот. Современите вакцини честопати се дури и поспецифични од ова, идентификувајќи некои од површинските протеини кои го карактеризираат патогенот и воведувајќи ги само нив како буквар.


Заклучно, вакцините го учат имунолошки систем како да создадете антитела кои штитат од болести. Многу е побезбедно за вашиот имунолошки систем да го научи ова преку вакцинација отколку со фаќање на болести и нивно лекување. Штом вашиот имунолошки систем знае како да се бори против некоја болест, честопати може да ве заштити многу години.


Имунологијата е неизмерна тема, но за среќа не треба да ја разбираме нејзината механика - како работи кај поединци - за да ја разбереме нејзината епидемиологија - како работи кај популациите. Всушност, како што ќе видиме, не ни треба вакцина со цел да ги добиеме ефектите од вакцинацијата.

## Повторно воведување на Scale-free мрежи

Тука се навратив на мрежите за контакт со луѓе како подлога за епидемија. Таквата контактна мрежа наликува на топологија на напојување со прекин на струјата отколку на „нормалната“ топологија на мрежата ЕР: има јазли кои имаат степени (контакти) значително поголеми од просекот на мрежата во целина. Посочивме дека ваквите мрежи се многу добри во ширењето болести.

Колку добро? Мрежите за контакт со луѓе имаат различни пресеци, точката во која драматично се намалува веројатноста да имате јазли со повисоки степени. Можеме да истражиме што значи ова со избирање на динамиката на болеста и варирање на пресекот за да видиме како истата болест се шири на мрежи со *различни топологии*.

from epydemic import NetworkGenerator
import numpy as np
import networkx as nx
import epydemic
from mpmath import *
import math
import matplotlib
%matplotlib inline
%config InlineBackend.figure_format = 'png'
matplotlib.rcParams['figure.dpi'] = 300
import matplotlib.pyplot as plt
import seaborn
matplotlib.style.use('seaborn')
seaborn.set_context("notebook", font_scale=1.35)
from scipy.integrate import odeint
import plotly.graph_objects as go
import plotly.tools as tls
from plotly.validators.scatter.marker import SymbolValidator
from plotly.offline import plot, iplot, init_notebook_mode
from IPython.core.display import display, HTML

init_notebook_mode(connected = True)
config={'showLink': False, 'displayModeBar': False}


class PowerLawWithCutoffNetwork(epydemic.NetworkGenerator):
    N = 'hcn.N'           #: Experimental parameter for the order of the network
    ALPHA = 'hcn.alpha'   #: Experimental parameter for the exponent of the distribution
    KAPPA = 'hcn.kappa'   #: Experimewntal parameter for the cutoff of the distribution

    def __init__(self, params=None, limit=None):
        super(PowerLawWithCutoffNetwork, self).__init__(params, limit)

    def _makePowerlawWithCutoff(self, alpha, kappa):
        '''Create a model function for a powerlaw distribution with exponential cutoff.

        :param alpha: the exponent of the distribution
        :param kappa: the degree cutoff
        :returns: a model function'''
        C = polylog(alpha, math.exp(-1.0 / kappa))
        def p( k ):
            return (pow((k + 0.0), -alpha) * math.exp(-(k + 0.0) / kappa)) / C
        return p

    def _generateFrom(self, N, p, maxdeg=100):
        '''Generate a random graph with degree distribution described
        by a model function.

        :param N: number of numbers to generate
        :param p: model function
        :param maxdeg: maximum node degree we'll consider (defaults to 100)
        :returns: a network with the given degree distribution'''
        rng = np.random.default_rng()
        ns = []
        t = 0
        for i in range(N):
            while True:
                # draw a random degree
                k = rng.integers(1, maxdeg)

                # do we include a node with this degree?
                if rng.random() < p(k):
                    # yes, add it to the sequence; otherwise,
                    # draw again
                    ns.append(k)
                    t += k
                    break

        # the final sequence of degrees has to sum to an even
        # number, as each edge has two endpoints
        # if the sequence is odd, remove an element and draw
        # another from the distribution, repeating until the
        # overall sequence is even
        while t % 2 != 0:
            # pick a node at random
            i = rng.integers(0, len(ns) - 1)

            # remove it from the sequence and from the total
            t -= ns[i]
            del ns[i]

            # choose a new node to replace the one we removed
            while True:
                # draw a new degree from the distribution
                k = rng.integers(1, maxdeg)

                # do we include a node with this degree?
                if rng.random() < p(k):
                    # yes, add it to the sequence; otherwise,
                    # draw again
                    ns.append(k)
                    t += k
                    break

        # populate the network using the configuration
        # model with the given degree distribution
        g = nx.configuration_model(ns, create_using=nx.Graph())
        return g

    def _generate(self, params):
        '''Generate the human contact network.

        :param params: the experimental parameters
        :returns: a network'''
        N = params[self.N]
        alpha = params[self.ALPHA]
        kappa = params[self.KAPPA]

        return self._generateFrom(N, self._makePowerlawWithCutoff(alpha, kappa))

class MonitoredSIR(epydemic.SIR, epydemic.Monitor):
 
    def __init__(self):
        super(MonitoredSIR, self).__init__()
        
    def build(self, params):
        '''Build the observation process.
        
        :param params: the experimental parameters'''
        super(MonitoredSIR, self).build(params)

        
        self.trackNodesInCompartment(epydemic.SIR.SUSCEPTIBLE)
        self.trackNodesInCompartment(epydemic.SIR.REMOVED)

Поставување на динамиката и големината на мрежата: 

# параметри за мрежата
N = 10_000
alpha = 2

# времетраење на симулација 
T = 1000

# местење на динамиката на болеста
pInfected = 0.001
pInfect = 0.01
pRemove = 0.002

ts_traces = []
sss_traces = []
iss_traces = []
rss_traces = []

for i in range(10, 81, 1):
    params = dict()
    params[epydemic.SIR.P_INFECTED] = pInfected
    params[epydemic.SIR.P_INFECT] = pInfect
    params[epydemic.SIR.P_REMOVE] = pRemove
    params[epydemic.PLCNetwork.N] = N
    params[epydemic.PLCNetwork.EXPONENT] = alpha
    params[epydemic.PLCNetwork.CUTOFF] = i
    params[epydemic.Monitor.DELTA] = T / 50

    e = epydemic.StochasticDynamics(MonitoredSIR(), epydemic.PLCNetwork())
    rc = e.set(params).run()
    
    timeseries = rc['results']['epydemic.Monitor.timeseries']
    ts = timeseries['epydemic.Monitor.observations']
    sss = timeseries['epydemic.SIR.S']
    iss = timeseries['epydemic.SIR.I']
    rss = timeseries['epydemic.SIR.R']
    
    ts_traces.append(ts)
    sss_traces.append(sss)
    iss_traces.append(iss)
    rss_traces.append(rss)

Прикажување на резултатите за различните cutoff вредности за Powerlaw мрежа: 

data = []
for trace in range(0, 70, 1):
    
    sim_ts  =  ts_traces[trace]
    sim_sss = sss_traces[trace]
    sim_iss = iss_traces[trace]
    sim_rss = rss_traces[trace]
    
    data_1 = go.Scatter(x = sim_ts, 
                        y = sim_sss, 
                        mode='markers',
                        visible = False,
                        marker_color="blue",
                        name = "Подлежни; <i>S(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')


    data_2 = go.Scatter(x = sim_ts, 
                        y = sim_iss,
                        mode='markers',
                        visible = False,
                        marker_color="red",
                        name = "Заразени; <i>I(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')


#     data_3 = go.Scatter(x = sim_ts,
#                         y = sim_rss, 
#                         mode='markers',
#                         visible = False,
#                         marker_color="green",
#                         name = "Оздравени; <i>R(t)</i>",
#                         hovertemplate = '<i> %{y:.0f} </i> луѓе')

    data.append(data_1)
    data.append(data_2)
#     data.append(data_3)

# Број на траги
data_len = len(data)
# print(data_len)

# Направи ги трагите за 0-та вредност видливи
data[0]['visible'] = True
data[1]['visible'] = True

# Креирај slider
steps = []
for i in range(0, 70, 1):
    step = dict(
        method = 'restyle',  
        args = ['visible', [False]*data_len],
        label = str(i+10))
    for j in range(0,2):
        step['args'][1][i*2+j] = True 
    
    steps.append(step)

sliders = [dict(
    active = 0,
    currentvalue = {'prefix':
                    "k (cutoff) = <b>"},
    pad = {"t": 80, "b": 10},
    steps = steps
)]

# Изглед на фигура
layout = go.Layout(title = 'SIR на powerlaw мрежи со различни cutoff вредности (<i>N</i> = {n}, &#945;={a})'.format(n=N, a=alpha),
                  title_x = 0.5, 
                  legend=dict(orientation = 'v',
                              bordercolor="Gray",
                              borderwidth=1),
                  xaxis_title='<i>t</i>',
                  xaxis=dict(range=[0,1000], 
                             mirror=False,
                             ticks='outside',
                             showline=True,
                             tickvals = [0, 250, 500, 750, 1000],
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  yaxis_title='<i>N</i>',
                  yaxis=dict(range=[0,10_000], 
                             mirror=False,
                             ticks='outside', 
                             showline=True,
                             showspikes = True,
                             linecolor='#000',
                             tickvals = [0, 2000, 4000, 6000, 8000, 10_000], 
                             tickfont = dict(size=11)),
                    plot_bgcolor='#fff', 
                    hovermode = 'x unified',
                    width = 700, 
                    height = 570,
                    sliders = sliders,
                    font = dict(size = 10),
                    margin=go.layout.Margin(l=50,
                                         r=50,
                                         b=60,
                                         t=35))

# Прикажи фигура 
fig5 = dict(data=data, layout=layout)
plot(fig5, filename = 'fig5.html', config = config)
display(HTML('fig5.html'))

Ова ни кажува дека мрежите со мал максимален број контакти ($\kappa = 10$) имаат релативно мали епидемии кои се појавуваат доста бавно: „врвот“ на инфекциите се јавува подалеку од избувнувањето. Како што ја зголемуваме $\kappa$, гледаме дека поголемите епидемии се случуваат побрзо (поблиску до почетокот на епидемијата), сè додека резултатите не се стабилизираат и нема да се променат многу, бидејќи продолжуваме да ги зголемуваме $\kappa$: се чини дека максимум околу 30 контакти се доволни за да се заразат околу половина од популацијата на врвот.

Повторно теоријата зад Powerlaw мрежите: 

Powerlaw мрежа со експонент $\alpha$ има одредена дистибуција дадена од:

\begin{equation*}
p_k \propto k^{-\alpha} 
\end{equation*}


каде $p_k$ е веројатноста дека случајно избран јазол во мрежата ќе има степен $k$. Оваа дистрибуција на степени има својство дека некои јазли можат да имаат многу високи степени со не-нулта веројатност, што доведува до многу големи центри со висока централност. Во популациска мрежа, ова би вовело поединци кои биле масовно подобро поврзани од другите, што обично се смета за непожелно: има ограничувања за тоа со колку луѓе дури и најпопуларната личност може да дојде во физички контакт.

Спротивно на тоа, мрежата за напојување со прекин на електрична енергија, става ограничување - cutoff (означено $k$) на „најверојатно“ највисокиот степен. До прекинот, степенот на дистрибуција се однесува како мрежа за напојување; над пресекот, веројатноста опаѓа експоненцијално брзо, што ги прави големи центри многу малку веројатни. Оваа дистрибуција на степени е дадена од: 

\begin{equation*}
p_k \propto k^{-\alpha} e^{-k / \kappa}
\end{equation*}

Следниот график ја покажува разликата во веројатноста да наидете на јазли од различен степен под двете распределби: 

```{figure} images/powerlaw-cutoff.png
---
width: 60%
align: center
name: image
---
Log-log график за степенски мрежи со cutoff и без cutoff
```



## Вакцинација кај SIR 

Ние очигледно го поедноставивме ова вакцинирање, бидејќи секој што ќе зафати болест за која е вакциниран ќе знае. Вакцинацијата не секогаш дава целосен имунитет против инфекција.

Како изгледа вакцинацијата кај  SIR моделот? Вакцинирана личност е оној кој не може да ја зафати болеста. Во смисла на моделот, тоа значи дека индивидуа која ги покажува тие карактеристики на веќе заболената и „извадена“ во состојбата **R**. Всушност, ова е она што се случува и биолошки: вакцинирано лице е изложено на супстанца што ги прави исти како да би имале болест, без всушност да бара да ја имаат. Ефектот што го бараме е имунитет на стада, каде што нема доволно подложни индивидуи во популацијата за да дозволат болеста да се утврди. Но, критички бараме [имунитет на стадо](https://zelenkastiot.github.io/Covid19-Herd-immunity/06/6_herd-explained.html), без претходно болеста да помине низ населението, со сите страдања и (евентуално) смрт што може да ги повлече.

Можеме да моделираме вакцинација со помош на нов оддел, што ќе доведе до модел што може да се нарече **SIVR**, заробување на вакцинираните лица **V**. Ако сакавме да истражуваме делумен имунитет преку вакцинација, тогаш **SIVR** ќе ни овозможи да имаме, на пример, различни вредности на $p_{infect}$ во зависност од тоа дали е **S** или **V** поединец што е потенцијално заразен: **V** станува половина куќа помеѓу **S** (целосно подложна ) и **R** (целосно отстранети).

## Вакцнирање по случајност 

Повеќето вакцини се применуваат широко на популација, обично во детството за низа вообичаени болести со кои повеќето луѓе ќе се соочат. Идеално, сите се вакцинирани; во пракса, некои се пропуштаат од разни причини, во некои вакцината нема да „земе“, некои мора да ја избегнуваат од неповрзани медицински причини и сл.

Можеме да се обидеме детално да ги моделираме начините на кои се случува овој процес, но целокупниот ефект е многу сличен на случајот кога земаме популација и случајно вакцинираме одреден процент од лицата пред да започнеме со инфекцијата. Бидејќи ова е SIR, ова значи дека ние случајно доделуваме ваков дел, $p_{vaccinated}$ на јазли во одделот **R**.

class MonitoredVaccinatedSIR(epydemic.SIR, epydemic.Monitor):
    '''
    SIVR модел 
    '''
    P_VACCINATED = 'pVaccinated'   #: Веројатност дека 
                                    # поединец првично е отстранет.
    def __init__(self):
        super(MonitoredVaccinatedSIR, self).__init__()
        
    def build(self, params):
        '''Build the observation process.
        
        :param params: the experimental parameters'''
        super(MonitoredVaccinatedSIR, self).build(params)

        # промена на почетната веројатност на одделот за вакцинирање (отстранување) на дел
        pInfected = params[epydemic.SIR.P_INFECTED]
        pVaccinated = params[self.P_VACCINATED]
        self.changeCompartmentInitialOccupancy(epydemic.SIR.INFECTED, pInfected)
        self.changeCompartmentInitialOccupancy(epydemic.SIR.REMOVED, pVaccinated)
        self.changeCompartmentInitialOccupancy(epydemic.SIR.SUSCEPTIBLE, 1.0 - pInfected - pVaccinated)

        # следи ги и другите состојби
        self.trackNodesInCompartment(epydemic.SIR.SUSCEPTIBLE)
        self.trackNodesInCompartment(epydemic.SIR.REMOVED)

Можеме да избереме кој било број што го сакаме за $p_{vaccinated}$, со тоа што 60% се типична цел за кампањи за имунизација и затоа ќе идеме со над 50% од популацијата. 

pVaccinated = 0.6

Оставајќи ги сите други експериментални параметри исти од горе, ајде да избереме вредност од $\kappa = 57$ како cutoff што видовме дека создаде епидемија кај невакцинирана популација и да спроведеме експеримент каде прво вакцинираме (отстрануваме) дел од јазли по случаен избор.


params[MonitoredVaccinatedSIR.P_VACCINATED] = pVaccinated
params[epydemic.PLCNetwork.CUTOFF] = 57

e = epydemic.StochasticDynamics(MonitoredVaccinatedSIR(), epydemic.PLCNetwork())
rc_1 = e.set(params).run()

data = []

timeseries = rc_1['results']['epydemic.Monitor.timeseries']
sim_ts = timeseries['epydemic.Monitor.observations']
sim_sss = timeseries['epydemic.SIR.S']
sim_iss = timeseries['epydemic.SIR.I']
sim_rss = timeseries['epydemic.SIR.R']
    
data_1 = go.Scatter(x = sim_ts, 
                        y = sim_sss, 
                        mode='markers',
                        visible = True,
                        marker_color="blue",
                        name = "Подлежни; <i>S(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')


data_2 = go.Scatter(x = sim_ts, 
                        y = sim_iss,
                        mode='markers',
                        visible = True,
                        marker_color="red",
                        name = "Заразени; <i>I(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')


data.append(data_1)
data.append(data_2)

y_lim = N * (1.0 - pVaccinated - pInfected)

# Изглед на фигура
layout = go.Layout(title = 'SIR епидемија со присуство на {v:.0f}% вакцинација (&#954; = {k})'.format(v=rc_1['parameters']['pVaccinated'] * 100, k=rc_1['parameters']['epydemic.generators.PLCNetwork.cutoff']), 
                   title_x = 0.5, 
                  legend=dict(orientation = 'v',
                              bordercolor="Gray",
                              borderwidth=1),
                  xaxis_title='<i>t</i>',
                  xaxis=dict(range=[0,1000], 
                             mirror=False,
                             ticks='outside',
                             showline=True,
                             tickvals = [0, 250, 500, 750, 1000],
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  yaxis_title='<i>N</i>',
                  yaxis=dict(range=[0,y_lim], 
                             mirror=False,
                             ticks='outside', 
                             showline=True,
                             showspikes = True,
                             linecolor='#000',
                             tickfont = dict(size=11)),
                    plot_bgcolor='#fff', 
                    hovermode = 'x unified',
                    width = 700, 
                    height = 450,
                    font = dict(size = 10),
                    margin=go.layout.Margin(l=50,
                                         r=50,
                                         b=60,
                                         t=35))

# Прикажи фигура 
fig6 = dict(data=data, layout=layout)
plot(fig6, filename = 'fig6.html', config = config)
display(HTML('fig6.html'))


Споредувањето на ова со горната слика покажува доста драматично намалување на големината на епидемијата.

Но, тука имаше еден интересен факт! - има мал проблем овој график. Погледнете ја оската y на овој графикон. Забележав дека максималното подложно население е околу 4 000, иако мрежата има 10 000 јазли. Мислењето во овој миг ми покажуваше зошто: ние моделиравме вакцинација како превентивно отстранета, оставајќи помалку подлежни. Можеби овој резултат е тој што би го очекувале на помала мрежа? Со други зборови, дали има ефект на големина што се игра кога се движиме од 10 000 надолу кон 4 000 индивидуи?

Треба да бидеме внимателни и да ја провериме оваа можност. Ова може да се направи со тоа што ќе ја разработиме големината на невакцинираната популација и ќе создадеме мрежа со иста топологија со оваа големина и потоа да ја спроведеме нашата епидемија.

Nsmall = int(N * (1.0 - pVaccinated - pInfected))
params[epydemic.PLCNetwork.N] = Nsmall
params[epydemic.PLCNetwork.CUTOFF] = 57
params[MonitoredVaccinatedSIR.P_VACCINATED] = 0

e = epydemic.StochasticDynamics(MonitoredVaccinatedSIR(), epydemic.PLCNetwork())
rc_2 = e.set(params).run()

data = []

timeseries = rc_2['results']['epydemic.Monitor.timeseries']
sim_ts = timeseries['epydemic.Monitor.observations']
sim_sss = timeseries['epydemic.SIR.S']
sim_iss = timeseries['epydemic.SIR.I']
sim_rss = timeseries['epydemic.SIR.R']
    
data_1 = go.Scatter(x = sim_ts, 
                        y = sim_sss, 
                        mode='markers',
                        visible = True,
                        opacity=0.5,
                        marker=dict(
                            color='blue',
                            size=4),
                        name = "Подлежни (без вакцинација); <i>S(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')


data_2 = go.Scatter(x = sim_ts, 
                        y = sim_iss,
                        mode='markers',
                        visible = True,
                        opacity=0.5,
                        marker=dict(
                            color='red',
                            size=4),
                        name = "Заразени (без вакцинација); <i>I(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')


data.append(data_1)
data.append(data_2)

timeseries = rc_1['results']['epydemic.Monitor.timeseries']
sim_ts = timeseries['epydemic.Monitor.observations']
sim_sss = timeseries['epydemic.SIR.S']
sim_iss = timeseries['epydemic.SIR.I']
sim_rss = timeseries['epydemic.SIR.R']
    
data_3 = go.Scatter(x = sim_ts, 
                        y = sim_sss, 
                        mode='markers',
                        visible = True,
                        marker_color="blue",
                        name = "Подлежни (пост вакцинација); <i>S(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')


data_4 = go.Scatter(x = sim_ts, 
                        y = sim_iss,
                        mode='markers',
                        visible = True,
                        marker_color="red",
                        name = "Заразени (пост вакцинација); <i>I(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')


data.append(data_3)
data.append(data_4)

y_lim = N * (1.0 - pVaccinated - pInfected)

# Изглед на фигура
layout = go.Layout(title = 'SIR епидемија со и без вакцинација (N = {n}, &#954; = {k})'.format(n=Nsmall, k=rc_2['parameters']['epydemic.generators.PLCNetwork.cutoff']), 
                   title_x = 0.45, 
                  legend=dict(orientation = 'v',
                              bordercolor="Gray",
                              borderwidth=1),
                  xaxis_title='<i>t</i>',
                  xaxis=dict(range=[0,1000], 
                             mirror=False,
                             ticks='outside',
                             showline=True,
                             tickvals = [0, 250, 500, 750, 1000],
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  yaxis_title='<i>N</i>',
                  yaxis=dict(range=[0, y_lim], 
                             mirror=False,
                             ticks='outside', 
                             showline=True,
                             showspikes = True,
                             linecolor='#000',
                             tickfont = dict(size=11)),
                    plot_bgcolor='#fff', 
                    hovermode = 'x unified',
                    width = 750, 
                    height = 450,
                    font = dict(size = 10),
                    margin=go.layout.Margin(l=50,
                                         r=50,
                                         b=60,
                                         t=35))

# Прикажи фигура 
fig6 = dict(data=data, layout=layout)
plot(fig6, filename = 'fig6.html', config = config)
display(HTML('fig6.html'))


Првото нешто што треба да се види е дека двата графика се различни: не само големината на мрежата влијае на работите. Во малата, но невакцинирана мрежа, гледаме поголема епидемија; во вакцинираната мрежа гледаме многу помала и побавна епидемија. Што е различно помеѓу двата случаи, бидејќи мрежите се со иста големина?

Мислата од еден момент може да го сугерира одговорот. Создадовме две мрежи со иста топологија, едната каде дел од јазлите се отстрануваат со вакцинација и другата каде што навистина беа отстранети голем број јазли (или поточно, никогаш не беа присутни во мрежата). Двете мрежи имаат јазли од висок степен, како што би очекувале за мрежите со моќност со прекинување. Но, во последниот (вакциниран) случај, некои од тие јазли од висок степен ќе бидат вакцинирани и затоа не се во можност да ја шират болеста. И бидејќи болеста се шири преку контакт помеѓу јазлите **S** и **I**, ја губиме можноста да заразиме јазол од висок степен што може да дејствува како супер-пренесувачи кои можат да заразат голем број јазли. И, тоа намалување на супер-ширењето е доволно за промена на динамиката на болеста.



## Колку се поврзани супер-пренесувачите? 

Иако графиците даваат увид во проблемите мораме да ги погледнеме бројките подетално. Прво, колку контакти има најповрзаниот јазол?

g = PowerLawWithCutoffNetwork()

params = dict()
params['hcn.N'] = N
params['hcn.alpha'] = alpha
params['hcn.kappa'] = 57

hcn = g._generate(params)

ks = sorted(list(dict(nx.degree(hcn)).values()))
print('Најголемиот степен на јазолот во мрежата е = {kmax}'.format(kmax=max(ks)))

94 е застрашувачки голем број. А, што е со бројот на контакти за просечно поврзан јазол (Mean Degree)?

print('Mean node degree = {kmean:.2f}'.format(kmean=np.mean(ks)))

Многу различно од најповрзаниот јазол, и токму оваа одлика ја разликува мрежата на човечки контакти од ЕР мрежите: постоење на јазли со степени што се многу повисоки од просечните. Всушност, ваквите мрежи имаат долга опашка на јазли со високи степени: само мал број во однос на големината на мрежата во целина, но сепак можат да поминат инфекција.


h = 10
print('најповрзаните {h} јазли со своите степени {l}'.format(h=h, l=ks[-h:]))

Колку се важни овие лица во ширењето на болеста? Можеме да го проучиме тоа со исклучување од нашата моделна програма за вакцинација. Наместо да вакцинираме дел од мрежата, по вакцинирањето ќе се осигураме дека дел од јазлите од највисок степен се подложни. Во суштина, ние менуваме јазли од висок степен за јазли од понизок степен во нашата програма за вакцинација.

class MonitoredVaccinatedLowDegreeSIR(MonitoredVaccinatedSIR):
    '''
    Класа модифицрана од Симон Дабсон (https://github.com/simoninireland)
    '''
    K_HIGH_FRACTION = 'k_high_fraction'
    
    def __init__(self):
        super(MonitoredVaccinatedLowDegreeSIR, self).__init__()
        
    def setUp(self, params):
        super(MonitoredVaccinatedLowDegreeSIR, self).setUp(params)
        
        # погледнете низ дел од јазли од висок степен и
        # направи ги повторно подложни, заменувајќи ги со
        # друг јазол избран по случаен избор
        rng = np.random.default_rng()
        g = self.network()
        ns = list(g.nodes())
        h = int(len(ns) * params[self.K_HIGH_FRACTION])
        degrees = dict(nx.degree(g))
        ks = sorted(list(degrees.values()))
        ks_high = set(ks[-h:])
        ns_high = [n for n in ns if degrees[n] in ks_high]
        for n in ns_high:
            if self.getCompartment(n) == self.REMOVED:
                # јазолот е отстранет, направете го повторно подложен
                self.setCompartment(n, self.SUSCEPTIBLE)
                
                # изберете друг јазол и отстранете го внатре
                # место на јазолот што само го принудивме
                # be susceptible
                while True:
                    i = rng.integers(0, len(ns) - 1)
                    m = ns[i]
                    if self.getCompartment(m) == self.SUSCEPTIBLE:
                        # најде подлежен јазол, отстранете го
                        self.setCompartment(m, self.REMOVED)
                        break

Водењето на експериментот, повторно со истите параметри на болеста и топологијата на мрежата како порано, ни ги покажува ефектите од овој неуспех при вакцинацијата.

kHighFraction = 0.08 

params = dict()

params[epydemic.SIR.P_INFECTED] = pInfected
params[epydemic.SIR.P_INFECT] = pInfect
params[epydemic.SIR.P_REMOVE] = pRemove
params[epydemic.PLCNetwork.N] = N
params[epydemic.PLCNetwork.EXPONENT] = alpha
params[epydemic.PLCNetwork.CUTOFF] = 57
params[epydemic.Monitor.DELTA] = T / 50
params[MonitoredVaccinatedLowDegreeSIR.P_VACCINATED] = 0
params[MonitoredVaccinatedLowDegreeSIR.K_HIGH_FRACTION] = kHighFraction

e = epydemic.StochasticDynamics(MonitoredVaccinatedLowDegreeSIR(), epydemic.PLCNetwork())
rc = e.set(params).run()

data = []

timeseries = rc['results']['epydemic.Monitor.timeseries']
sim_ts = timeseries['epydemic.Monitor.observations']
sim_sss = timeseries['epydemic.SIR.S']
sim_iss = timeseries['epydemic.SIR.I']
sim_rss = timeseries['epydemic.SIR.R']
    
data_1 = go.Scatter(x = sim_ts, 
                        y = sim_sss, 
                        mode='markers',
                        visible = True,
                        marker_color="blue",
                        name = "Подлежни; <i>S(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')


data_2 = go.Scatter(x = sim_ts, 
                        y = sim_iss,
                        mode='markers',
                        visible = True,
                        marker_color="red",
                        name = "Заразени; <i>I(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')


data.append(data_1)
data.append(data_2)

y_lim = N * (1.0 - pInfected - pVaccinated) + N * kHighFraction

# Изглед на фигура
layout = go.Layout(title = 'SIR епидемија без вакцинација на {khigh:.0f}% од најповрзаните јазли (N = {n}, &#954;= {k:.0f})'.format(khigh=kHighFraction * 100, n=N, k=rc['parameters']['epydemic.generators.PLCNetwork.cutoff']), 
                   title_x = 0.5, 
                  legend=dict(orientation = 'v',
                              bordercolor="Gray",
                              borderwidth=1),
                  xaxis_title='<i>t</i>',
                  xaxis=dict(range=[0,1000], 
                             mirror=False,
                             ticks='outside',
                             showline=True,
                             tickvals = [0, 250, 500, 750, 1000],
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  yaxis_title='<i>N</i>',
                  yaxis=dict(range=[0,y_lim+2000], 
                             mirror=False,
                             ticks='outside', 
                             showline=True,
                             showspikes = True,
                             linecolor='#000',
                             tickfont = dict(size=11)),
                    plot_bgcolor='#fff', 
                    hovermode = 'x unified',
                    width = 700, 
                    height = 450,
                    font = dict(size = 9),
                    margin=go.layout.Margin(l=50,
                                         r=50,
                                         b=60,
                                         t=65))

# Прикажи фигура 
fig7 = dict(data=data, layout=layout)
plot(fig7, filename = 'fig7.html', config = config)
display(HTML('fig7.html'))

Оставањето мал дел од јазлите од висок степен - т.е. најврзаните лица (hubs) - да останат подлежни, повторно ја менува епидемијата, што ја прави поголема и побрза. Не е важна само големината на вакцинираната популација: тоа што го вакцинираме (или, во овој случај, не вакцинираме) е навистина важно. Промашување дури и на мал дел од многу поврзаните, радикално ќе ја намали ефикасноста на програмата за вакцинација.


## Таргетирана вакцинација

Значи, постоењето на јазли од висок степен нуди можност болеста да зарази многу повеќе лица доколку тие јазли не се заштитени со вакцинација.

Но, ова исто така нуди можности за понатамошни контрамерки. Ако јазлите од висок степен се важни за ширење на болеста, што ако - наместо да вакцинираме по случаен избор - наместо тоа, експлицитно ќе ги насочиме оние јазли за кои веруваме дека се најважни во ширењето на болеста? Тоа може да ја направи нашата програма поефикасна. Тоа исто така може да значи дека можеме да изведеме помала, пофокусирана програма, каде што наместо широко да вакцинираме по случаен избор, ние {индексираме} вакцинација тесно <таргетирана вакцинација>, но на фокусиран, „паметен” начин.

Можеме и ова да го истражуваме. Наместо да извршуваме случајна вакцинација, ние наместо тоа насочуваме кон одреден дел од јазлите од највисок степен.

class MonitoredVaccinatedHighDegreeSIR(MonitoredSIR):
    '''
    Класа модифицрана од Симон Дабсон (https://github.com/simoninireland)
    '''
    K_VACCINATED_FRACTION = 'k_vaccinated_fraction'
    
    def __init__(self):
        super(MonitoredVaccinatedHighDegreeSIR, self).__init__()
        
    def setUp(self, params):
        super(MonitoredVaccinatedHighDegreeSIR, self).setUp(params)

        # побарајте дел од јазлите од највисок степен
        # и вакцинирајте ги (отстранете ги)
        g = self.network()
        ns = list(g.nodes())
        h = int(len(ns) * params[self.K_VACCINATED_FRACTION])
        degrees = dict(nx.degree(g))
        ks = sorted(list(degrees.values()))
        ks_high = set(ks[-h:])
        ns_high = [n for n in ns if degrees[n] in ks_high]
        for n in ns_high:
            # отстранете го (вакцинирајте го) јазолот
            self.setCompartment(n, self.REMOVED)

Колку голем дел треба да насочиме? Да бидеме амбициозни и да започнеме мало, вакцинираме само 2% од јазлите - триесет пати помалку од порано.

kVaccinatedFraction = 0.02    # топ 2% највпорзани јазли

params = dict()

params[epydemic.SIR.P_INFECTED] = pInfected
params[epydemic.SIR.P_INFECT] = pInfect
params[epydemic.SIR.P_REMOVE] = pRemove
params[epydemic.PLCNetwork.N] = N
params[epydemic.PLCNetwork.EXPONENT] = alpha
params[epydemic.PLCNetwork.CUTOFF] = 57
params[epydemic.Monitor.DELTA] = T / 50

params[MonitoredVaccinatedHighDegreeSIR.K_VACCINATED_FRACTION] = kVaccinatedFraction

e = epydemic.StochasticDynamics(MonitoredVaccinatedHighDegreeSIR(), epydemic.PLCNetwork())
rc = e.set(params).run()

data = []

timeseries = rc['results']['epydemic.Monitor.timeseries']
sim_ts = timeseries['epydemic.Monitor.observations']
sim_sss = timeseries['epydemic.SIR.S']
sim_iss = timeseries['epydemic.SIR.I']
sim_rss = timeseries['epydemic.SIR.R']
    
data_1 = go.Scatter(x = sim_ts, 
                        y = sim_sss, 
                        mode='markers',
                        visible = True,
                        opacity=0.8,
                        marker=dict(
                            color='blue',
                            size=7),
                        name = "Подлежни; <i>S(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')


data_2 = go.Scatter(x = sim_ts, 
                        y = sim_iss,
                        mode='markers',
                        visible = True,
                        opacity=0.8,
                        marker=dict(
                            color='red',
                            size=7),
                        name = "Заразени; <i>I(t)</i>",
                        hovertemplate = '<i> %{y:.0f} </i> луѓе')


data.append(data_1)
data.append(data_2)

y_lim = N * (1.0 - pInfected - pVaccinated) + N * kHighFraction

# Изглед на фигура
layout = go.Layout(title = 'SIR епидемија без вакцинација на {khigh:.0f}% од најповрзаните јазли (N = {n}, &#954;= {k:.0f})'.format(khigh=kHighFraction * 100, n=N, k=rc['parameters']['epydemic.generators.PLCNetwork.cutoff']), 
                   title_x = 0.5, 
                  legend=dict(orientation = 'v',
                              bordercolor="Gray",
                              borderwidth=1),
                  xaxis_title='<i>t</i>',
                  xaxis=dict(range=[0,1000], 
                             mirror=False,
                             ticks='outside',
                             showline=True,
                             tickvals = [0, 250, 500, 750, 1000],
                             linecolor='#000',
                             tickfont = dict(size=11)),
                  yaxis_title='<i>N</i>',
                  yaxis=dict(range=[0,N], 
                             mirror=False,
                             ticks='outside', 
                             showline=True,
                             showspikes = True,
                             linecolor='#000',
                             tickfont = dict(size=11)),
                    plot_bgcolor='#fff', 
                    hovermode = 'x unified',
                    width = 700, 
                    height = 450,
                    font = dict(size = 9),
                    margin=go.layout.Margin(l=50,
                                         r=50,
                                         b=60,
                                         t=65))

# Прикажи фигура 
fig8 = dict(data=data, layout=layout)
plot(fig8, filename = 'fig8.html', config = config)
display(HTML('fig8.html'))


Со скоро никој не вакциниран - 200 во мрежа од 10 000 - во исто време и ја намалуваме и ја забавуваме епидемијата. И двата ефекти се важни. Вкупниот број на заразени лица е помал, но исто така е и „рампата“ на почетокот на епидемијата, што значи дека се става помал стрес врз здравствените системи кои се справуваат со приливот на болни луѓе.

Кога луѓето зборуваат за **израмнување на кривата**, ова е ефектот кон кој се стремат - постигнат во овој случај преку насочена вакцинација на мал дел од популацијата.

Ова намалување на напорите за вакцинација го прави побрз, поевтин и посигурен - ако можеме да ги идентификуваме и насочиме супер-распрснувачите. Но, ова може да биде можно, бидејќи знаеме дека супер-распрснувачите се јазли од највисок степен, кои едноставно се оние со најмногу изложеност на други луѓе. Во современиот свет, степенот на контакт на една личност честопати е барем делумно функција на нивната работа, и така со насочување кон оние чии работни места ги доведуваат во контакт со повеќето луѓе - и особено во контакт со најинфицираните лица - можеме да создадеме многу ефективна стратегија за вакцинирање и брзо да ја примениме. 