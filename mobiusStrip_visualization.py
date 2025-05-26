import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from IPython.display import HTML

class MobiusStrip:
    def __init__(self, R=1.0, w=0.2, n=100):
        """
        Initialize the Mobius strip with given radius, width, and resolution.
        R - Radius from center to strip midline
        w - Width of the strip
        n - Number of points for mesh resolution
        """
        self.R = R
        self.w = w
        self.n = n
        self.u_vals = np.linspace(0, 2 * np.pi, n)
        self.v_vals = np.linspace(-w / 2, w / 2, n)
        self.X, self.Y, self.Z = self._generate_mesh()

    def _parametric(self, u, v):
        """
        Parametric equations of the Mobius strip.
        Returns x, y, z for given u and v.
        """
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def _generate_mesh(self):
        """
        Generate the meshgrid of (X, Y, Z) coordinates.
        """
        U, V = np.meshgrid(self.u_vals, self.v_vals)
        X, Y, Z = self._parametric(U, V)
        return X, Y, Z

    def plot(self, cmap='plasma'):
        """
        Static 3D plot of the Mobius strip.
        """
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, cmap=cmap, edgecolor='k')
        ax.set_title("Möbius Strip")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.tight_layout()
        plt.show()

    def animate(self, frames=90, interval=100):
        """
        Create a rotating 3D animation of the Mobius strip.
        Returns a matplotlib animation object.
        """
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis', edgecolor='k', alpha=0.8)

        def init():
            ax.view_init(elev=30, azim=0)
            return fig,

        def update(frame):
            ax.view_init(elev=30, azim=frame)
            return fig,

        ani = animation.FuncAnimation(fig, update, init_func=init,
                                      frames=frames, interval=interval, blit=False)
        plt.close(fig)  # Prevent duplicate output
        return ani

# Create the Mobius strip object
strip = MobiusStrip(R=1.0, w=0.3, n=150)

# Render animation
animation_obj = strip.animate(frames=120, interval=100)

# Display in Google Colab
HTML(animation_obj.to_jshtml())
