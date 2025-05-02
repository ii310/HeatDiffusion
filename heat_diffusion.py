import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from save_data import add_buttons
from db_user_masterpieces import save_drawing_to_db


grid_size = 80 
dx = 1.0 # widths
dy = 1.0
alpha = 0.1 # Coefficient of radiated heat (thermal diffusion)        
dt = 0.1 # time step


T = np.zeros((grid_size, grid_size)) # Adujusting Initnal heat matrix, set to zero


fig, ax = plt.subplots(figsize=(10, 6)) # Settings for matplotlib 
cax = ax.imshow(T, cmap='hot', interpolation='nearest', vmin=0, vmax=100) #imshow() used to display images in a plot
fig.colorbar(cax)
plt.title("Interactive 2D Heat Diffusion")


mouse_position = None # track the mouse, update

def mouse_movement(event):
    global mouse_position
    if event.xdata is not None and event.ydata is not None:
        mouse_position = (int(event.ydata), int(event.xdata))  # get as y,x for 2D matrixs 
    else:
        mouse_position = None

fig.canvas.mpl_connect('motion_notify_event', mouse_movement)


def diffuse(T): # applying heat diffusion function (The two-dimensional diffusion equation, scipython Christian Hill Chapter 7)
    T_new = T.copy()
    dx2 = dx**2
    dy2 = dy**2
    D = alpha

    for i in range(1, grid_size - 1):
        for j in range(1, grid_size - 1):
            uxx = (T[i+1,j] - 2*T[i,j] + T[i-1,j]) / dx2
            uyy = (T[i,j+1] - 2*T[i,j] + T[i,j-1]) / dy2
            T_new[i,j] = T[i,j] + dt * D * (uxx + uyy)
    
    return T_new

def on_key(event):
    if event.key == 'w':
        name = input("Hey there arist! Please enter your name here: ")
        if name:
            save_drawing_to_db(name, T)



fig.canvas.mpl_connect('key_press_event', on_key)

def update(frame): # updateing the frame by using function
    global T
    if is_paused[0]:
        return cax,
    T = diffuse(T)

    
    if mouse_position is not None: # if mouse there activate heat
        y, x = mouse_position
        if 1 <= y < grid_size-1 and 1 <= x < grid_size-1:
            T[y-1:y+2, x-1:x+2] += 1.5   # heating the small area of the mouse 

            # limiting the maxsimum heat value
            T = np.clip(T, 0, 100)
            
    T_ref[0] = T
    cax.set_data(T)
    return cax,

is_paused = [False]
T_ref = [T]  # List içine koyarsak referans verilebilir olur

add_buttons(fig, T_ref, is_paused)

ani = animation.FuncAnimation(fig, update, frames=300, interval=50, blit=False) # starting the animation
plt.show()