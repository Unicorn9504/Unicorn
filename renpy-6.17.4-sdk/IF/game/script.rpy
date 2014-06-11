define e = Character('Eileen', color="#c8ffc8")

init python:
    #import ramdom 
    DAYS_PER_MONTH = 30
    WHETHER_RAIN = 0
    WHETHER_SNOW = 1
    WHETHER_CLOUDY = 2
    WHETHER_SUNNY = 3
    WHETHER_TYPHOON = 4
    WHETHER_THUNDER = 5
    WHETHER_MAX = 6
    SPRING = 0
    SUMMOR = 1
    AUTUMN = 2
    WINTER = 3
    SEASON_MAX = 4
    M_PI = 3.14159
    
    whether_temperature = [-4,-10,1,5,-5,-5]
    dist_spring = [0.20, 0.00, 0.40, 0.35, 0.00, 0.05]
    dist_summor = [0.15, 0.00, 0.20, 0.50, 0.05, 0.10]
    dist_autumn = [0.10, 0.00, 0.25, 0.60, 0.00, 0.05]
    dist_winter = [0.10, 0.10, 0.30, 0.50, 0.00, 0.00]

    def rarray(arr, size):
        r = random.random();
        result = -1;
        for i in range(size):
            r -= arr(i);
            if(r <= 0.0):
                return i
        return result

    def whether(x):
        season = x / DAYS_PER_MONTH;
        if(season == SPRING):
            return rarray(dist_spring, WHETHER_MAX)
        elif(season == SUMMOR):
            return rarray(dist_summor, WHETHER_MAX)
        elif(season == AUTUMN):
            return rarray(dist_autumn, WHETHER_MAX)
        elif(season == WINTER):
            return rarray(dist_winter, WHETHER_MAX)
        else:
            return -1
            
    def year(x, base, yearLambda):
        return base + yearLambda*sin( x / (DAYS_PER_MONTH * 4.0) * 2.0 * M_PI)
        
    def month(x, baseYear, baseMonth , lambdaYear, lambdaMonth):
        return baseMonth + lambdaMonth * year(x,baseYear,lambdaYear)

    def day (x, whe, baseYear, baseMonth, lambdaYear, lambdaMonth):
        return month(x, baseYear, baseMonth, lambdaYear, lambdaMonth) + whether_temperature(whe)
        


 
#GameS Start
label start:
    e "Loop Start"
    $ loop_cnt = 1
label loop:    
    e "show pref: [loop_cnt]" 
    call screen firm
    $ loop_cnt += 1
    e "pref end"
    jump loop

    return
