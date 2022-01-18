# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:33:17 2022

@author: vanaa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


colors=['mediumpurple', 'cornflowerblue', 'lightgreen', 'palegoldenrod']

#wczytanie i czyszczenie
data=pd.read_csv('Placement_Data_Full_Class.csv', encoding='Latin1')
data=data.drop_duplicates() #delete duplicates
data.info()
data_correlation=data.corr()

#podzbiory
data_F=data[data.gender=='F'] #df for female only
data_M=data[data.gender=='M'] #df for male only
nan_salary=data.salary.isnull()
data_sal=data[~nan_salary] #df bez wierszy gdzie nie ma salary
workex_yes=data[data.workex=='Yes']
workex_no=data[data.workex=='No']
data_other = data_sal[data_sal.degree_t =='Others']
data_comm = data_sal[data_sal.degree_t =='Comm&Mgmt']
data_scien = data_sal[data_sal.degree_t =='Sci&Tech']
workex_yes_sal=data_sal[data_sal.workex=='Yes']
workex_no_sal=data_sal[data_sal.workex=='No']

#pie charts
degree_t_v=data.degree_t.value_counts()
degree_t_names=list(degree_t_v.index)
fig=plt.figure(figsize=(10,6))
plt.pie(degree_t_v, labels=degree_t_names, textprops={'fontsize': 16}, colors=colors, autopct ='%1.1f%%')
plt.savefig('pie_chart_degree_t.png', dpi=150)
plt.show()

degree_t_yes=workex_yes.degree_t.value_counts()
plt.pie(degree_t_yes, labels=degree_t_names,textprops={'fontsize': 12}, colors=colors, autopct ='%1.1f%%')
plt.savefig('pie_chart_degree_t_yes.png', dpi=150)
plt.show()

degree_t_no=workex_no.degree_t.value_counts()
plt.pie(degree_t_no, labels=degree_t_names,textprops={'fontsize': 12}, colors=colors, autopct ='%1.1f%%')
plt.savefig('pie_chart_degree_t_no.png', dpi=150)
plt.show()

workex_v=data.workex.value_counts()
workex_names=list(workex_v.index)
plt.pie(workex_v, labels=workex_names ,textprops={'fontsize': 12}, colors=colors, autopct ='%1.1f%%')
plt.savefig('pie_chart_workex.png', dpi=150)
plt.show()

gender_v=data.gender.value_counts()
gender_names=list(gender_v.index)
plt.pie(gender_v, labels=gender_names, textprops={'fontsize': 12}, colors=colors, autopct ='%1.1f%%')
plt.savefig('pie_chart_g.png', dpi=150)
plt.show()

#boxplot wyniki magisterki dla osób z doświadczeniem i bez

plt.boxplot([workex_yes['mba_p'],workex_no['mba_p']],)
plt.xticks([1,2],['tak','nie'])
plt.xlabel('doświadczenie zawodowe [tak/nie]')
plt.ylabel('studia drugiego stopnia - wynik końcowy [%]')
plt.savefig('boxplot_mba_p_worke.png',dpi=150)
plt.show()

#scatterplot dla etapów edukacji
plt.scatter(data['ssc_p'], data['hsc_p'], c=data['degree_p'], alpha=0.5)
cbar=plt.colorbar()
cbar.set_label('studia pierwszego stopnia - wynik końcowy [%]')
plt.xlabel('edukacja podstawowa - wynik końcowy [%]')
plt.ylabel('edukacja średnia - wynik końcowy [%]')
plt.savefig('scatter_plot_hsc_ssc_degree_p.png', dpi=150)
plt.show()

#scatterplot mężczyźni
plt.scatter(data_M['ssc_p'], data_M['hsc_p'], c=data_M['degree_p'], alpha=0.5)
cbar=plt.colorbar()
cbar.set_label('studia pierwszego stopnia - wynik końcowy [%]')
plt.xlabel('edukacja podstawowa - wynik końcowy [%]')
plt.ylabel('edukacja średnia - wynik końcowy [%]')
plt.savefig('scatter_plot_M.png', dpi=150)
plt.show()

#scatterplot kobiety
plt.scatter(data_F['ssc_p'], data_F['hsc_p'], c=data_F['degree_p'], alpha=0.5)
cbar=plt.colorbar()
cbar.set_label('studia pierwszego stopnia - wynik końcowy [%]')
plt.xlabel('edukacja podstawowa - wynik końcowy [%]')
plt.ylabel('edukacja średnia - wynik końcowy [%]')
plt.savefig('scatter_plot_F.png', dpi=150)
plt.show()

#tabele edukacja
#wykształcenie podstawowe
ssc_p_f=data_F.ssc_p.describe()#dla kobiet
ssc_p_f_mode=data_F.ssc_p.mode()
ssc_p_f
ssc_p_f_mode

ssc_p_m=data_M.ssc_p.describe()#dla mężczyzn
ssc_p_m_mode=data_M.ssc_p.mode()
ssc_p_m
ssc_p_m_mode

ssc_p_g=data.ssc_p.describe()#dla wszytskich
ssc_p_g_mode=data.ssc_p.mode()
ssc_p_g
ssc_p_g_mode

#wykształcenie srednie
hsc_p_f=data_F.hsc_p.describe()#dla kobiet
hsc_p_f_mode=data_F.hsc_p.mode()
hsc_p_f
hsc_p_f_mode

hsc_p_m=data_M.hsc_p.describe()#dla mężczyzn
hsc_p_m_mode=data_M.hsc_p.mode()
hsc_p_m
hsc_p_m_mode

hsc_p_g=data.hsc_p.describe()#dla wszytskich
hsc_p_g_mode=data.hsc_p.mode()
hsc_p_g
hsc_p_g_mode


#studia pierwszy stopien
degree_p_f=data_F.degree_p.describe() #dla kobiet
degree_p_f_mode=data_F.degree_p.mode()
degree_p_f
degree_p_f_mode

degree_p_m=data_M.degree_p.describe()#dla mężczyzn
degree_p_m_mode=data_M.degree_p.mode()
degree_p_m
degree_p_m_mode

degree_p_g=data.degree_p.describe()#dla wszytskich
degree_p_g_mode=data.degree_p.mode()
degree_p_g
degree_p_g_mode

#studia drugiego stopnia
mba_p_f=data_F.mba_p.describe() #dla kobiet
mba_p_f_mode=data_F.mba_p.mode()
mba_p_f
mba_p_f_mode

mba_p_m=data_M.mba_p.describe()#dla mężczyzn
mba_p_m_mode=data_M.mba_p.mode()
mba_p_m
mba_p_m_mode

mba_p_g=data.mba_p.describe()#dla wszystkich
mba_p_g_mode=data.mba_p.mode()
mba_p_g
mba_p_g_mode

#tabele kierunki
#other
other_av =data_other['salary'].mean()
other_med = data_other['salary'].median()
other_mode = data_other['salary'].mode()
other_sss = pd.Series(data_other['salary'])
other_sd = other_sss.std()

#comm
comm_av = data_comm['salary'].mean()
comm_med = data_comm['salary'].median()
comm_mode = data_comm['salary'].mode()
comm_sss = pd.Series(data_comm['salary'])
comm_sd = comm_sss.std()

#science
scien_av = data_scien['salary'].mean()
scien_med = data_scien['salary'].median()
scien_mode = data_scien['salary'].mode()
scien_sss = pd.Series(data_scien['salary'])
scien_sd = scien_sss.std()

#for workex_yes salary
yes_sal_av = workex_yes['salary'].mean()
yes_sal_med = workex_yes['salary'].median()
yes_sal_mod = workex_yes['salary'].mode()
yes_sal_sss = pd.Series(workex_yes['salary'])
yes_sal_sd = yes_sal_sss.std()

#for workex_no salary
no_sal_av = workex_no['salary'].mean()
no_sal_med = workex_no['salary'].median()
no_sal_mod = workex_no['salary'].mode()
no_sal_sss = pd.Series(workex_no['salary'])
no_sal_sd = no_sal_sss.std()

#for workex_yes employability
yes_emp_av = workex_yes['etest_p'].mean()
yes_emp_med = workex_yes['etest_p'].median()
yes_emp_mod = workex_yes['etest_p'].mode()
yes_emp_sss = pd.Series(workex_yes['etest_p'])
yes_emp_sd = yes_emp_sss.std()

#for workex_no employability
no_emp_av = workex_no['etest_p'].mean()
no_emp_med = workex_no['etest_p'].median()
no_emp_mod = workex_no['etest_p'].mode()
no_emp_sss = pd.Series(workex_no['etest_p'])
no_emp_sd = no_emp_sss.std()

#specialisation
data_specfin = data_sal[data_sal.specialisation =='Mkt&Fin']
data_spechr = data_sal[data_sal.specialisation =='Mkt&HR']

specfin_av =data_specfin['salary'].mean()
specfin_med = data_specfin['salary'].median()
specfin_mode = data_specfin['salary'].mode()
specfin_sss = pd.Series(data_specfin['salary'])
specfin_sd = specfin_sss.std()

spechr_av =data_spechr['salary'].mean()
spechr_med = data_spechr['salary'].median()
spechr_mode = data_spechr['salary'].mode()
spechr_sss = pd.Series(data_spechr['salary'])
spechr_sd = spechr_sss.std()
