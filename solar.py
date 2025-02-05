from manim import *
import numpy as np

class SideViewSolarSystem(ThreeDScene):  # Use ThreeDScene for 3D camera manipulation
    def construct(self):
        # Define the Sun and planets
        sun = Dot(color=YELLOW).scale(2)  # Sun at the center

        # Orbital radii for planets (scaled for visualization)
        orbit_radii = [2, 3, 4, 6, 8, 10, 12, 14]  # Orbital radii
        planet_colors = [BLUE, GREEN, RED, ORANGE, PURPLE, TEAL, GRAY, DARK_BLUE]
        planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

        # Create orbits (ellipses) and planets (dots)
        orbits = VGroup()
        planets = VGroup()
        planet_labels = VGroup()

        for i, radius in enumerate(orbit_radii):
            orbit = Circle(radius=radius, color=WHITE, stroke_opacity=0.5).set_stroke(width=1)
            orbits.add(orbit)

            planet = Dot(color=planet_colors[i]).scale(11)  # Smaller planets
            planet.move_to([radius, 0, 0])
            planets.add(planet)

            label = Text(planet_names[i], font_size=12, color=planet_colors[i])
            label.next_to(planet, UP, buff=0.2)
            planet_labels.add(label)

        # Group all elements to scale them together
        solar_system = VGroup(sun, orbits, planets, planet_labels)
        solar_system.scale(0.3)  # Scale down the entire solar system

        # Add all elements to the scene
        self.add(sun, orbits, planets, planet_labels)

        # Set the camera to a side view
        self.set_camera_orientation(phi=30
         * DEGREES, theta=30 * DEGREES)

        # Animation: Planets orbit around the Sun
        animations = []
        for i, planet in enumerate(planets):
            # Each planet rotates around the Sun at a different speed
            orbit_period = 10 / (i + 1)  # Faster for inner planets, slower for outer planets
            animations.append(Rotate(planet, angle=TAU, about_point=ORIGIN, run_time=orbit_period, rate_func=linear))

        # Animate all planets together
        self.begin_ambient_camera_rotation(rate=0.1)  # Slow rotation of the camera
        self.play(AnimationGroup(*animations, lag_ratio=0.1), run_time=20, rate_func=linear)
        self.wait()
