from string import Template


class SRVertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        t = Template("($x, $y, $z)")
        return t.substitute(x=self.x, y=self.y, z=self.z)


class SRTriangle:
    def __init__(self, v0: SRVertex, v1: SRVertex, v2: SRVertex):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2

    def __str__(self):
        t = Template("T: V0=$v0 V1=$v1 V2=$v2")
        return t.substitute(v0=self.v0, v1=self.v1, v2=self.v2)


class SRObject:
    def __init__(self, name):
        self.name = name
        self.triangles = []
        self.center_x = 0.0
        self.center_y = 0.0
        self.center_z = 0.0

    def __str__(self):
        t = Template("$name: ($x, $y, $z) with $f triangles")
        return t.substitute(name=self.name, x=self.center_x, y=self.center_y, z=self.center_z, f=len(self.triangles))

    def change_name(self, new_name):
        self.name = new_name

    def move_object(self, x, y, z):
        self.center_x = x
        self.center_y = y
        self.center_z = z

    def add_triangle(self, triangle):
        self.triangles.append(triangle)
