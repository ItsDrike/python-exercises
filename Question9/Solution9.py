def get_input():
    tests = []

    # Get int test amount
    test_amt = int(input('Enter amount of tests to be run: '))

    # For every test #x
    for x in range(test_amt):
        # Get cars amount in this test (int)
        cars_amt = int(input(f'Enter amount of cars for test #{x + 1}: '))
        # Add new empty list to tests list (for this new test case)
        tests.append([])
        # Get every car number
        for y in range(cars_amt):
            # Get car number
            car_number = int(
                input(f'(Test#{x + 1})Enter car number for position #{y + 1}: '))
            # Add car number to list for current test
            tests[x].append(car_number)
        # Reverse test order (last car entered (bottom car) is first car to go)
        tests[x] = tests[x][::-1]
    return tests


def car_can_go(car, arrived_cars):
    '''Check if given car can arrive in given list

    Arguments:
        car {int} -- Car index
        arrived_cars {list} -- List of cars which has already arrived

    Returns:
        bool -- Can car arrive
    '''
    # Check if some cars has already arrived
    if arrived_cars:
        # Set expected car to be the last arrived car + 1
        expected_car = arrived_cars[-1] + 1
    else:
        # Set expected car to 1 (no cars has arrived yet)
        expected_car = 1

    if expected_car == car:
        return True
    else:
        return False


def analyze_test(mountain_top, branch=[], lake=[]):
    '''Check if cars in this test case can make it to the lake

    Arguments:
        mountain_top {list} -- Starting cars (on the mountain top)

    Keyword Arguments:
        branch {list} -- Cars in the branch (default: {[]})
        lake {list} -- Cars in the lake (arrived cars) (default: {[]})
    '''

    # Create copy of mountain_top to loop over every car (syntax for that is list[:])
    # (removing elements from list while looping is dangerous, hence create a copy)
    for car in mountain_top[:]:
        # Test if car can go to the lake
        if car_can_go(car, lake):
            # Add car to the lake and remove it from mountain_top
            lake.append(car)
            mountain_top.pop(0)
        # If car can't go to the lake and branch is not empty
        elif branch:
            # Create copy of branch to loop over every car in it
            for branch_car in branch[:]:
                if car_can_go(branch_car, lake):
                    # Add branch car to the lake and remove it from branch
                    lake.append(branch_car)
                    branch.pop(0)
                # No more cars from the branch can go
                else:
                    # If first car from branch failed to go to lake
                    if branch_car == branch[0]:
                        # mountain_top cars can't go, neither can the branch cars
                        # Add car from the mountain_top to the start of branch list and remove it from mountain_top
                        branch.insert(0, car)
                        mountain_top.pop(0)
                    # Repeat test for the car that failed before
                    return analyze_test(mountain_top, branch, lake)
        # Branch is empty and car can't go to the lake
        else:
            # Add car to the branch and remove it from mountain_top
            branch.append(car)
            mountain_top.pop(0)
    # Create copy of branch to loop over remaining cars
    for branch_car in branch[:]:
        # Test if car from branch can go to the lake
        if car_can_go(branch_car, lake):
            # Add car from branch to the lake (and remove it from branch)
            lake.append(branch_car)
            branch.pop(0)
        # Car can't arrive to the lake, stuck in branch -> FALSE
        else:
            return False
    return True


tests = get_input()

# Loop through every test
for test in tests:
    # Analyze test and save it to test_result
    test_result = analyze_test(test)
    # print result
    if test_result:
        print('Y')
    else:
        print('N')
