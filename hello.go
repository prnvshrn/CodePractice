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
}