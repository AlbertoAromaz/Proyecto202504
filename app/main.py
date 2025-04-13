import utils
import read_csv
import charts
import pandas as pd

def run():
  df = pd.read_csv('./app/data.csv')
  df = list(filter(lambda item : item['Continent'] == 'South America', df))

  countries = list(map(lambda x: x['Country', df]))
  percentages = list(map(lambda x: x['World Population Percentage'], df))
  charts.generate_pie_chart(countries,percentages)

  country = input('Type Country => ')
  
  result = utils.population_by_country(df, country)
  
  if len(result) > 0:
    country = result[0]
    #print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
 
if __name__ == '__main__':
  run()