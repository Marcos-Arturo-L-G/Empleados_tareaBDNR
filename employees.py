
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Empleados')

st.subheader('Integrantes: Marcos Arturo Lopez Gonzalez')
st.subheader('Jose Obed Mariano Hipolito')

st.write ("App que analiza los datos del csv employees")

barra = st.sidebar
barra.title("Opciones")

DATA_URL = ('https://raw.githubusercontent.com/Marcos-Arturo-L-G/Empleados_tareaBDNR/master/Employees.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, encoding_errors='ignore')
    return data

data = load_data(1000)

TodosDat = barra.checkbox("Mostrar todos los datos ",key ="Dataframe")
if TodosDat:
  data = load_data(1000)
  st.text('Todos los datos:')
  st.dataframe(data)

@st.cache
def load_data_byEmployeesID(id):
  filtered_data_byID = data[data['Employee_ID'].str.contains(id)]
  return filtered_data_byID

@st.cache
def load_data_byHometown(hometown):
  filtered_data_byHome = data[data['Hometown'].str.contains(hometown)]
  return filtered_data_byHome

@st.cache
def load_data_byUnit(unit):
  filtered_data_byUnit = data[data['Unit'].str.contains(unit)]
  return filtered_data_byUnit

IDHomeUnit = barra.text_input('Ingrese el id o ciudad o el trabajo: ')
btnFilteredID = barra.button('Buscar por ID')
btnFilteredHometown = barra.button('Buscar por Ciudad natal')
btnFilteredUnit = barra.button('Buscar por Trabajo')

if (btnFilteredID):
  st.write ("ID buscado: " + IDHomeUnit)
  filterbyID = load_data_byEmployeesID(IDHomeUnit)
  count_row = filterbyID.shape[0]
  st.write(f'Total: {count_row}')
  st.dataframe(filterbyID)

if (btnFilteredHometown):
  st.write ("Ciudad buscada: " + IDHomeUnit)
  filterbyHome = load_data_byHometown(IDHomeUnit)
  count_row = filterbyHome.shape[0]
  st.write(f'Total: {count_row}')
  st.dataframe(filterbyHome)

if (btnFilteredUnit):
  st.write ("Trabajo buscado: "+ IDHomeUnit)
  filterbyUnit = load_data_byUnit(IDHomeUnit)
  count_row = filterbyUnit.shape[0]
  st.write(f'Total: {count_row}')
  st.dataframe(filterbyUnit)

@st.cache
def load_data_bydire(level):
  filtered_data_byLevel = data[data['Education_Level'] == level]
  return filtered_data_byLevel

EducationLevel = barra.selectbox("Selecciona el Nivel educativo", data['Education_Level'].unique())
btnFilterByLevel = barra.button('Filtrar por Nivel educativo')

if (btnFilterByLevel): 
  st.write("Empleados con nivel educativo "+ str(EducationLevel))
  filterbylevel = load_data_bydire(EducationLevel)
  count_row = filterbylevel.shape[0]
  st.write(f'Total: {count_row}')
  st.dataframe(filterbylevel)

@st.cache
def load_data_byhome(home):
  filtered_data_byHome = data[data['Hometown'] == home]
  return filtered_data_byHome

selectedHome = barra.selectbox("Selecciona la ciudad natal", data['Hometown'].unique())
btnFilterByHometown = barra.button('Filtrar por Ciudad')

if (btnFilterByHometown): 
  st.write("Empleados con Ciudad natal "+ str(selectedHome))
  filterbyHome = load_data_byhome(selectedHome)
  count_row = filterbyHome.shape[0]
  st.write(f'Total: {count_row}')
  st.dataframe(filterbyHome)

selectedUnit = barra.selectbox("Selecciona el trabajo", data['Unit'].unique())
btnFilterByUnit = barra.button('Filtrar por Trabajo')

if (btnFilterByUnit): 
  st.write("Empleados con el trabajo "+ str(selectedUnit))
  filterbyUnit = load_data_byUnit(selectedUnit)
  count_row = filterbyUnit.shape[0]
  st.write(f'Total: {count_row}')
  st.dataframe(filterbyUnit)

grafEdades = barra.checkbox("Histograma de edades ",key = "edades")

if grafEdades:
  fig, ax = plt.subplots()
  ax.hist(data['Age'])
  ax.set_xlabel("Edad")
  ax.set_ylabel("Numero de empleados")
  st.header("Histograma de empleados por edad")
  st.pyplot(fig)

grafFrec = barra.checkbox("Frecuencia por trabajo ",key = "frecuencia")

if grafFrec:
  fig, ax = plt.subplots()
  ax.hist(data['Unit'])
  ax.set_xlabel("Trabajo")
  ax.set_ylabel("Numero de empleados")
  st.header("Frecuencia de Empleados por Trabajo ")
  plt.setp(ax.get_xticklabels(), rotation=45, ha='right')#checar
  st.pyplot(fig)

grafDescercion = barra.checkbox("Indice de deserción por ciudad ",key = "desercion")

if grafDescercion:
  fig, ax = plt.subplots()
  y_pos = data['Attrition_rate']
  x_pos = data['Hometown']
  ax.bar(x_pos, y_pos)
  ax.set_ylabel("Desercion")
  ax.set_xlabel("Ciudad natal")
  ax.set_title('empleados que desertaron por ciudad')
  st.header("Indice de deserción por ciudad")
  st.pyplot(fig)

grafEdadDes = barra.checkbox("Indice de deserción por edad ", key = "desEdad")

if grafEdadDes:
  fig, ax = plt.subplots()
  y_pos = data['Attrition_rate']
  x_pos = data['Age']
  ax.barh(x_pos, y_pos)
  ax.set_xlabel("Desercion")
  ax.set_ylabel("Edad")
  ax.set_title('empleados que desertaron por edad')
  st.header("Indice de deserción por edad")
  st.pyplot(fig)

grafTime = barra.checkbox("Indice de deserción por Tiempo de servicio ",key = "service")

if grafTime:
  fig, ax = plt.subplots()
  y_pos = data['Attrition_rate']
  x_pos = data['Time_of_service']
  ax.bar(x_pos, y_pos)
  ax.set_ylabel("Desercion")
  ax.set_xlabel("Tiempo de servicio")
  ax.set_title('¿Cuantos empleados desertaron por tiempo de servicio?')
  st.header("Indice de deserción por tiempo de servicio")
  st.pyplot(fig)