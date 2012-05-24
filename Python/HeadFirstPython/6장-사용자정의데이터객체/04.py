# 이름, 생일, 데이터를 클래스에 담아서 출력한다.
# 클래스에 새로운 멤버함수를 추가한다.

#-------------------------------------------------------------------------------
def sanitize( time_string ):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return ( time_string )

    ( mins, secs ) = time_string.split( splitter )

    return ( mins + '.' + secs )

#-------------------------------------------------------------------------------
class Athlete:
    def __init__ ( self, name, dob=None, times=[] ) :
        self.name = name
        self.dob = dob
        self.times = times

    def top3 ( self ) :
        return sorted(set([sanitize(t) for t in self.times]))[0:3]

    def addTime ( self, time ) :
        self.times.append( time )

    def addTimes ( self, times ) :
        self.times.extend( times )

#-------------------------------------------------------------------------------
def get_coach_data ( filename ):
    try:
        with open ( filename ) as f:
            data = f.readline()

        templ = data.strip().split( ',' )

        return ( Athlete( templ.pop(0),
                          templ.pop(0),
                          templ ) )

    except IOError as ioerr:
        print ( 'File error: ' + str( ioerr ) )

        return ( None )

#-------------------------------------------------------------------------------

james = get_coach_data ( 'data\james2.txt' )
julie = get_coach_data ( 'data\julie2.txt' )
mikey = get_coach_data ( 'data\mikey2.txt' )
sarah = get_coach_data ( 'data\sarah2.txt' )

print( james.name + "'s fastest times are: " + str( james.top3() ) )
print( julie.name + "'s fastest times are: " + str( julie.top3() ) )
print( mikey.name + "'s fastest times are: " + str( mikey.top3() ) )
print( sarah.name + "'s fastest times are: " + str( sarah.top3() ) )

james.addTime( '1-1' )
james.addTimes( ['1.2', '1:3'] )
julie.addTime( '1-1' )
julie.addTimes( ['1.2', '1:3'] )
mikey.addTime( '1-1' )
mikey.addTimes( ['1.2', '1:3'] )
sarah.addTime( '1-1' )
sarah.addTimes( ['1.2', '1:3'] )

print( '===== Affter Add =====' )
print( james.name + "'s fastest times are: " + str( james.top3() ) )
print( julie.name + "'s fastest times are: " + str( julie.top3() ) )
print( mikey.name + "'s fastest times are: " + str( mikey.top3() ) )
print( sarah.name + "'s fastest times are: " + str( sarah.top3() ) )
