from functools import lru_cache

from pages.code.pages.context_processing import local_link_converter


@lru_cache
def links():
    context = [
        {
            "topic_name": "Computer Science",
            "link_data":
                [
                    {"name": "Index", "viewname": "computer_science:index"},
                    {"name": "Glossary", "viewname": "computer_science:glossary"},
                ]
        },
        {
            "topic_name": "Characteristics of Contemporary Processors",
            "link_data": [
                {"name": "Structure and Function of the Processor", "viewname": "computer_science:topic_page",
                 "args": ["contemporary_processors", "structure_and_function"]},
                {"name": "Types of Processor", "viewname": "computer_science:topic_page",
                 "args": ["contemporary_processors", "types_of_processor"]},
                {"name": "Input, Output and Storage", "viewname": "computer_science:topic_page",
                 "args": ["contemporary_processors", "input_output_and_storage"]},
            ]
        },
        {
            "topic_name": "Software and Software Development",
            "link_data": [
                {"name": "Systems Software", "viewname": "computer_science:topic_page",
                 "args": ["software_and_software_development", "systems_software"]},
                {"name": "Applications Software", "viewname": "computer_science:topic_page",
                 "args": ["software_and_software_development", "applications_software"]},
                {"name": "Software Development", "viewname": "computer_science:topic_page",
                 "args": ["software_and_software_development", "software_development"]},
                {"name": "Types of Programming Logic", "viewname": "computer_science:topic_page",
                 "args": ["software_and_software_development", "types_of_programming_logic"]},
            ]
        },
        {
            "topic_name": "Exchanging Data",
            "link_data": [
                {"name": "Compression, Encryption and Hashing", "viewname": "computer_science:topic_page",
                 "args": ["exchanging_data", "compression_encryption_and_hashing"]},
                {"name": "Databases", "viewname": "computer_science:topic_page",
                 "args": ["exchanging_data", "databases"]},
                {"name": "Networks", "viewname": "computer_science:topic_page",
                 "args": ["exchanging_data", "networks"]},
                {"name": "Web Technologies", "viewname": "computer_science:topic_page",
                 "args": ["exchanging_data", "web_technologies"]},
            ]
        },
        {
            "topic_name": "Data Types and Data Structures",
            "link_data": [
                {"name": "Data Types", "viewname": "computer_science:topic_page",
                 "args": ["data_types_and_data_structures", "data_types"]},
                {"name": "Data Structures", "viewname": "computer_science:topic_page",
                 "args": ["data_types_and_data_structures", "data_structures"]},
                {"name": "Boolean Algebra", "viewname": "computer_science:topic_page",
                 "args": ["data_types_and_data_structures", "boolean_algebra"]},
            ]
        },
        {
            "topic_name": "Legal, Moral, Cultural and Ethical Issues",
            "link_data": [
                {"name": "Computing related legislation", "viewname": "computer_science:topic_page",
                 "args": ["issues", "computing_related_legislation"]},
                {"name": "Moral and Ethical Issues", "viewname": "computer_science:topic_page",
                 "args": ["issues", "moral_and_ethical_issues"]},
            ]
        },
        {
            "topic_name": "Elements of Computational Thinking",
            "link_data": [
                {"name": "Thinking Abstractly", "viewname": "computer_science:topic_page",
                 "args": ["computational_thinking", "thinking_abstractly"]},
                {"name": "Thinking Ahead", "viewname": "computer_science:topic_page",
                 "args": ["computational_thinking", "thinking_ahead"]},
                {"name": "Thinking Procedurally", "viewname": "computer_science:topic_page",
                 "args": ["computational_thinking", "thinking_procedurally"]},
                {"name": "Thinking Logically", "viewname": "computer_science:topic_page",
                 "args": ["computational_thinking", "thinking_logically"]},
                {"name": "Thinking Concurrently", "viewname": "computer_science:topic_page",
                 "args": ["computational_thinking", "thinking_concurrently"]},
            ]
        },
        {
            "topic_name": "Problem Solving and Programming",
            "link_data": [
                {"name": "Programming Techniques", "viewname": "computer_science:topic_page",
                 "args": ["problem_solving_and_programming", "programming_techniques"]},
                {"name": "Computational Methods", "viewname": "computer_science:topic_page",
                 "args": ["problem_solving_and_programming", "computational_methods"]},
            ]
        },
        {
            "topic_name": "Algorithms",
            "link_data": [
                {"name": "Analysis, Design and Comparison", "viewname": "computer_science:topic_page",
                 "args": ["algorithms", "analysis_design_and_comparison"]},
                {"name": "Algorithms for the Main Data Structures", "viewname": "computer_science:topic_page",
                 "args": ["algorithms", "algorithms_for_the_main_data_structures"]},
                {"name": "Sorting Algorithms", "viewname": "computer_science:topic_page",
                 "args": ["algorithms", "sorting_algorithms"]},
                {"name": "Searching Algorithms", "viewname": "computer_science:topic_page",
                 "args": ["algorithms", "searching_algorithms"]},
                {"name": "Path Finding Algorithms", "viewname": "computer_science:topic_page",
                 "args": ["algorithms", "path_finding_algorithms"]},
            ]
        },

    ]

    return {"computer_science_links": local_link_converter(context)}


def computer_science_links(request):
    return links()
