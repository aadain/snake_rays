from SRObject import SRVertex
from SRObject import SRTriangle
from os import path


def read_obj_file(filename: str):
    print(f"Reading OBJ file {filename}")
    # Test that the file actually exits first
    if path.exists(filename):
        with open(filename, "r") as f:
            vertices = []
            faces = []
            # Read the first line then start the loop
            line = f.readline()
            while line != '':
                if line.startswith("#"):
                    print(f"Comment line: {line}")
                elif line.startswith("v "):
                    print(f"Vertex line: {line}", end="")
                    v_parts = line.split()
                    v_parts.pop(0)
                    cords = [float(i) for i in v_parts]
                    print(cords)
                    print(f"X={cords[0]} Y={cords[1]} Z={cords[2]}")

                    # Now build a vertex out of these numbers
                    v = SRVertex(cords[0], cords[1], cords[2])

                    vertices.append(v)
                    count = len(vertices)
                    print(f"Now have {count} vertices")
                # elif line.startswith("vn "):
                #     print(f"Vertex Normal line: {line}")
                elif line.startswith("f "):
                    print(f"Face line: {line}", end="")
                    # Split the line up & drop the 'f' element at the front
                    f_parts = line.split()
                    f_parts.pop(0)
                    # Convert the indexes to ints & decrease by 1 since OBJ format
                    # always starts from 1 instead of the civilized starting index of 0
                    f_parts = [int(i)-1 for i in f_parts]
                    print(f_parts)
                    # Grab the indicated vertices from the vertex list
                    points = [vertices[i] for i in f_parts]
                    # print(points)
                    # Create a triangle from the list
                    face = SRTriangle(points[0], points[1], points[2])
                    faces.append(face)
                    print(face)
                    count = len(faces)
                    print(f"We now have {count} faces")

                line = f.readline()

    else:
        print("Does not exist")
