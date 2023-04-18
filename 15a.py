from collections import namedtuple
Coordinate = namedtuple('Point', ['x', 'y'])

def manhattan_distance(sensor, beacon):
    return abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)

def extract_sensor(line):
    # convert string "Sensor at x=2, y=18" to tuple (2, 18)
    line = line.replace("Sensor at ", "")
    line = line.replace(",", "")
    xs = [words for words in line.split(" ") if words.startswith("x=")][0]
    ys = [words for words in line.split(" ") if words.startswith("y=")][0]
    x = int(xs.replace("x=", ""))
    y = int(ys.replace("y=", ""))
    return Coordinate(x,y)

def extract_beacon(line):
    # convert string "Closest beacon is at x=2, y=18" to tuple (2, 18)
    line = line.replace("Closest beacon is at ", "")
    line = line.replace(",", "")
    xs = [words for words in line.split(" ") if words.startswith("x=")][0]
    ys = [words for words in line.split(" ") if words.startswith("y=")][0]
    x = int(xs.replace("x=", ""))
    y = int(ys.replace("y=", ""))
    return Coordinate(x,y)

sensor_number=1
def block_out_impossible_coords_on_row(taxi_distance: int, y_value: int, sensor_coord: Coordinate, beacon_coord: Coordinate) -> set:
    global sensor_number

    print(f" checking sensor #{sensor_number} {sensor_coord} and beacon {beacon_coord} distance = {taxi_distance}")
    sensor_number += 1

    # does this sensor have an exclusion zone in the y-space we care about?
    number_of_x = set()

    # Calc lowest Y
    this_min = sensor_coord.y - taxi_distance
    # Calc highest Y
    this_max = sensor_coord.y + taxi_distance

    # Are we in the Y-space we care about?
    if this_min <= y_value <= this_max:

        y_diff = abs(sensor_coord.y - y_value)
        x_range = taxi_distance - y_diff

        # print(f"y_diff is {y_diff}, taxi_distance is {taxi_distance}, x_range is {x_range}")

        start_x = sensor_coord.x - x_range
        stop_x  = sensor_coord.x + x_range

        if start_x > stop_x:
            start_x, stop_x = stop_x, start_x

        print(f"Blocking out between {start_x} and {stop_x}")

        # Loop over X-axis for this y-value
        # x_value = taxi_distance - abs(y_value)
        for x in range(start_x, stop_x + 1):
            number_of_x.add(Coordinate(x, y_value))

    # Remove the beacon coord
    if beacon_coord in number_of_x:
        number_of_x.remove(beacon_coord)
    
    # if len(number_of_x) > 0:
    #     print(f"  No-beacon area: {number_of_x} length:{len(number_of_x)}")
    return number_of_x

def place_sensors_and_beacons(data):
    total_empty_area = set()
    y_we_care_about=2000000

    for line in data.split("\n"):
        parts = line.split(":")
        sensor = extract_sensor(parts[0])
        beacon = extract_beacon(parts[1])

        distance = manhattan_distance(sensor, beacon)
        non_beacon_area = block_out_impossible_coords_on_row(distance, y_we_care_about, sensor, beacon)
        total_empty_area = total_empty_area.union(non_beacon_area)

    print(f"There are {len(total_empty_area)} positions that cannot have a beacon present.")


data = open("input-15.txt").read().strip()
place_sensors_and_beacons(data)
