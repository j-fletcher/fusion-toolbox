import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Shot:
    """Shot class to store data from a shot.
    
    Parameters
    ----------
    path : string
        Path to the shot data file.

    """
    def __init__(self, path: str=None):
        self.path = path # Path to the shot data file
        self.data = {} # Dictionary of signals. Each signal is a dictionary with keys "time" and "value"
        self.tokamak = None
        self.shot_id = None
        self.events = {}

        # Load data from csv if path is given
        if path is not None:
            self.from_csv(path)
        
    @classmethod
    def from_csv(path: str, self):
        """Loads the data of a shot from the database into shot object.

        Parameters
        ----------
        path : string
            Path to the shot data file.

        Example
        --------
        >>> my_shot = Shot()
        >>> my_shot.from_csv("shots/shot_2023010101.csv")

        """
        
        df = pd.read_csv(path)
        self.path = path
        if 'time' not in df.columns:
            print('Warning: no time column found in shot data. Creating dummy time column.')
            df["time"] = np.arange(len(df))

        for column in df.columns:
            if column=="time":
                continue
            self.data[column] = {"time": df["time"], "value": df[column]}
        
        try:
            self.shot_id = self.data["shot_id"]
        except:
            try:
                self.shot_id = self.data["shot"]
            except:
                pass
        try:
            self.device = self.data["tokamak"]
        except:
            pass
        self.signals = df.columns

    def compute_flattop_current(self):
        pass


def plot_shot(shot: Shot, signal: str, **kwargs):
    """Plots a signal from a shot object.

    Parameters
    ----------
    shot : Shot
        Shot object.
    signal : str
        Name of the signal to plot.
    **kwargs : dict
        Keyword arguments to pass to matplotlib.pyplot.plot.

    Returns
    -------
    matplotlib.plot object

    Example
    -------
    >>> my_shot = Shot(path="shots/shot_2023010101.csv")
    >>> fig, axs = plt.subplots(ncols=1, nrows=2, sharex=True)
    >>> plt.sca(axs[0])
    >>> axs[0].set_ylim([0,2000])
    >>> plot_shot(my_shot, "Plasma_Current (A)", color="tab:red")
    >>> plt.sca(axs[1])
    >>> plot_shot(my_shot, "Plasma_Density (particlesm3)")
    >>> plt.show()


    """
    return plt.plot(shot.data[signal]["time"], shot.data[signal]["value"], **kwargs)

def plot_standard_shot(shots: list):
    """Plots a standard set of signals from a list of shots.

    Parameters
    ----------
    shots : list
        List of Shot objects.

    Returns
    -------
    fig, axs : matplotlib.pyplot.subplots object

    Example
    -------
    >>> my_shot = Shot(path="shots/shot_2023010101.csv")
    >>> my_shot2 = Shot(path="shots/shot_2023010102.csv")
    >>> fig, axs = plot_standard_shot([my_shot,my_shot2])
    >>> plt.show()

    """

    fig, axs = plt.subplots(ncols=1, nrows=2, sharex=True)
    for shot in shots:
        plt.sca(axs[0])
        plot_shot(shot, "Plasma_Current (A)", label="Plasma Current (A)")
        plt.sca(axs[1])
        plot_shot(shot, "Plasma_Density (particlesm3)", label="Plasma_Density (particlesm3)")


    return fig, axs

