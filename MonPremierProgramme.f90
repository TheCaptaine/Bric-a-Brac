program zero
  implicit none
  real :: x, y, tol
  integer :: i=1
  integer :: j
  integer, dimension(5) :: tab = (/(j, j=1,5)/)
  x = 5
  tol = 0.01
  do
     call funct(x, y, tab)
     if (abs((y-x)/x) <= tol) then
        exit
     else
        x=y
     i = i + 1
     end if
  end do
  print*, 'La solution est ', y
  do i=1,5
     print*, tab(i)
  end do
  
contains
  subroutine funct(x, y, tab)
    implicit none
    real, intent(in) :: x
    real, intent(out) :: y
    integer, dimension(5), intent(out) :: tab
    y=x-(x-exp(-x))/(1+exp(-x))
    tab(i) = y
  end subroutine funct
  
end program zero


