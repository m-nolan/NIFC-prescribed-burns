import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DPI = 150
FIG_SIZE = (10,4)
DATA_DIR = './data/'
FIG_DIR = './figures/'
KEY_LIST = ['BIA','BLM','USFS','FWS','NPS','State/Other']

def load_data( data_dir=DATA_DIR ):
    fires_df = pd.read_csv(os.path.join(data_dir,'fires.csv'))
    acres_df = pd.read_csv(os.path.join(data_dir,'acres.csv'))
    return fires_df, acres_df

def plot_nifc_dataframe( df, key_list=KEY_LIST, dpi=DPI, fig_size=FIG_SIZE ):
    sort_idx = np.argsort(df['Year'])
    fig, ax = plt.subplots(1,2,dpi=dpi,figsize=fig_size,constrained_layout=True)
    for key in key_list:
        ax[0].plot(df['Year'][sort_idx],df[key][sort_idx],label=key)
    ax[0].set_xlim(1,22)
    ax[0].set_yscale('log')
    ax[0].legend(loc=0)
    ax[0].set_xticklabels(df['Year'][sort_idx],rotation=90)
    ax[0].set_xlabel('Year')
    ax[1].plot(df['Year'][sort_idx],df['Total'][sort_idx],label='Total')
    ax[1].set_xlim(1,22)
    ax[1].set_yscale('log')
    ax[1].legend(loc=0)
    ax[1].set_xticklabels(df['Year'][sort_idx],rotation=90)
    ax[1].set_xlabel('Year')
    return fig, ax

def plot_fires( fires_df ):
    fig, ax = plot_nifc_dataframe(fires_df)
    ax[0].set_ylabel('Num. of Presc. Burns')
    ax[0].set_title('Burns per Agency')
    ax[1].set_title('Burns, Total')
    fig.suptitle('Number of Prescribed Burns per Year, 1998-2019')
    return fig

def plot_acres( acres_df ):
    fig, ax = plot_nifc_dataframe(acres_df)
    ax[0].set_ylabel('Area of Presc. Burns (acres)')
    ax[0].set_title('Area per Agency')
    ax[1].set_title('Area, Total')
    fig.suptitle('Area of Prescribed Burns per Year, 1998-2019')
    return fig

def save_figures( fires_fig, acres_fig, fig_dir=FIG_DIR ):
    if not os.path.exists(fig_dir):
        os.makedirs(fig_dir)
    fires_fig.savefig(os.path.join(fig_dir,'fires.png'))
    acres_fig.savefig(os.path.join(fig_dir,'acres.png'))

def main():
    fires_df, acres_df = load_data()
    fires_fig = plot_fires(fires_df)
    acres_fig = plot_acres(acres_df)
    save_figures(fires_fig,acres_fig)

if __name__ == "__main__":
    main()