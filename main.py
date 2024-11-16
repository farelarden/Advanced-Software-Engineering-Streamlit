
# currentWorkingDirectory = "C:\\(...)\\project1"
# #currentWorkingDirectory = "/mount/src/berlingeoheatmap1/"

# # -----------------------------------------------------------------------------
# import os
# os.chdir(currentWorkingDirectory)
# print("Current working directory\n" + os.getcwd())

import pandas                        as pd
from core import methods             as m1
from core import HelperTools         as ht

from config                          import pdict

# -----------------------------------------------------------------------------
@ht.timer
def main():
    """Main: Generation of Streamlit App for visualizing electric charging stations & residents in Berlin"""

    df_geodat_plz   = pd.read_csv("datasets/geodata_berlin_plz.csv", sep=';')
    
    df_lstat = pd.read_excel("datasets/downloaded_datasets/Ladesaeulenregister_SEP.xlsx", header=10)
    # df_lstat2       = pd.read_csv("datasets\downloaded_datasets\Ladesaeulenregister_SEP.xlsx")
    # gdf_lstat3      = pd.read_csv("datasets\downloaded_datasets\Ladesaeulenregister.csv")
    
    df_residents    = pd.read_csv("datasets/downloaded_datasets\plz_einwohner.csv")
    # pd.read_csv("datasets\downloaded_datasets\Ladesaeulenregister_SEP.xlsx") #I'm not sure
    gdf_residents2  = pd.read_csv("datasets/geodata_berlin_dis.csv", sep=';')
    
# -----------------------------------------------------------------------------------------------------------------------

    #


if __name__ == "__main__": 
    main()

