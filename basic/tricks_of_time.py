import time
ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)


#Date arithmetic is easy to do with ticks. However, dates before the epoch cannot be
#represented in this form. Dates in the far future also cannot be represented this way - the
#cutoff point is sometime in 2038 for UNIX and Windows
