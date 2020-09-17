import pandas as pd
import numpy as np
import scipy.spatial.distance as pi

def recom_correlation_st_lim (bed,fbath,garage,zip_code,living_area,built_year,predicted_price,datosRecomendador):
    # parámetros sobre los que se calcula la semejanza de items
    col=['Beds','FBaths','Garage_Spaces','Zip_Code',
          'SqFt_Liv_Area','Year_Built','Sale_Price']
    dat=datosRecomendador[col]
    # variable auxiliar
    valor=[]
    # Parametros de estandarizacion del Sale_Price
    media=dat['Sale_Price'].mean() # media de variable
    dt=dat['Sale_Price'].std() # desviación tipoica 
    
    # nueva variable estandarizada
    dat['Sale_Price_st']=(dat['Sale_Price']-media)/dt
    
    # Ejemplo de x=[1,1,0,33166, 710,1986,160000]
    x = [bed, fbath, garage, zip_code, living_area, built_year, predicted_price] # valor de prediction hay que añadirlo
    
    # estandarizo la variable de precio en el vector de entrada
    x[-1]=(x[-1]-media)/dt
    
    # nuevo rango de columnas (tengo 1 dim mas en dat)
    col_st=['Beds','FBaths','Garage_Spaces','Zip_Code',
          'SqFt_Liv_Area','Year_Built','Sale_Price_st']
    
    # calculo de la distancia
    for i in range(len(dat)):
        c=pi.correlation(x,list(dat.iloc[i][col_st]))
        valor.append(c)
    
    # Creo la nueva columna en la matriz de apoyo
    dat['metric']=valor
    # filtro de Zip_code
    condicion_zip= dat['Zip_Code']==x[3]
    
    
    # condicion de proximidad
    limite=np.percentile(dat['metric'],25)
    condicion_limite=dat['metric']<limite
    
    # filtro los valores
    dat_2=dat[condicion_zip & condicion_limite]
    
    # recojo en un nuevo dataframe los mejores items ordenados
    salida=dat_2.sort_values(by='metric',ascending=True)[:10][col]
    
    # calculo el rango de oscilacion de precios
    max=salida['Sale_Price'].max()
    min=salida['Sale_Price'].min()
    rango=[min,max]
    rango_pct=[min/predicted_price-1, max/predicted_price-1]
    
    
    #print('el rango de oscilacion es ',rango, rango_pct)      
    return salida.head(5) #





