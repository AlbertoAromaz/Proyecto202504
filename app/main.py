import utils
import read_csv
import charts

def run():
  df = read_csv.read_csv('data.csv')
  df = list(filter(lambda item : item['Continent'] == 'South America', df))

  countries = list(map(lambda x: x['Country'], df))
  percentages = list(map(lambda x: x['World Population Percentage'], df))
  charts.generate_pie_chart(countries,percentages)

  country = input('Type Country => ')
  #print(country)
  
  result = utils.population_by_country(df, country)
  
  if len(result) > 0:
    country = result[0]
    #print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)
 
if __name__ == '__main__':
  run()