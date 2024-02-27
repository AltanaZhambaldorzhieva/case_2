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
    total_time_min += dock_dis / (spd_perry / 60)
    total_time_min += shark_time
    total_time_min += turn_rnd_dis / (spd_bike / 60)
    total_time_hrs = total_time_min / 60
    hours_time = total_time_min // 60
    minutes_time = total_time_min % 60
    finish_min = int((minutes + total_time_min) % 60)
    finish_hrs = int((hours + ((minutes + total_time_min)//60))%24)

    print(f'{ru.TOTAL_TIME} {int(hours_time)} {ru.HOUR}, {int(minutes_time)} {ru.MINUTES}')
    print(f'{ru.TIME_IN_MINUTES} {int(total_time_min)} {ru.MINUTES}')
    print(f'{ru.TIME_IN_HOURS} {total_time_hrs} {ru.HOURS}')
    print(f'{ru.FINISH_TIME} {finish_hrs}{ru.SPLIT}{finish_min}')

if __name__ == '__main__':
    main()
