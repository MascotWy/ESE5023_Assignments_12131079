module Declination_angle
implicit none

contains 
  subroutine day_ang(day,ang)
    integer :: day
    real :: day2,ang
    day2=real(day)
    ang=-23.44*cos((day2+10)*360/365)
  end subroutine day_ang

end module Declination_angle
