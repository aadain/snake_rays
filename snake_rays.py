from SRObjectReader import read_obj_file
import logging


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s')
    test_obj_file = "Objects/teapot.obj"
    test_obj = read_obj_file(test_obj_file)
    test_obj.change_name("teapot")



if __name__ == '__main__':
    main()

