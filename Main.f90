Program Main

implicit none

integer                        :: u, i
real :: a(5,3), b(3,5),c(5,5)

! File unit
u = 10
! Open the file
open(unit=u, file='M.dat')
! Read data line by line
do i = 1,5
  read(u, *) a(i,1:3)
enddo
! Close the file
close(u)
! Display the values
do i=1,5
  write(*,*) a(i,1:3)
enddo

! File unit
u = 20
! Open the file
open(unit=u, file='N.dat')
! Read data line by line
do i = 1,3
  read(u, *) b(i,1:5)
enddo
! Close the file
close(u)
! Display the values
do i=1,3
  write(*,*) b(i,1:5)
enddo

call Matrix_multip(a,b,c)
open(unit=u, file='MN.dat', status='replace')
do i=1,5
 write(u, "(f9.2,f9.2,f9.2,f9.2,f9.2)") c(i,1:5)
enddo
close(u)
End Program Main
