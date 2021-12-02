import typing

def getData(input_file_path: str) -> typing.List[int]:
    with open(input_file_path, 'r') as openFile:
        return list(map(lambda x: int(x.strip()),openFile.read().split('\n')))


def sliding_window(list_of_depths: typing.List[int], window_size: int = 3) -> typing.List[typing.List[int]]:
    return list(
        filter(
            lambda x:len(x) == window_size,
            [list_of_depths[index:index+window_size] for index, _ in enumerate(list_of_depths)]
        )
    )

def solution(list_of_depths: typing.List[int]) -> int:
    assert len(list_of_depths) > 2, "list of depths must have atleast three elements"

    windows = map(sum, sliding_window(list_of_depths=list_of_depths, window_size=3))
    previous_depth_sum = 0
    increased_depth_count = 0


    for index, window_summation in enumerate(windows):
        if index == 0:
            previous_depth_sum = window_summation
            continue

        if window_summation > previous_depth_sum:
            increased_depth_count += 1

        previous_depth_sum = window_summation

    return increased_depth_count


if __name__ == "__main__":
    # the solution 1257
    print(
        solution(getData("input.txt"))
    )