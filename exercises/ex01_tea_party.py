"""Program to help plan a cozy tea party!"""

__author__: str = "730476994"


def main_planner(guests: int) -> None:
    """Calls each function and produces a printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Compute the number of tea bags needed"""
    return 2 * people


def treats(people: int) -> int:
    """Computes the number of treats needed"""
    return int((tea_bags(people=people)) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of the tea bags and treats combined"""
    return (0.5 * tea_count) + (0.75 * treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
