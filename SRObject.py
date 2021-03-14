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
    pass
