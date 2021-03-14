from SRObject import SRVertex
from SRObject import SRTriangle
from os import path
import logging
import sys

FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "snake_rays.log"


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = logging.FileHandler(LOG_FILE, mode='w+')
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # better to have too much log than not enough
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger


def read_obj_file(filename: str):
    sr_logger = get_logger("SRObjectReader")
    sr_logger.info(f"Reading OBJ file {filename}")
    if path.exists(filename):
        with open(filename) as f:
            vertices = []
            faces = []
            for line in f:
                line = line.rstrip()
                if line.startswith("#"):
                    sr_logger.debug(f"Comment line: {line}")
                elif line.startswith("v "):
                    sr_logger.debug(f"Vertex line: {line}")
                    v_parts = line.split()
                    v_parts.pop(0)
                    cords = [float(i) for i in v_parts]
                    sr_logger.debug(cords)
                    sr_logger.debug(f"X={cords[0]} Y={cords[1]} Z={cords[2]}")

                    # Now build a vertex out of these numbers
                    v = SRVertex(cords[0], cords[1], cords[2])

                    vertices.append(v)
                    count = len(vertices)
                    sr_logger.debug(f"Now have {count} vertices")
                elif line.startswith("vn "):
                    sr_logger.debug(f"Vertex Normal line: {line}")
                elif line.startswith("f "):
                    sr_logger.debug(f"Face line: {line}")
                    # Split the line up & drop the 'f' element at the front
                    f_parts = line.split()
                    f_parts.pop(0)
                    # Convert the indexes to ints & decrease by 1 since OBJ format
                    # always starts from 1 instead of the civilized starting index of 0
                    f_parts = [int(i)-1 for i in f_parts]
                    sr_logger.debug(f_parts)
                    # Grab the indicated vertices from the vertex list
                    points = [vertices[i] for i in f_parts]
                    # Create a triangle from the list
                    face = SRTriangle(points[0], points[1], points[2])
                    faces.append(face)
                    sr_logger.debug(face)
                    count = len(faces)
                    sr_logger.debug(f"We now have {count} faces")

        sr_logger.info(f"Read a total of {len(faces)} triangles with {len(vertices)} vertices")
    else:
        sr_logger.error("Does not exist")
