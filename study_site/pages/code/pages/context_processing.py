from django.urls import reverse


def local_link_converter(context):
    return list(map(_create_topic_dict, context))


def _create_topic_dict(topic):
    return {"topic_name": topic["topic_name"], "link_pairs": process_links(topic["link_data"])}


def process_links(link_datas):
    return list(map(_create_name_and_link, link_datas))


def _create_name_and_link(link_data):
    return {"name": link_data.pop("name"), "link": _create_link(link_data)}


def _create_link(reverse_data):
    return reverse(**reverse_data)
