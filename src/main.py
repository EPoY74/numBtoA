"""
Решает задачу:
Даны два строковых представления чисел A и B. Нужно максимизировать A, заменив в нём любую
цифру на цифру из B. Каждую цифру B можно использовать только один раз.
"""


def printInfo(info: str):
    print(info, end=" ")


def inputNums() -> tuple[str, str]:
    while True:
        try:
            printInfo("Введите число А:")
            numA: str = input().strip()
        except Exception as err:
            raise err
        break

    while True:
        try:
            printInfo("Введите число В:")
            numB: str = input().strip()
            break
        except Exception as err:
            raise err
        break
    return (numA, numB)


def main(numA: str, numB: str) -> str:
    print(numA)
    print(numB)
    return "1"


if __name__ == "__main__":
    inputNumA: str = ""
    inputNumB: str = ""
    inputNumA, inputNumB = inputNums()

    main(inputNumA, inputNumB)
