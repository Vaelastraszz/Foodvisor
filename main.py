from database import Database
import json


def get_json_data(url="/Users/RomainLejeune/Downloads/"):
    with open(url + "graph_build.json", "r") as read_file, \
            open(url + "graph_edits.json", "r") as read_file_2, \
            open(url + "img_extract.json", "r") as read_file_3:
        build = json.load(read_file)
        edits = json.load(read_file_2)
        extract = json.load(read_file_3)

    return build, edits, extract


if __name__ == '__main__':
    build, edits, extract = get_json_data()
    db = Database(build[0][0])
    db.add_nodes(build[1:])
    db.display
    db.add_extract(extract)
    db.add_nodes(edits)
    db.display
    db.get_extract
