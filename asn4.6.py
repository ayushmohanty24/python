"""
Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
"""



hours=input('hours:')
rate=input('rate:')
h=float(hours)
r=float(rate)

def computepay(h, r):
    if h<40 :
        return h*r
    overtime = h - 40.0               
    return (r * 40.0) + (1.5 * r * overtime) 

p = computepay(h,r)
print("Pay", p)
