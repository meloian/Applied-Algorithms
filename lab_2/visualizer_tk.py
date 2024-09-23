from directed_graph import DirectedGraph
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
                        self.draw_edge(canvas, pos[i], pos[j], directed=isinstance(self.graph, DirectedGraph))
        elif self.graph.rep == 'list':
            for v, edges in self.graph.neighbors.items():
                for edge in edges:
                    self.draw_edge(canvas, pos[v], pos[edge[0]], directed=isinstance(self.graph, DirectedGraph))


        # draw vertices
        for v, (x, y) in pos.items():
            self.draw_vertex(canvas, x, y, v)

        window.mainloop()

    def draw_vertex(self, canvas, x, y, label):
        # draw a vertex as a circle
        canvas.create_oval(x - self.v_r, y - self.v_r,
                           x + self.v_r, y + self.v_r, fill="lightblue")
        canvas.create_text(x, y, text=str(label), font=("Arial", 14))

    def draw_edge(self, canvas, pos1, pos2, directed=False):
        x1, y1 = pos1
        x2, y2 = pos2

        dx = x2 - x1
        dy = y2 - y1
        distance = math.sqrt(dx**2 + dy**2)

        # shorten the edge by radius of the vertex to prevent overlap
        if distance > 0:
            x1 = x1 + self.v_r * dx / distance
            y1 = y1 + self.v_r * dy / distance
            x2 = x2 - self.v_r * dx / distance
            y2 = y2 - self.v_r * dy / distance

        if directed:
            # Draw a directed edge with an arrow
            canvas.create_line(x1, y1, x2, y2, fill="black", width=2, arrow=tk.LAST, arrowshape=(10, 12, 6))
        else:
            # Draw an undirected edge (simple line)
            canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

    def draw_arrow(self, canvas, x1, y1, x2, y2):
        angle = math.atan2(y2 - y1, x2 - x1)
        arrow_length = 10
        arrow_angle = math.pi / 6  # 30 degrees

        x3 = x2 - arrow_length * math.cos(angle - arrow_angle)
        y3 = y2 - arrow_length * math.sin(angle - arrow_angle)
        x4 = x2 - arrow_length * math.cos(angle + arrow_angle)
        y4 = y2 - arrow_length * math.sin(angle + arrow_angle)

        canvas.create_line(x2, y2, x3, y3, fill="black", width=2)
        canvas.create_line(x2, y2, x4, y4, fill="black", width=2)
