import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib.patches as patches


def set_axes(ax,xlim,ylim,xlabel,ylabel,xscale='linear',yscale='linear'):

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xscale(xscale)
    ax.set_yscale(yscale)
    ax.set_xlabel(xlabel, fontsize=20, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=20, fontweight='bold')
    ax.spines['bottom'].set_linewidth(3)
    ax.spines['left'].set_linewidth(3)
    ax.spines['top'].set_linewidth(3)
    ax.spines['right'].set_linewidth(3)
    ax.tick_params(axis='both', which='major', labelsize=18, width=3)

def plot_basis(basis):
    plt.rcParams['figure.figsize'] = (8, 6)
    axes = plt.gca()
    axes.plot(np.arange(1,len(basis)+1),np.abs(basis)**2,ls="-",linewidth=7,color="red")
    set_axes(axes,xlim=[1,len(basis)+1],ylim=None,xlabel="basis_idx",ylabel="probability",xscale='linear',yscale='linear')

def plot_dygif(x,t_points,phi):
    fig, ax = plt.subplots(ncols=1,nrows=1,figsize=(8,6))
    line, = ax.plot([], [], lw=5,linestyle='-', color='blue', label="wave")
    set_axes(ax,xlim=[x.min(),x.max()],ylim=[0,phi.max()],xlabel="x",ylabel="probability",xscale='linear',yscale='linear')
    def update(frame):
        print(f'gif animating frame {frame} of {phi.shape[0]}', end='\r')
        line.set_data(x, phi[frame-1])
        return [line,]
    ani = animation.FuncAnimation(fig, update, frames=t_points , blit=True, interval=20)
    return ani