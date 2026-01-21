import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button
import time
import sys
import argparse

from balls import dynamics, Ball
from files import impData, expData


def generate_sphere_coords(center, radius, resolution=8):
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)    
    x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
    y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
    return x, y, z

def run_simulation(balls_list, dt, trails=False, limit=666):
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit])
    ax.set_zlim([-limit, limit])
    ax.set_title("M.A.S.S.")

    #axb = plt.axes([0.8,0.03,0.1,0.04])
    #save = Button(axb, "save data")
    #save.on_clicked(lambda event: expData("export "+time.ctime()+".csv",balls_list))
    
    #data show
    info_text = fig.text(0.02, 0.95, "Press 'n' to select object...", 
                         fontsize=10, color='white', 
                         bbox=dict(facecolor='black', alpha=0.7, edgecolor='gray'),
                         verticalalignment='top', fontfamily='monospace')

    

    selection_state = {'index': None}
    plots_cache = []

    

    def physics_generator():
        while True:
            dynamics(balls_list, dt)
            
            data_packet = []
            for ball in balls_list:
                data_packet.append((ball.getPos(), ball.r))
            
            yield data_packet

    def on_key(event):
        if event.key == 'n':
            N = len(balls_list)
            if N == 0: return
            
            if selection_state['index'] is None:
                selection_state['index'] = 0
            else:
                selection_state['index'] = (selection_state['index'] +1) % N

        if event.key == 'e':
           expData("export "+time.ctime()+".csv",balls_list)

    fig.canvas.mpl_connect('key_press_event',on_key)

    def draw_frame(data, cache_list):
        for p in cache_list:
            p.remove()
        cache_list.clear()
        
        for i, (position, radius) in enumerate(data):
            if trails:
                ax.scatter(position[0], position[1], position[2], s=1, c="blue")

            x, y, z = generate_sphere_coords(position, radius, resolution=8)

            selected  = (i == selection_state['index'])
            color = 'red' if selected else 'purple'
            alpha = 1.0 if selected else 0.8

            surf = ax.plot_surface(x, y, z, color=color, alpha=alpha, shade=True)
            cache_list.append(surf)
       

        if selection_state['index'] is None:
            info_text.set_text("Press 'n' to select object")
            info_text.set_color('white')
        else:
            id = selection_state['index']
            if  id < len(balls_list):
                b = balls_list[id]
                pos = b.getPos()
                vel = np.linalg.norm(b.getVel())
            txt = (f"Object no. {id+1}\n"
                   f"Mass:      {b.getMass():.2e}\n"
                   f"Radius:    {b.getRad()}\n"
                   f"Position:  [{pos[0]:.1f},{pos[1]:.1f},{pos[2]:.1f}]\n"
                   f"Velocity:  {vel:.2f}")
            info_text.set_text(txt)
            info_text.set_color('yellow')

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

def main():
    
    info = ("MACRO:\n"
            "============================\n"
            "   n   focus on next object\n"
            "   e   save current state\n"
            "============================\n"
            "\n\n"
            "FILE STRUCTURE: \n"
            "==============\n"
            " mass, radius, x position, y position, z position, x velocity, y velocity, z velocity\n"
            "--------------------------------------------------------------------------------------\n"
            " 2e10,     30,        1.1,        2.2,        3.3,        4.4,        5.5,     6.6    \n"
            "  100,      2,         10,          9,          8,          7,          6,       5    \n"
            "======================================================================================\n"
            "File should contain only values!\n\n"

            "Authors: Kacper Śmieżewski, Stanisław Pokora\n")

    parser = argparse.ArgumentParser(description="Modeling and Analysing of Spacetime Simulation", epilog=info, formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-f', '--file', type=str, required=True, help='csv file path')

    parser.add_argument('-dt', '--dtime', type=float, default=0.1, help='timestep length')

    parser.add_argument('-t', '--trail', action="store_true", help="enable trails (not recomended for slow computers)")

    parser.add_argument('-l', '--limit', type=int, default=666, help="box limits")

    args = parser.parse_args()

    objects=impData(args.file)
    run_simulation(objects, args.dtime, args.trail, args.limit) 

    
def randBall(N):
    balls = []
    for _ in range(N):
        m = (np.random.rand() * 100 + 1)*10**11
        r = 1.0
        pos = np.random.rand(3) * 200 - 100
        vel = np.random.rand(3) * 10 - 5
        balls.append(Ball(m, r, pos, vel))

    expData("interstellarballs.csv", balls)    


if __name__ == "__main__":
    main()
    #randBall(42)
