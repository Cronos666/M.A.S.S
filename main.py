import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button
import time

from balls import dynamics
from files import impData, expData


def generate_sphere_coords(center, radius, resolution=8):
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)    
    x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
    y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
    return x, y, z

def run_simulation(balls_list, dt, limit=666):
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit])
    ax.set_zlim([-limit, limit])
    ax.set_title("M.A.S.S.")

    axb = plt.axes([0.8,0.03,0.1,0.04])
    save = Button(axb, "save data")
    save.on_clicked(lambda event: expData("export "+time.ctime()+".csv",balls_list))
    

    plots_cache = []

    

    def physics_generator():
        while True:
            dynamics(balls_list, dt)
            
            data_packet = []
            for ball in balls_list:
                data_packet.append((ball.getPos(), ball.r))
            
            yield data_packet

    def draw_frame(data, cache_list):
        for p in cache_list:
            p.remove()
        cache_list.clear()
        
        for position, radius in data:
            x, y, z = generate_sphere_coords(position, radius, resolution=8)
            surf = ax.plot_surface(x, y, z, color='blue', alpha=0.9, shade=True)
            cache_list.append(surf)
            
        return cache_list

    ani = animation.FuncAnimation(
        fig, 
        draw_frame,              
        frames=physics_generator, 
        fargs=(plots_cache,),
        interval=10, 
        blit=False,
        save_count=50            
    )

    plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print("Not enough arguments")
    else:
        filename=sys.argv[1]
        print(filename)
        objects=impData(filename)

        run_simulation(objects, dt=0.05)
        pass
