package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	b, err := os.Open("./input.txt")
	if err != nil {
		log.Fatalln(err)
	}

	defer b.Close()
	total := 0
	scanner := bufio.NewScanner(b)
	for scanner.Scan() {
		row := scanner.Text()
		num, err := strconv.Atoi(row)
		if err != nil {
			log.Fatalln(err)
		}
		total += num
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Println(total)

}
