from pathlib import Path


def read_data(filename):
    pass


def write_data(filename, data):
    pass


def get_md_data(data):
    pass


def get_new_md_solution(data):
    pass


def get_old_md_solutions():
    pass


def generate_md_header_prefix(level):
    return "#" * level + " "


def main():
    name_link_sourcecode_filepath = Path("input.txt")
    path_of_md_file_to_modify = Path("arrays2.md")
    code_language = "python3"

    md_unordered_list_item_prefix = "+ "
    md_link_decor_start = "["
    md_link_decor_mid = "]("
    md_link_decor_end = ")"

    md_url_prefix = "<"
    md_url_postfix = ">"

    md_code_block_prefix = "```"
    md_code_block_postfix = "```"

    md_header2_decor = generate_md_header_prefix(level=2)
    md_header_link_prefix = "#"

    with name_link_sourcecode_filepath.open(mode="r") as name_link_sourcecode_filestream,\
            path_of_md_file_to_modify.open(mode="r+") as stream_of_md_file_to_modify:
        while True:
            line = stream_of_md_file_to_modify.readline()
            if line.startswith(md_unordered_list_item_prefix):
                break
        while stream_of_md_file_to_modify.readline().startswith(md_unordered_list_item_prefix):
            pass
        task_name = name_link_sourcecode_filestream.readline().rstrip("\n")
        stream_of_md_file_to_modify.write(md_unordered_list_item_prefix + md_link_decor_start + task_name +
                                          md_link_decor_mid + md_header_link_prefix +
                                          task_name.lower().replace(" ", "-") + md_link_decor_end + "\n")
        stream_of_md_file_to_modify.readlines()
        stream_of_md_file_to_modify.write("\n")
        stream_of_md_file_to_modify.write(md_header2_decor + task_name + "\n\n")

        task_link = name_link_sourcecode_filestream.readline().rstrip("\n")
        stream_of_md_file_to_modify.write(md_url_prefix + task_link + md_url_postfix + "\n\n")

        stream_of_md_file_to_modify.write(md_code_block_prefix + code_language + "\n")
        while code_line := name_link_sourcecode_filestream.readline():
            stream_of_md_file_to_modify.write(code_line)
        stream_of_md_file_to_modify.write(md_code_block_postfix + "\n\n")


if __name__ == "__main__":
    main()
