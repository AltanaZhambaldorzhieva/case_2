# Case_2
# Developers: Zhambaldorzhieva A., Zaytseva D., Ryaguzova D., Makarenko K.
#

import ru_local as ru


def main():
    """
    Main function.
    :return: None
    """

    spd_perry = 10
    spd_bike = 60
    grandma_dis = 0.005
    dock_dis = 10
    river_dis_1 = 10
    shark_time = 0.25
    turn_rnd_dis = 5
    spd_strm = 5
    river_dis_2 = 10

    start_time = input(ru.START_TIME)
    hours, minutes = map(int, start_time.split(":"))

    total_time_hour = 0
    total_time_hour += grandma_dis / spd_perry
    total_time_hour += dock_dis / spd_perry
    total_time_hour += river_dis_1 / (spd_bike + spd_strm)
    total_time_hour += shark_time
    total_time_hour += turn_rnd_dis / (spd_bike - spd_strm)
    total_time_hour += river_dis_2 / (spd_bike + spd_strm)

    total_time_min = int(total_time_hour * 60)
    hours_time = int(total_time_hour)
    minutes_time = int((total_time_hour - hours_time) * 60)

    finish_hrs = hours + hours_time
    finish_min = minutes + minutes_time
    if finish_min >= 60:
        finish_min -= 60
        finish_hrs += 1

    print(f'{ru.TOTAL_TIME} : {total_time_min} {ru.MINUTES}')
    print(f'{ru.FINISH_TIME} {finish_hrs}:{finish_min}')


if __name__ == '__main__':
    main()
