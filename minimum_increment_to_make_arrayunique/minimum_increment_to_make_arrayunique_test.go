package minimum_increment_to_make_arrayunique

import (
	"fmt"
	"sort"
	"testing"
)

func minIncrementForUnique(A []int) int {
	sort.Ints(A)
	res := 0
	for i := 0 ; i < len(A)-1 ; i++{
		curr := i
		next := i+1
		if A[curr] >= A[next]{
			temp := A[next]
			A[next] = A[curr]+1
			res += A[next] - temp
		}
	}
	return res
}

func Test_minIncrementForUnique(t *testing.T){
	var A = []int{1,2,2}
	if minIncrementForUnique(A) != 1{
		t.Fail()
	}
	A = []int{3,2,1,2,1,7}
	if minIncrementForUnique(A) != 6{
		t.Fail()
	}
	fmt.Println("test")
}