import os
import re
from typing import List, Dict


def create_topic_and_pages(name: str, subject: str, page_dicts: List[Dict[str, str]], dir_name: str = None) -> str:
    """
    Creates a dictionary which can should be placed into the relevant context_processor links function. This will hook
    the new topic and pages into the local links bar.
    :param name: The displayed name of the topic on the webpage.
    :param subject: The app the created pages are being placed in.
    :param page_dicts: List of dictionaries that have the name of each page to be created. They may also give a specific
    file name to be used for a page.
    :param dir_name: The name (not path) of the directory the topic pages will be placed in.
    :return: String that is a dictionary containing topic_name and link_data.
    """
    dir_name = _path_legal_name(name) if dir_name is None else dir_name
    hook_dictionaries = [create_topic_page(dir_name=dir_name, subject=subject, **page_dict) for page_dict in page_dicts]
    link_data = "".join(hook_dictionaries)
    topic_dictionary = "{\n\"topic_name\": \"%s\",\n\"link_data\": [\n%s\n]\n}," % (name, link_data)
    return topic_dictionary


def create_topic_page(dir_name: str, subject: str, name: str, file_name: str = None) -> str:
    """
    Creates a html file with boilerplate code. Places it in the correct directory. Returns a string representation of a
    dict that be used to find the link to the page.
    :param dir_name: Name (not path) of the directory the topic page will be placed in.
    :param name: Displayed name of the page on the webpage.
    :param subject: App the created pages are being placed in.
    :param file_name: Specific file name for the html file. Will be a cleaned  and lowercase version of the name if not
    specified.
    :return: String representation of a dictionary containing data that the relevant context processor will use to get
    get the link for the page.
    """
    file_name = _path_legal_name(name) if file_name is None else file_name
    file_directory = os.path.join(os.getcwd(), subject, "templates", subject, "topics", dir_name)
    file_content = _topic_page_content(name, subject)

    if not os.path.exists(file_directory):
        os.mkdir(file_directory)
        print(f"Created new directory {file_directory}")

    with open(os.path.join(file_directory, f"{file_name}.html"), "w") as f:
        f.write(file_content)
        print(f"Created {file_name}.html")

    return "{\"name\": \"%s\", \"viewname\": \"%s: topic_page\", \"args\": [\"%s\", \"%s\"]}," % (
    name, subject, dir_name, file_name)


def _topic_page_content(name: str, subject: str) -> str:
    """
    Creates the boilerplate code that every topic page will use.
    :param name: Displayed name of the page on the webpage.
    :param subject: App the created pages are being placed in.
    :return: String of text.
    """
    line1 = "{% extends \"" + subject + "/base.html\" %}\n\n"
    line2 = "{% block title %}" + name + "{% endblock title %}\n\n"
    line3 = "{% block body %}<h1>" + name + "</h1>{% endblock body %}\n"
    return line1 + line2 + line3


def _path_legal_name(string: str) -> str:
    """
    Removes punctuation except underscores and changes spaces to underscores. This creates a string safe for use in the
    file path.
    :param string: Displayed name of the page on the webpage.
    :return: String that is safe to be used as a directory or file name.
    """
    string = string.lower()
    # Replaces all spaces with an underscore.
    string = re.sub(r"\s", "_", string)
    # Removes all characters that are NOT an alphabetical character or an underscore.
    string = re.sub(r"[^a-z_]", "", string)
    return string
