# StudyCovid19

## Data
We obtained data from following sources:

- [datasets/covid-19](https://github.com/datasets/covid-19)

- [CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)

- [nytimes/covid-19-data](https://github.com/nytimes/covid-19-data)


## process

In `process/data.py` and `process/data.ipynb` you can find various functions which read and process data from above sources.

In `process/bayesian` you will find assignment notebook and processed data for three countries US, Japan, and South Korea.

## FitCovid19

We introduce the Bayesian learning technique using the Covid-19 data for Japan. In [notebook](FitCovid19/Bayesian\ learning\ with\ application\ to\ Covid-19.ipynb), we first introduce the Bayesian calibration, validation and prediction approach. We consider sub-exponential growth model consisting of two parameters, growth rate and deceleration of growth, and seek to find the optimal values of these parameters which fit the Covid-19 cases in the Japan. The notebook presents the ideas involved very briefly and highlights some key practical issues during numerical implementation. Notebook also includes source codes. We hope that this will be useful in understanding the powerful concept of Bayesian inference and learning. 
