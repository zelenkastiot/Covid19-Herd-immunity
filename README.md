# Covid19-Herd-immunity

- **Mentors**: Prof. Miroslav Mirchev, Prof. Lasko Basnarkov
- **Students:** Kiril Zelenkovski
- **Research topic:** Extended research from the [COVID-19_book](https://zelenkastiot.github.io/COVID-19_book/intro): This repo contains Jupyter notebooks related to COVID19 herd immunity simulations and analysis.We are interested in how the individual immunity (gained through herd immunity) of people is distributed based on their connection (exposure) to other people (degree-based mean-field DBMF). We are using SIR to describe the population, as it is the simplest and partially adequate model to run COVID19 simulations:
 We take a network with given degree distribution. We solve the evolution equations of probability for the infected when the nodes of the networks are grouped by neighbors (degree-based mean-field DBMF). These equations are based on the paper [1](). For different parameters of infection (lambda) when there is a pandemic, we observe the distribution of the infected (or recovered). At the end of a pandemic, we observe it as a function of the number of neighbors. Then we calculate the percentage of people that have gained immunity.
- **Клучни Зборови**: Python, Plotly, Covid-19, degree based mean field DBMF, Scale-free networks, Herd immunity
