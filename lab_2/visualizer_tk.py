import tkinter as tk
import math

class GraphVisualizer:
    def __init__(self, graph):
        self.graph = graph
        self.r = 200
        self.v_r = 20
        self.cx = 250
        self.cy = 250

    def visualize(self):
        # create a Tkinter window
        window = tk.Tk()
        window.title("Graph Visualization")

        canvas = tk.Canvas(window, width=500, height=500)
        canvas.pack()

        # calculate positions for vertices in a circle
        pos = {}
        for i in range(self.graph.n):
            angle = 2 * math.pi * i / self.graph.n  # angle for placing vertices
            x = self.cx + self.r * math.cos(angle)
            y = self.cy + self.r * math.sin(angle)
            pos[i] = (x, y)

        # draw edges based on graph representation
        if self.graph.rep == 'matrix':
            for i in range(self.graph.n):
                for j in range(i + 1, self.graph.n):
                    if self.graph.matrix[i][j]:
                        self.draw_edge(canvas, pos[i], pos[j])
        elif self.graph.rep == 'list':
            for v, edges in self.graph.neighbors.items():
                for edge in edges:
                    self.draw_edge(canvas, pos[v], pos[edge[0]])

        # draw vertices
        for v, (x, y) in pos.items():
            self.draw_vertex(canvas, x, y, v)

        window.mainloop()

    def draw_vertex(self, canvas, x, y, label):
        # draw a vertex as a circle
        canvas.create_oval(x - self.v_r, y - self.v_r,
                           x + self.v_r, y + self.v_r, fill="lightblue")
        canvas.create_text(x, y, text=str(label), font=("Arial", 14))

    def draw_edge(self, canvas, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        canvas.create_line(x1, y1, x2, y2, fill="black", width=2)