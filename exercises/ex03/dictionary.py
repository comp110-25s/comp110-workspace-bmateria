"""Practice with dictionary functions!"""

__author__: str = "730476994"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values in a dictionary"""
    invert_input: dict[str, str] = {}
    for key in input:
        invert_input[input[key]] = key
    return invert_input


def count(input_list: list[str]) -> dict[str, int]:
    """produces a dictionary with unique key and number of times it appears in list"""
    result: dict[str, int] = {}
    idx: int = 0
    while idx < len(input_list):
        if input_list[idx] in result:
            result[input_list[idx]] += 1
        else:
            result[input_list[idx]] = 1
        idx += 1
    return result


def favorite_color(colors_dict: dict[str, str]) -> str:
    """returns color that appears most frequently in the dictionary"""
    colors_list: list[str] = []
    for key in colors_dict:
        colors_list.append(colors_dict[key])
    color_count: dict[str, int] = count(colors_list)
    max_count: int = 0
    max_color: str = ""
    for key in color_count:
        max = color_count[key]
        if max > max_count:
            max_color = key
            max_count = max
    return max_color


def bin_len(input_list: list[str]) -> dict[int, set[str]]:
    """Create a dictionary with strings organized by their lengths"""
    result_dict: dict[int, set] = {}
    for item in input_list:
        if len(item) in result_dict:
            result_dict[len(item)].add(item)
        else:
            result_dict[len(item)] = {item}
    return result_dict
