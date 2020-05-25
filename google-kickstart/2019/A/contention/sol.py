import math
import numpy as np


def get_ints():
    return tuple(map(int, input().split()))


def should_move(booked, a, b):
    a_front_success = np.sum(~booked & a)
    b_front_success = np.sum(~booked & b)
    a_back_success = np.sum(~(booked | b) & a)
    b_back_success = np.sum(~(booked | a) & b)
    return min(b_front_success, a_back_success) > min(a_front_success,
                                                      b_back_success)


def calc_min_seats(seats, bookings):
    booked = np.zeros(seats, dtype=bool)
    max_success = math.inf
    for order in bookings:
        success = np.sum(~booked & order)
        max_success = min(max_success, success)
        booked |= order

    return max_success


def main(seats, num_bookings, bookings):
    # bubble sort bookings from start to end
    for i in range(num_bookings):
        j = 0
        booked = np.zeros(seats, dtype=bool)
        while j < num_bookings - i - 1:  # last i elements are sorted
            # if bookings[j] > bookings[j + 1]:
            if should_move(booked, bookings[j], bookings[j + 1]):
                bookings[j], bookings[j + 1] = bookings[j + 1], bookings[j]
            booked |= bookings[j]
            j += 1
        # print(calc_min_seats(seats, bookings))
    return calc_min_seats(seats, bookings)


T, = get_ints()
for i in range(T):
    seats, num_bookings = get_ints()
    bookings = []
    for j in range(num_bookings):
        L, R = get_ints()
        order = np.zeros(seats, dtype=bool)
        order[L - 1:R] = True
        bookings.append(order)
    ans = main(seats, num_bookings, bookings)
    print("Case #{}: {}".format(i + 1, ans))
