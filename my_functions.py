import matplotlib.pyplot as plt
import seaborn as sns

def vc_hist(data, x):
    plt.figure(figsize=(10,6), dpi=80)

    ax = sns.countplot(data = data, x = x, hue = x)

    #Just wanted to put in the count values on top of each bar so as to better interpret the data for ease of interpretability. This is all done in 1000s points for fit.
    for axi in ax.patches:
        height = axi.get_height()
        ax.text(axi.get_x()+axi.get_width()/2.,
                height + 3,
                f'{round(axi.get_height() / 1000, 1)}K',
                ha="center")

    #rotate labels for no overlap     
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=45, ha = "right", x = -0.1)

    plt.show()
    plt.close()