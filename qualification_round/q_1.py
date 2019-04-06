def main():
    number_of_test_cases = int(input())

    for case_id in range(1, number_of_test_cases + 1):
        jamcoins = int(input())

        if jamcoins == 4:
            print("Case #{}: {} {}".format(case_id, 2, 2))

        else:
            jamcoins_list = list(str(jamcoins))
            new_jamcoins_list = ["0"] * len(jamcoins_list)

            for jamcoins_index, jamcoins_number in enumerate(jamcoins_list):
                if jamcoins_number == "4":
                    jamcoins_list[jamcoins_index] = str(int(jamcoins_number) - 1)
                    new_jamcoins_list[jamcoins_index] = "1"

            print("Case #{}: {} {}".format(case_id, int("".join(jamcoins_list)), int("".join(new_jamcoins_list))))


if __name__ == '__main__':
    main()
