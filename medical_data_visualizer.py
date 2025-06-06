import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x:1 if x >25 else 0)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)


# 4 
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars =['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])

    df_cat['total'] = 1
    # 6
    df_cat = df_cat.groupby(["cardio","variable","value"],as_index=False).count()
    

    # 7
    fig= sns.catplot(x='variable', y='total', hue='value', kind='bar', data= df_cat, col='cardio').fig


    # 8
    #fig = g.get_figure()


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <=df['ap_hi'])&
                (df['height'] >= df['height'].quantile(0.025)) &
                (df['height'] <= df['height'].quantile(0.975)) &
                (df['weight'] >= df['weight'].quantile(0.025)) &
                (df['weight'] <= df['weight'].quantile(0.975))
               ]

    # 12
    corr = df_heat.corr(method ="pearson")

    # 13
    mask = np.triu(corr)




    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    sns.heatmap(corr, linewidths=1, annot=True, square = True, mask = mask, fmt = '.1f', cbar_kws={"shrink": .5}, center = 0.00)



    # 16
    fig.savefig('heatmap.png')
    return fig
