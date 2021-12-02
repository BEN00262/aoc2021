import typing


def getData(input_file_path: str) -> typing.List[int]:
    with open(input_file_path, 'r') as openFile:
        return list(map(lambda x: int(x.strip()),openFile.read().split('\n')))


def solution(list_of_depths: typing.List[int]) -> int:
    assert len(list_of_depths) > 0, "list of depths must have atleast one element"
    
    previous_depth = list_of_depths[0]
    increased_depth_count = 0

    for index, depth in enumerate(list_of_depths):
        if index == 0:
            # this is (N/A - no previous measurement)
            continue
        
        if depth > previous_depth:
            increased_depth_count += 1

        previous_depth = depth

    return increased_depth_count


if __name__ == "__main__":
    # the solution 1228
    print(
        solution(getData("input.txt"))
    )