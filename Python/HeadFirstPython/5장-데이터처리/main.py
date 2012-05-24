
def sanitize ( time_string ):    
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return ( time_string )
        
    ( mins, secs ) = time_string.split( splitter )
    return ( mins + '.' + secs )

def ProcessAndOutput ( fileName ):
    try:
        with open( fileName ) as file:
            data = file.readline()
        rec = data.strip().split(',')
        recTidy = sorted( set( [ sanitize( t ) for t in rec ] ) )
        print( recTidy[0:3] )
    except IOError as ioerr:
        print( 'File error: ' + str( ioerr ) )
        return ( None )

ProcessAndOutput ( 'data/james.txt' )
ProcessAndOutput ( 'data/julie.txt' )
ProcessAndOutput ( 'data/mikey.txt' )
ProcessAndOutput ( 'data/sarah.txt' )
