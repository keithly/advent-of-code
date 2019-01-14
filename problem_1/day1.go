package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func partOne() (int, []int) {
	b, err := os.Open("./input.txt")
	if err != nil {
		log.Fatalln(err)
	}

	defer b.Close()
	total := 0
	var data []int
	scanner := bufio.NewScanner(b)
	for scanner.Scan() {
		row := scanner.Text()
		num, err := strconv.Atoi(row)
		if err != nil {
			log.Fatalln(err)
		}
		data = append(data, num)
		total += num
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return total, data
}

func partTwo(input []int) int {
	currentFreq := 0
	value := 0
	freqs := map[int]bool{}
	for i := 0; freqs[value] == false; i = (i + 1) % len(input) {
		freqs[value] = true
		currentFreq = input[i]
		value = value + currentFreq
	}
	return value
}

func main() {
	total, data := partOne()
	fmt.Println(total)
	fmt.Println(partTwo(data))
}
