import numpy as np
import scipy as sc

class ball:

    def __init__(self, x, y, vx, vy, omega, r, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.omega = omega
        self.r = r
        self.mass = mass

    def shoot(self, rim_x, rim_y, rim_r, g, drag_coefficient, air_density, dt):
        result = False
        while True:
            old_dis = self.distance_to_rim(rim_x, rim_y) 
            self = self.euler(dt, g, drag_coefficient, air_density)
            new_dis = self.distance_to_rim(rim_x, rim_y)
            if (new_dis > old_dis): break
            # find minimum distance to the rim
            min_distance = self.distance_to_rim(rim_x, rim_y)
            if self.distance_to_rim(rim_x, rim_y) < min_distance :
                min_distance = self.distance_to_rim(rim_x, rim_y)
            if min_distance < rim_r-self.r:
                result = True
                break
        return result, min_distance

    def trajectory(self, rim_x, rim_y, rim_r, g, drag_coefficient, air_density, dt):
        traj = [[self.x], [self.y], [self.vx], [self.vy]]
        while True:
            old_dis = self.distance_to_rim(rim_x, rim_y) 
            self = self.euler(dt, g, drag_coefficient, air_density)
            new_dis = self.distance_to_rim(rim_x, rim_y)
            traj[0].append(self.x)
            traj[1].append(self.y)
            traj[2].append(self.vx)
            traj[3].append(self.vy)
            if (new_dis > old_dis): break
            if self.distance_to_rim(rim_x, rim_y) < rim_r-self.r: break
        return np.array(traj)

    def find_min_distance(self, rim_x, rim_y, g, drag_coefficient, air_density, dt):
        while (self.x+2*self.r > 0) and (self.y >= 0):
            ball = ball.euler(dt, g, drag_coefficient, air_density)
            # find minimum distance to the rim
            min_distance = ball.distance_to_rim(rim_x, rim_y)
            if ball.distance_to_rim(rim_x, rim_y) < min_distance :
                min_distance = ball.distance_to_rim(rim_x, rim_y)
        return min_distance

    def force(self, g, drag_coefficient, air_density):
        vx, vy, omega = self.vx, self.vy, self.omega
        # air resistance
        w = 0.5 * drag_coefficient * air_density * (np.pi * self.r**2) * self.speed()**2
        # magnus force f_M = 4.1 * 10^-4 * m * omega x v
        # ref: http://farside.ph.utexas.edu/teaching/329/lectures/node43.html 
        l = 4.1 * 1e-4 * self.mass
        fx = -w * vx / self.speed() - l * vy * omega
        fy = -w * vy / self.speed() - self.mass * g + l * vx * omega
        return [fx, fy]

    def euler(self, dt, g, drag_coefficient, air_density):
        xn, yn, vxn, vyn = 0, 0, 0, 0
        xn = self.x + self.vx * dt
        yn = self.y + self.vy * dt
        vxn = self.vx + self.force(g, drag_coefficient, air_density)[0] * dt / self.mass
        vyn = self.vy + self.force(g, drag_coefficient, air_density)[1] * dt / self.mass
        return ball(xn, yn, vxn, vyn, self.omega, self.r, self.mass)

    def distance_to_rim(self, x, y):
        d = ((self.x - x)**2 + (self.y - y)**2)**0.5
        return d

    def speed(self):
        return (self.vx**2 + self.vy**2)**0.5