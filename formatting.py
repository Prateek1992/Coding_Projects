for i in range(1, 13):
    print("No {0:2} squared is {1:3} and cube is {2:4}.".format(i, i ** 2, i ** 3))  # use : for field width

print()
# changing alignment usin <,>,^
for i in range(1, 13):
    print("No {0:2} squared is {1:<3} and cube is {2:^4}.".format(i, i ** 2, i ** 3))


print("Pi is approximately {0:12.50f}".format(22 / 7))  # precision  superseded field width
