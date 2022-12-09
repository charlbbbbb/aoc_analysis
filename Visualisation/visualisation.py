import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def get_percentage_of_part_2():
    df = pd.read_excel('/Users/charliebrowning/PycharmProjects/aoc_analysis/aoc_star_data.xlsx')
    df['Percentage'] = (df['Part2']/df['Part1'])*100

    palette = sns.color_palette()[:7]
    plt.figure(figsize=(14, 8))
    plt.xticks(df['Day'])
    sns.lineplot(data=df, x='Day', y='Percentage', hue='Year', palette=palette, marker='o')
    plt.axhline(df['Percentage'].mean(), linestyle='--', color='black')
    plt.text(x=26.3, y=df['Percentage'].mean()-1, s=f"Mean={round(df['Percentage'].mean(), 0)}%",
             fontdict={
              'size': 12,
             'style': 'italic',
             'weight': 'bold'})
    plt.title(r"$\bf{Percentage}$"' of People Who Completed '+r"$\bf{Part}$ $\bf{1}$"+' but Failed to Complete '+r"$\bf{Part}$ $\bf{2}$")
    plt.tight_layout()
    plt.savefig('part1_vs_part2.JPEG')


get_percentage_of_part_2()