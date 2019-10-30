# Goldman Sac Interview Question -> Given time "xx:xx" find angle between minute and hour hand


def angle(time):
	hour = 0
	minute = 0
	hour_angle = 0
	minute_angle = 0
	if len(time) == 5:
		hour = int(time[0:1])
		minute = int(time[3:5])
	else:
		hour = int(time[0])
		minute = int(time[2:4])
	# compute the angles from 0 to minute hand and hour hand
	# minute hand first
	print(hour)
	print(minute)
	minute_angle = minute/60.0 * 360.0
	hour_angle = hour/12.0 * 360.0 + 30.0*minute/60.0
	return abs(minute_angle-hour_angle)


