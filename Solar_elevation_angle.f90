program Solar_elevation_angle
use Solar_hour_angle
use Declination_angle

implicit none
integer :: tz,day
real :: time,lon,ang

tz=8
day=365
lon=114.062996
time=10.53
call cal_ang(lon,day,time,tz,ang)
print*, ang

call day_ang(day,ang)
print*,ang
end program Solar_elevation_angle
