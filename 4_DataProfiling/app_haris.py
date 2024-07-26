import os
from pathlib import Path
from datagenerator import DataGenerator


os.chdir(Path(__file__).parent)


def main():
    
    data_chart1 = DataGenerator(400) 
    data_chart1.do_all_things(save_file=True)

    data_chart2 = DataGenerator(7000)
    data_chart2.do_all_things()


if __name__ == "__main__":
    main()
