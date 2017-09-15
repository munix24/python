#http://www.investopedia.com/university/movingaverage/movingaverages1.asp
#https://en.wikipedia.org/wiki/Moving_average

def average(data):
    '''return the average of a list of numbers'''
    return sum(data) / len(data)

def moving_average(data, period):
    '''return the moving_average for a list of numbers and period'''
    if period > len(data) or len(data) < 1:
        return 0
    period -= 1
    
    ma = {}
    for i in range(period, len(data)):
        ma[i] = average(data[i - period : i + 1])

    return ma

def EMA(data, alpha):
    '''return the exmponential moving average of a list of numbers with factor "alpha"'''
    if not data:
        return 0
    if len(data) == 1:
        return data[0]
    else:
        return alpha * data[-1] + (1 - alpha) * EMA(data[:-1], alpha)

def moving_exponential_moving_average(data, period, alpha):
    '''
	return the moving_exponential_moving_average for a list of numbers, period, and alpha.
	
	The exponential moving average is a type of moving average that gives more weight to recent prices in an attempt to make it more responsive to new information
	'''
    if period > len(data) or len(data) < 1:
        return 0
    period -= 1
    
    ema = {}
    for i in range(period, len(data)):
        ema[i] = EMA(data[i - period : i + 1], alpha)

    return ema

data = [7, 8, 9, 10, 9, 8, 7, 9, 11, 13, 15, 17,
        16, 15, 14, 13, 12, 11, 10, 9, 7, 5, 3, 1]
period = 3
##alpha = 2 / (1 + period)
alpha = .6

##print(moving_average(data, period))
##print(moving_exponential_moving_average(data, period, alpha))

