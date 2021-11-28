from pathlib import Path
import tempfile


def generate_md_header_prefix(level):
    return "#" * level + " "


def main():
    name_link_sourcecode_filepath = Path(input("Write full filename of the new source:\n"))
    path_of_md_file_to_modify = Path(input("Write full name of the markdown file to modify:\n"))
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

    with name_link_sourcecode_filepath.open(mode="rt") as name_link_sourcecode_filestream:
        with tempfile.TemporaryFile(mode="w+t") as prefix_tmpfile, tempfile.TemporaryFile(mode="w+t") as suffix_tmpfile:
            with path_of_md_file_to_modify.open(mode="rt") as stream_of_md_file_to_modify:
                while True:
                    line = stream_of_md_file_to_modify.readline()
                    prefix_tmpfile.write(line)
                    if line.startswith(md_unordered_list_item_prefix):
                        break
                while True:
                    line = stream_of_md_file_to_modify.readline()
                    prefix_tmpfile.write(line)
                    if not line.startswith(md_unordered_list_item_prefix):
                        break
                prefix_tmpfile.seek(0)

                while True:
                    line = stream_of_md_file_to_modify.readline()
                    if line:
                        suffix_tmpfile.write(line)
                    else:
                        break
                suffix_tmpfile.seek(0)

            with path_of_md_file_to_modify.open(mode="wt") as stream_of_md_file_to_modify:
                while True:
                    line = prefix_tmpfile.readline()
                    if line:
                        stream_of_md_file_to_modify.write(line)
                    else:
                        break

                task_name = name_link_sourcecode_filestream.readline().rstrip("\n")
                stream_of_md_file_to_modify.write(md_unordered_list_item_prefix + md_link_decor_start + task_name +
                                                  md_link_decor_mid + md_header_link_prefix +
                                                  task_name.lower().replace(" ", "-") + md_link_decor_end + "\n\n")

                while True:
                    line = suffix_tmpfile.readline()
                    if line:
                        stream_of_md_file_to_modify.write(line)
                    else:
                        break

                stream_of_md_file_to_modify.write("\n")
                stream_of_md_file_to_modify.write(md_header2_decor + task_name + "\n\n")

                task_link = name_link_sourcecode_filestream.readline().rstrip("\n")
                stream_of_md_file_to_modify.write(md_url_prefix + task_link + md_url_postfix + "\n\n")

                stream_of_md_file_to_modify.write(md_code_block_prefix + code_language + "\n")
                while code_line := name_link_sourcecode_filestream.readline():
                    stream_of_md_file_to_modify.write(code_line)
                stream_of_md_file_to_modify.write("\n" + md_code_block_postfix + "\n")

    print("Done.")


if __name__ == "__main__":
    main()
