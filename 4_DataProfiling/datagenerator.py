from matplotlib import pyplot as plt
import random


class DataGenerator:

    def __init__(self, count_points) -> None:
        self.count_points = count_points
        self.x = None 
        self.y_data = None 

    def do_all_things(self, save_file = False):
        self.data_generate()
        self.plot_data()

        if save_file:
            self.write_report() 

    def data_generate(self):

        self.x = list(range(self.count_points))

        self.y_data = [random.randint(-5, 5) for _ in range(self.count_points)]
        self.y_data = [sum(self.y_data[:i+1]) for i in range(len(self.y_data))]
       

    def plot_data(self):

        # 1. Create a figure (Window)
        fig = plt.figure() 

        # 2. Create a draw area (subplot)
        ax = fig.add_subplot(111)

        # 2. Create a draw area (subplot)
        # fig, ax = plt.subplots() Vereinfachte Version?

        ax.plot(self.x, self.y_data, label = "Aktien")

        # Plot Configuration 
        ax.legend()
        ax.grid(True)
        ax.set_title("Random Aktienbewegung")
        ax.set_xlabel("Tage")
        ax.set_ylabel("Wert in €")

        plt.savefig("./aktien.png")

        # Show the plot 
        plt.show()


    def write_report(self):
        with open("./report.txt", mode = "w", encoding= "UTF-8") as file:
            file.write("Hallo Mohamed")