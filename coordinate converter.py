# converts hours, minutes and seconds to decimal degrees.

def hms2dec(h, m, s):
    dec = 15 * (h+m/60+s/(60*60))

    return dec

# converts degrees, minutes, and seconds to decimal degrees.

def dms2dec(d, m, s):
    # analyse for negative values before conversion .
    
    if d > 0:
        dec = (d+m/60+s/(60*60))
        
    else:
        dec = -1*((-1*d)+m/60+s/(60*60))
        
    return dec
