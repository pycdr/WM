package main

import (
	"fmt"
	"io/ioutil"
	"path/filepath"
	"os"
	"log"
	"time"
	"strconv"
	"sort"
)

type list_sort []string;
func (s list_sort) Len() int {
	return len(s)
}
func (s list_sort) Less(i, j int) bool {
	namei := filepath.Base(s[i])
	namej := filepath.Base(s[j])
	numi, erri := strconv.Atoi(namei[:len(namei)-4])
	if erri != nil {
		panic(erri);
	}
	numj, errj := strconv.Atoi(namej[:len(namej)-4])
	if erri != nil {
		panic(errj);
	}
	return numi < numj
}
func (s list_sort) Swap (i, j int) {
	s[i], s[j] = s[j], s[i]
}

func outf(path string) {
	frame, err := ioutil.ReadFile(path)
	if err != nil {
		panic(err);
	}
	fmt.Print("\033[2J")
	fmt.Print(string(frame))
}

func main() {
	dpath := os.Args[2]
	fps, _ := strconv.Atoi(os.Args[1])
	files, err := filepath.Glob(filepath.Join(dpath, "*.txt"))
	if err != nil {
		log.Fatal(err)
	}
	sort.Sort(list_sort(files))
	for _, f := range files {
		outf(f)
		time.Sleep(time.Second/time.Duration(fps))
	}
}
