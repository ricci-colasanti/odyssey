class SVGCanvas:
    def __init__(self,width,height,size):
        self.width = width
        self.height = height
        self.size = size
        self.html_s =""

    def clear(self):
        self.html_s = f'<svg width="{self.width}" height="{self.height}"style="border:1px solid black">'

    def addCircle(self,x_pos,y_pos,color):
        x_pos = x_pos/self.size
        y_pos = y_pos/self.size
        r = 1/(self.size*2)
        int_x = int((x_pos*self.width)+(r*self.width))
        int_y = int((y_pos*self.height)+(r*self.width))
        int_r = int(r*self.width)
        self.html_s +=f'<circle cx="{int_x}" cy="{int_y}" r="{int_r}" fill="{color}"/>'

    def addRect(self,x_pos,y_pos,color):
        x_pos = x_pos/self.size
        y_pos = y_pos/self.size
        height = 1/self.size
        width = 1/self.size
        int_x = str(int(x_pos*self.width))
        int_y = str(int(y_pos*self.height))
        int_width = str(int(width*self.width))
        int_height = str(int(height*self.height))
        self.html_s +=f'<rect x="{int_x}" y="{int_y}" width="{int_width}" height="{int_height}" fill="{color}"/>'

    def getCanvas(self):
        self.html_s += "</svg>"
        return self.html_s