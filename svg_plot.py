class SVGPlot:
    """A utility class for dynamically generating SVG (Scalable Vector Graphics) elements.

    Attributes:
        width (int): The width of the SVG canvas in pixels.
        height (int): The height of the SVG canvas in pixels.
        size (float): A scaling factor to normalize coordinates.
        html_s (str): A string buffer to accumulate SVG elements.
    """

    def __init__(self, width: int, height: int, size: float) -> None:
        """Initialize the SVG canvas with dimensions and a scaling factor.

        Args:
            width: The width of the SVG canvas in pixels.
            height: The height of the SVG canvas in pixels.
            size: A scaling factor to normalize coordinates (e.g., for grid-based systems).
        """
        self.width = width
        self.height = height
        self.size = size
        self.html_s = ""

    def clear(self) -> None:
        """Reset the SVG canvas by initializing the HTML string with an empty SVG container."""
        self.html_s = f'<svg width="{self.width}" height="{self.height}" style="border:1px solid black">'

    def add_circle(
        self,
        x_pos: float,
        y_pos: float,
        color: str,
        size: float = 1.0
    ) -> None:
        """Add a circle to the SVG canvas.

        Args:
            x_pos: The x-coordinate of the circle's center (normalized by `size`).
            y_pos: The y-coordinate of the circle's center (normalized by `size`).
            color: The fill color of the circle (e.g., "red", "#FF0000").
            size: The diameter of the circle (normalized by `size`).
        """
        x_pos = x_pos / self.size
        y_pos = self.size - y_pos
        y_pos = y_pos / self.size
        radius = size / (self.size * 2)

        # Convert normalized coordinates to pixel values
        str_int_x = str(int((x_pos * self.width) + (radius * self.width)))
        str_int_y = str(int((y_pos * self.height) + (radius * self.width)))
        str_int_r = str(int(radius * self.width))

        self.html_s += f'<circle cx="{str_int_x}" cy="{str_int_y}" r="{str_int_r}" fill="{color}"/>'

    def add_rect(
        self,
        x_pos: float,
        y_pos: float,
        color: str,
        size: float = 1.0
    ) -> None:
        """Add a rectangle to the SVG canvas.

        Args:
            x_pos: The x-coordinate of the rectangle's top-left corner (normalized by `size`).
            y_pos: The y-coordinate of the rectangle's top-left corner (normalized by `size`).
            color: The fill color of the rectangle (e.g., "blue", "#0000FF").
            size: The side length of the square (normalized by `size`).
        """
        x_pos = x_pos / self.size
        y_pos = self.size - y_pos
        y_pos = y_pos / self.size
        height = size / self.size
        width = size / self.size

        # Convert normalized coordinates to pixel values
        str_int_x = str(int(x_pos * self.width))
        str_int_y = str(int(y_pos * self.height))
        str_int_width = str(int(width * self.width))
        str_int_height = str(int(height * self.height))

        self.html_s += f'<rect x="{str_int_x}" y="{str_int_y}" width="{str_int_width}" height="{str_int_height}" fill="{color}"/>'

    def add_polygon(
        self,
        vertices: list[tuple[float, float]],
        color: str
    ) -> None:
        """Add a polygon to the SVG canvas.

        Args:
            vertices: A list of (x, y) tuples representing the polygon's vertices (normalized by `size`).
            color: The fill color of the polygon (e.g., "green", "#00FF00").

        Raises:
            ValueError: If fewer than 3 vertices are provided.
        """
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")

        scaled_vertices = []
        for x, y in vertices:
            scaled_x = (x / self.size) * self.width
            y = self.size - y
            scaled_y = (y / self.size) * self.height
            scaled_vertices.append([scaled_x, scaled_y])

        # Format points as "x1,y1 x2,y2 ..."
        points_string = ' '.join([f"{x},{y}" for x, y in scaled_vertices])
        self.html_s += f'<polygon points="{points_string}" fill="{color}" stroke="black" stroke-width="0.5"/>'

    def get_canvas(self) -> str:
        """Finalize and return the SVG as an HTML object for rendering.

        Returns:
            An HTML object containing the rendered SVG.
        """
        self.html_s += "</svg>"
        return self.html_s