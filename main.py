from interval import parse_input, merge_intervals, print_intervals

if __name__ == '__main__':
    res = parse_input("1-5, 2-10")
    print(print_intervals(merge_intervals(res)))

