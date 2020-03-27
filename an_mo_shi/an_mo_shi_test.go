package an_mo_shi

import (
	"testing"
)

func massage(nums []int) int {
	if len(nums) < 3 {
		return max(nums[0], nums[1])
	}
	f, s := nums[0], nums[1]
	var t int
	for i, v := range nums {
		if i < 2 {
			continue
		}
		t = max(f+v, s)
		f = max(f, s)
		s = t
	}
	return t
}

func max(i, j int) int {
	if i > j {
		return i
	} else {
		return j
	}
}

func Test_massage(t *testing.T) {

	if massage([]int{1, 2, 3, 1}) != 4 {
		t.Error("err")
	}

	if massage([]int{2, 7, 9, 3, 1}) != 12 {
		t.Error("err")
	}

	if massage([]int{2, 1, 4, 5, 3, 1, 1, 3}) != 12 {
		t.Error("err")
	}
}
