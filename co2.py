from matplotlib import pyplot as plt

def extract_data(extract):
    if len(extract)>3:
            print('ERR: Sorry, at most 3 countries can be entered')
            return False
    else:
        new_data={}
        new_data['CO2 per capita']=scan_file['CO2 per capita']
        data = open('C:/Users/lenovo/Desktop/python/projects/CO2 emission/Emissions_subset.csv','w')
        for countries in extract:
            countries = countries.capitalize()
            if countries not in scan_file.keys():
                print(f"ERR: Sorry “{countries}” is not a valid country", end="\n\n")
            else:
                new_data[countries]=scan_file[countries]
        for key,value in new_data.items():
            string = ','.join(value)
            data.write('%s,%s\n' % (key, string))
        data.close()
        print(f"Data successfully extracted for countries " + ", ".join(
            extract).title() + " saved into file Emissions_subset.csv", end="\n\n")
    return True

print("A Simple Data Analysis Program")
print()
try:
    scan_file = {}
    file_handle= open('C:/Users/lenovo/Desktop/python/projects/CO2 emission/Emissions.csv','r')
    for row in file_handle:
        scan_file[row.strip().split(',')[0]]=row.strip().split(',')[1:]
    print("All data from Emissions.csv has been read into a dictionary.\n")
    
    year_value=scan_file['CO2 per capita']
    while True:
        year = input(f'Select a year to find statistics ({year_value[0]} to {year_value[-1]}): ')
        if year not in year_value:
            print("Sorry that is not a valid year.")
            continue
        else:
            break
    
    index = scan_file['CO2 per capita'].index(year)
    
    list_of_emission = [float(emission[index]) for emission in scan_file.values()][1:]
    
    minimum_co2,maximum_co2= min(list_of_emission) ,max(list_of_emission)
    average = round(sum(list_of_emission)/len(list_of_emission),6)
    
    country_with_minimum_co2_index=list_of_emission.index(minimum_co2)
    country_with_maximum_co2_index=list_of_emission.index(maximum_co2)
    
    country_with_minimum_co2=list(scan_file.keys())[1:][country_with_minimum_co2_index]
    country_with_maximum_co2=list(scan_file.keys())[1:][country_with_maximum_co2_index]
    
    print(f'In {year}, countries with minimum and maximum CO2 emission levels were: [{country_with_minimum_co2}] and [{country_with_maximum_co2}] respectively.\nAverage CO2 emissions in {year} were {average}')

    while True:
        country_input=input('\nSelect country to visualize: ').title()
        if country_input in scan_file.keys():
            years_of_emission=list(map(int, list(scan_file.values())[0]))
            plt.title('Year vs Emissions in Capita')
            plt.xlabel('Year')
            plt.ylabel('Emissions in' + country_input)
            plt.plot(years_of_emission, list(map(float,list(scan_file[country_input]))))
            plt.show()
            break
        else:
            print("Sorry that is not a valid Country.")
            continue
    while True:
        try:
            country1,country2 = input("Write two comma-seperated coutries for which you want to visualize data: ").title().split(',')
        except ValueError:
            print("Please write up to two comma-separated countries for which you want to visualize data...")
            continue
        if country1 not in scan_file.keys() or country2 not in scan_file.keys():
            print("Sorry that is not a valid Country.")
            continue
        else:
            years_of_emission=list(map(int, list(scan_file.values())[0]))
            plt.title('Year vs Emissions in Capita')
            plt.xlabel('Year')
            plt.ylabel('Emissions in')
            plt.plot(years_of_emission, list(map(float,list(scan_file[country1]))),color='tab:blue',label=country1)
            plt.plot(years_of_emission, list(map(float,list(scan_file[country2]))),color='tab:orange',label=country2)
            plt.legend()
            plt.show()
            break
    while True:
        extract=input("Write up to three comma-seperated coutries for which you want to extract data: ").capitalize().split(',')
        if not extract_data(extract):
            continue
        else:
            break
        
except FileNotFoundError:
    print("File not found....")
except IOError:
    print("Output file can’t be saved")
    
