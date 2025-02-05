from manim import *
import numpy as np
from scipy.integrate import odeint


class ThreeBodyProblem(Scene):
    def construct(self):
        # Non-Dimensionalisation
        G = 6.67408e-11  # Gravitational constant
        m_nd = 1.989e+30  # Reference mass (kg)
        r_nd = 5.326e+12  # Reference distance (m)
        v_nd = 30000  # Reference velocity (m/s)
        t_nd = 79.91 * 365.25 * 24 * 3600  # Reference time (s)

        # Net constants
        K1 = G * t_nd * m_nd / (r_nd**2 * v_nd)
        K2 = v_nd * t_nd / r_nd

        # Masses of the bodies
        m1, m2, m3 = 1.1, 0.907, 1.425

        # Initial positions
        r1 = np.array([-0.5, 1, 0])
        r2 = np.array([0.5, 0, 0.5])
        r3 = np.array([0.2, 1, 1.5])

        # Initial velocities
        v1 = np.array([0.02, 0.02, 0.02])
        v2 = np.array([-0.05, 0, -0.1])
        v3 = np.array([0, -0.03, 0])

        # Define the system of differential equations
        def ThreeBodyEquations(w, t, G, m1, m2, m3):
            # Unpack positions and velocities
            r1, r2, r3 = w[:3], w[3:6], w[6:9]
            v1, v2, v3 = w[9:12], w[12:15], w[15:18]
            r12 = np.linalg.norm(r2 - r1)
            r13 = np.linalg.norm(r3 - r1)
            r23 = np.linalg.norm(r3 - r2)
            # Compute accelerations
            dv1dt = K1 * m2 * (r2 - r1) / r12**3 + K1 * m3 * (r3 - r1) / r13**3
            dv2dt = K1 * m1 * (r1 - r2) / r12**3 + K1 * m3 * (r3 - r2) / r23**3
            dv3dt = K1 * m1 * (r1 - r3) / r13**3 + K1 * m2 * (r2 - r3) / r23**3
            dr1dt = K2 * v1
            dr2dt = K2 * v2
            dr3dt = K2 * v3
            return np.concatenate((dr1dt, dr2dt, dr3dt, dv1dt, dv2dt, dv3dt))

        # Initial parameters
        init_params = np.concatenate((r1, r2, r3, v1, v2, v3))
        time_span = np.linspace(0, 20, 1000)

        # Solve the equations of motion
        solution = odeint(ThreeBodyEquations, init_params, time_span, args=(G, m1, m2, m3))
        r1_sol, r2_sol, r3_sol = solution[:, :3], solution[:, 3:6], solution[:, 6:9]

        # Normalize solutions to fit within the screen bounds
        scale_factor = 2  # Adjust this to fit the scene
        r1_sol /= scale_factor
        r2_sol /= scale_factor
        r3_sol /= scale_factor

        # Create celestial bodies
        body1 = Dot(color=BLUE).move_to(r1_sol[0])
        body2 = Dot(color=RED).move_to(r2_sol[0])
        body3 = Dot(color=YELLOW).move_to(r3_sol[0])

        # Create trails
        trail1 = VMobject(color=BLUE)
        trail2 = VMobject(color=RED)
        trail3 = VMobject(color=YELLOW)

        trail1.set_points_as_corners([body1.get_center()])
        trail2.set_points_as_corners([body2.get_center()])
        trail3.set_points_as_corners([body3.get_center()])

        self.add(body1, body2, body3, trail1, trail2, trail3)

        # Update function for bodies and trails
        def update_bodies_and_trails(mob, alpha):
            idx = int(alpha * (len(r1_sol) - 1))  # Scale alpha to index
            body1.move_to(r1_sol[idx])
            body2.move_to(r2_sol[idx])
            body3.move_to(r3_sol[idx])
            trail1.add_points_as_corners([body1.get_center()])
            trail2.add_points_as_corners([body2.get_center()])
            trail3.add_points_as_corners([body3.get_center()])

        # Play animation
        self.play(UpdateFromAlphaFunc(trail1, update_bodies_and_trails), run_time=10, rate_func=linear)
