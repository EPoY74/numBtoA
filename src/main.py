"""
Решает задачу:
Даны два строковых представления чисел A и B. Нужно максимизировать A, заменив в нём любую
цифру на цифру из B. Каждую цифру B можно использовать только один раз.
"""


def main(numA: str, numB: str) -> str:
    result: list[str] = []
    is_all_zeros: bool = False
    numB_sorted_asc = sorted(numB)
    numB_sorted_dec = sorted(numB, reverse=True)
    # numA_list =
    my_str: str = ""
    is_negative: bool = False

    for index, oneDig in enumerate(numA):
        if (oneDig == "-") and (index == 0):
            is_negative = True
            continue
        if is_negative:
            if not numB_sorted_dec:
                result.append(oneDig)
                continue

            if oneDig > numB_sorted_dec[-1]:
                result.append(numB_sorted_dec[-1])
                numB_sorted_dec.pop(-1)
            else:
                result.append(oneDig)

        else:
            if not numB_sorted_asc:
                result.append(oneDig)
                continue

            if oneDig < numB_sorted_asc[-1]:
                result.append(numB_sorted_asc[-1])
                # result = numB_sorted[-1]
                numB_sorted_asc.pop(-1)
            else:
                result.append(oneDig)

    if all(ch == "0" for ch in result):
        is_all_zeros = True
    my_str = "".join(result)
    if is_negative and (not is_all_zeros):
        my_str = "-" + my_str
    return str(my_str)


if __name__ == "__main__":
    inputNumA: str = "8350"
    inputNumB: str = "0129"
    # inputNumA, inputNumB = inputNums()

    result = main(inputNumA, inputNumB)
    print(result)
