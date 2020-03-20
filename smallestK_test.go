package leetcode

import (
	"fmt"
	"sort"
	"testing"
)

func smallestK(arr []int, k int) []int {
	sort.Ints(arr)
	return arr[:k]
}

func Test_SamllestK(t *testing.T) {
	arr := []int{1,2,6455,7,43,232,2020}
	fmt.Println(smallestK(arr, 3))
}