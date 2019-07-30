package main
import "fmt"
func add(x int, y int) int {
	return x + y
}
func swap(x, y string) (string, string) {
	return y, x
}
func main(){
	fmt.Println(add(1,5))
	fmt.Println(swap("Pranav","Sharan"))
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
}