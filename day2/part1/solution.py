import typing

def getData(file_path: str) -> typing.List[typing.Union[str, int]]:
    with open(file_path, "r") as openFile:
        return list(
            map(
                lambda instruction: [instruction[0], int(instruction[1])],
                map(
                    lambda x: x.strip().split(" "), 
                    openFile.read().split("\n")
                )
            )
        )

def solution(list_of_instructions: typing.List[typing.Union[str, int]]) -> int:
    # movements
    depth = 0
    horizontal = 0

    for instruction in list_of_instructions:
        assert len(instruction) == 2 and type(instruction[0]) == str, "Invalid Instruction"

        command = instruction[0].lower() # this is the command to execute on
        movement = instruction[1]

        if command == "forward":
            horizontal += movement
        elif command == "up":
            depth -= movement
        elif command == "down":
            depth += movement

    return depth * horizontal


print(
    solution(getData("input.txt"))
)