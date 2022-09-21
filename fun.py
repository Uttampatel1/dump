"""
Create a pie chart showing "code"  as 5%  and "everything" else as 95%
"""


import matplotlib.pyplot as plt


def main():
    slices = [5, 95]
    activities = ['code', 'everything else']
    cols = ['c', 'm']

    plt.pie(slices,
            labels=activities,
            colors=cols,
            startangle=90,
            shadow=True,
            explode=(0, 0.1),
            autopct='%1.1f%%')

    plt.title('Pie Chart')
    plt.show()

main()