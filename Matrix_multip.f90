subroutine Matrix_multip(a,b,c)
implicit none
integer :: i
real    :: a(5,3),b(3,5),c(5,5)
c=matmul(a,b)

end
