def read_log(l):
    x = []
    y = []
    
    f = open("/home/pi/solar_automa/stats/log", "r")
    lines = f.read().splitlines()
    f.close()
        
    split_lines = []
    for line in lines:
        split_lines.append(line.split("|"))
    
    #list of splited => [[time1, val1], [time2, val2], [time3, val3]]

    date_time=[]
    v_pv=[]
    i_pv=[]
    p_pv=[]
    v_bat=[]
    i_load=[]
    p_load=[]

    for line in split_lines:
        date_time.append(line[0])
        v_pv.append(line[1])
        i_pv.append(line[2])
        p_pv.append(line[3])
        v_bat.append(line[4])
        i_load.append(line[5])
        p_load.append(line[6])
    
    #extract splitted lis to seperate lis => x=[time1, time2, time3]

    x_date_time = []
    y_v_pv = []
    y_i_pv = []
    y_p_pv = []
    y_v_bat = []
    y_i_load = []
    y_p_load = []
    for i in range(l):
        try:
            if l <= 1440:
                x_date_time.append((date_time.pop())[11:16])
            else:
                x_date_time.append(date_time.pop())
                
            y_v_pv.append(v_pv.pop())
            y_i_pv.append(i_pv.pop())
            y_p_pv.append(p_pv.pop())
            y_v_bat.append(v_bat.pop())
            y_i_load.append(i_load.pop())
            y_p_load.append(p_load.pop())
        except:
            break
    x_date_time.reverse()
    y_v_pv.reverse()
    y_i_pv.reverse()
    y_p_pv.reverse()
    y_v_bat.reverse()
    y_i_load.reverse()
    y_p_load.reverse()

    return {
        'date_time':x_date_time,
        'v_pv':y_v_pv,
        'i_pv':y_i_pv,
        'p_pv':y_p_pv,
        'v_bat':y_v_bat,
        'i_load':y_i_load,
        'p_load':y_p_load }
