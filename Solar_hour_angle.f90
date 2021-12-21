module Solar_hour_angle
implicit none

contains 
  subroutine cal_ang(lon,day,time,tz,ang) 
    real :: lon,time,rad,eot,offset,lst
    integer :: day,tz
    real :: ang

    rad=2*3.14159/365*(day-1+(time-12)/24)
    eot=229.18*(0.000075+0.001868*cos(rad)-0.032077*sin(rad)-0.014615*cos(2*rad)-0.040849*sin(2*rad))
    offset=eot+4*(lon-15*tz)
    lst=time+offset/60
    ang=15*(lst-12)
  end subroutine cal_ang

end module Solar_hour_angle
