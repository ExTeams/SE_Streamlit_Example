import streamlit as st


def create_list(lines):
    names = []
    ages = []
    for line in lines:
        data = line.split(',')
        save = data[1]
        if save == '1' and data[6] != '':
            name = (data[3] + data[4])[1:-1]
            age = float(data[6])
            names.append(name)
            ages.append(age)
    passengers = {'Имя': names, 'Возраст': ages}
    return passengers


def do_work():
    with open("data.csv") as file:
        passengers = create_list(file.readlines())
    st.dataframe(passengers)
