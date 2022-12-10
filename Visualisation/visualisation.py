import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def get_percentage_of_part_2():
    df = pd.read_excel('/Users/charliebrowning/PycharmProjects/aoc_analysis/aoc_star_data.xlsx')
    df['Overall'] = df['Part1'] + df['Part2']
    df['Percentage'] = (df['Part2']/df['Overall'])*100

    palette = sns.color_palette()[:7]
    plt.figure(figsize=(14, 8))
    plt.xticks(df['Day'])
    sns.lineplot(data=df, x='Day', y='Percentage', hue='Year', palette=palette, marker='o', sort='Year')
    plt.axhline(df['Percentage'].mean(), linestyle='--', color='black')
    plt.text(x=26.3, y=df['Percentage'].mean()-1, s=f"Mean={round(df['Percentage'].mean(), 0)}%",
             fontdict={
              'size': 12,
             'style': 'italic',
             'weight': 'bold'})
    plt.title(r"$\bf{Percentage}$"' of People Who Completed '+r"$\bf{Part}$ $\bf{1}$"+' but Failed to Complete '+r"$\bf{Part}$ $\bf{2}$")
    plt.tight_layout()
    plt.savefig('part1_vs_part2.JPEG')


def overall_users():
    df = pd.read_excel('/Users/charliebrowning/PycharmProjects/aoc_analysis/aoc_star_data.xlsx')
    df['Overall'] = df['Part1'] + df['Part2']
    for year in list(dict.fromkeys(list(df['Year']))):
        temp_df = df[df['Year'] == year]
        sns.barplot(data=temp_df, y='Day', x='Overall', color='blue', orient='h')
        plt.title("Overall Users Per Day " + fr"$\bf{year}$")
        plt.grid(axis='x')
        plt.savefig(f"{year}_overall_users.JPEG")
        plt.clf()


def overall_percentage_change_in_users():
    df = pd.read_excel('/Users/charliebrowning/PycharmProjects/aoc_analysis/aoc_star_data.xlsx')
    df['Overall'] = df['Part1'] + df['Part2']
    for year in list(dict.fromkeys(list(df['Year']))):
        temp_df = df[df['Year'] == year]
        temp_df = temp_df.reset_index()
        change = []
        for i in range(len(temp_df['Overall'][:-1])):
            change.append(-(((temp_df['Overall'][i + 1] / temp_df['Overall'][i])-1) * 100))
        change.append(0)
        temp_df['Change'] = change
        plt.figure(figsize=(14, 8))
        sns.lineplot(data=temp_df, x='Day', y='Change', color='blue')
        plt.title("Overall Users Per Day " + fr"$\bf{year}$")
        plt.grid(axis='y')
        for record in range(len(temp_df)):
            if temp_df['Change'][record] == max(temp_df['Change']):
                highest = f"Largest Change: Day {temp_df['Day'][record]}={round(temp_df['Change'][record], 0)}%"
        plt.text(x=19, y=max(temp_df['Change']), s=f"{highest}\n*largest change usually represents the \nday after a difficult challenger", fontdict={'weight': 'bold',
                                                                        'size': 10})
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.xticks(df['Day'])
        plt.tight_layout()
        plt.savefig(f"{year}_percentage_change_users.JPEG")
        plt.clf()


overall_percentage_change_in_users()