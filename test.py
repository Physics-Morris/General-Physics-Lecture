import numpy as np
import StephCurry.basketball as sc
import matplotlib.pyplot as plt

# pip install git+https://github.com/Physics-Morris/General-Physics-Lecture 

mass = 0.59
distances = [6.25, 7.6, 14]
height = 3.05
inner_r = 0.4572/2
release_point = 2.0
initial_angle = 45 * np.pi / 180
ball_r = 0.24
dt = 1e-2
ball_omega = 2*np.pi/0.1
cw = 0.5
da = 1.14

##### EXAMPLE 1 #####
# create a ball object and shoot
# v = 8
# vx, vy = v * np.cos(initial_angle), v * np.sin(initial_angle)
# basketball = sc.ball(x=0, y=release_point, vx=vx, vy=vy, omega=ball_omega, r=ball_r, mass=mass)
# goal, d_min = basketball.shoot(rim_x=distances[0], rim_y=height, rim_r=inner_r,
#                                g=9.8, drag_coefficient=cw, air_density=da, dt=dt)


##### EXAMPLE 2 #####
# find minimum distance to the rime
# minimum = []
# for v in np.arange(6, 12, .01):
#     vx, vy = v * np.cos(initial_angle), v * np.sin(initial_angle)
#     basketball = sc.ball(x=0, y=release_point, vx=vx, vy=vy, omega=ball_omega, r=ball_r, mass=mass)

#     # shoot a ball
#     goal, d_min = basketball.shoot(rim_x=distances[0], rim_y=height, rim_r=inner_r,
#                                    g=9.8, drag_coefficient=cw, air_density=da, dt=dt)
#     minimum.append(d_min)
# plt.plot(np.arange(6, 12, .01), minimum)
# plt.show()


##### EXAMPLE 3 #####
# plot trajectory of ball
v = 8
vx, vy = v * np.cos(initial_angle), v * np.sin(initial_angle)
basketball = sc.ball(x=0, y=release_point, vx=vx, vy=vy, omega=ball_omega, r=ball_r, mass=mass)
traj = basketball.trajectory(rim_x=distances[0], rim_y=height, rim_r=inner_r,
                             g=9.8, drag_coefficient=cw, air_density=da, dt=dt)
plt.plot(traj[0, :], traj[1, :])
plt.show()