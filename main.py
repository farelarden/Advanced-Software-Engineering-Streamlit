
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
from core.methods import sort_by_plz_add_geometry, preprop_lstat, count_plz_occurrences,preprop_resid, make_streamlit_electric_Charging_resid 

# -----------------------------------------------------------------------------
@ht.timer
def main():
    """Main: Generation of Streamlit App for visualizing electric charging stations & residents in Berlin"""

    df_geodat_plz   = pd.read_csv("datasets/geodata_berlin_plz.csv", sep=';')
    
    # df_lstat = pd.read_excel("datasets/downloaded_datasets/Ladesaeulenregister_SEP.xlsx", header=10)
    df_lstat2       = pd.read_excel("datasets/downloaded_datasets/Ladesaeulenregister_SEP.xlsx", header=10)
    # gdf_lstat3      = pd.read_csv("datasets\downloaded_datasets\Ladesaeulenregister.csv")
    
    df_residents    = pd.read_csv("datasets/downloaded_datasets/plz_einwohner.csv")
    # pd.read_csv("datasets\downloaded_datasets\Ladesaeulenregister_SEP.xlsx") #I'm not sure
    gdf_residents2  = pd.read_csv("datasets/geodata_berlin_dis.csv", sep=';')

    res_1 = preprop_lstat(df_lstat, df_geodat_plz, pdict)
    res_2 = count_plz_occurrences(res_1)
    res_3 = preprop_resid(df_residents, df_geodat_plz, pdict)
    res_4 = make_streamlit_electric_Charging_resid(res_2, res_3)

# -----------------------------------------------------------------------------------------------------------------------

    #


if __name__ == "__main__": 
    main()

