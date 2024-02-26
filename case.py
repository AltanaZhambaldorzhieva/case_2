# Case_2
# Developers: Zhambaldorzhieva A., Zaytseva D., Ryaguzova D., Makarenko K.
#

import ru_local as ru

def main():
    '''
    Main function.
    :return: None
    '''

    spd_perry = 10
    spd_bike = 60
    grandma_dis = 0.5
    dock_dis = 10
    shark_time = 15
    turn_rnd_dis = 5

    start_time = input(ru.START_TIME)
    hours, minutes = map(int, start_time.split(":"))

    total_time_min = 0
    total_time_min += grandma_dis / (spd_perry / 60)
    total_time_min += dock_dis / spd_perry * 60
    total_time_min += shark_time
    total_time_min += turn_rnd_dis / (spd_bike / 60)

if __name__ == '__main__':
    main()
