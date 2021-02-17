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

func outfc(path string) {
	frame, err := ioutil.ReadFile(path)
	if err != nil {
		panic(err);
	}
	//fmt.Print("\033[2J")
	fmt.Print("\033[0;0H")
	var i int = 0
	var rnum int
	var gnum int
	var bnum int
	for _, c := range string(frame) {
		chr := string(c)
		if chr == "\n" {
			fmt.Print("\n")
		} else {
			if i == 0 {
				outn,_ := strconv.ParseInt(chr, 16, 64)
				rnum += 16*int(outn)
			} else if i == 1 {
				outn,_ := strconv.ParseInt(chr, 16, 64)
				rnum += int(outn)
			} else if i == 2 {
				outn,_ := strconv.ParseInt(chr, 16, 64)
				gnum += 16*int(outn)
			} else if i == 3 {
				outn,_ := strconv.ParseInt(chr, 16, 64)
				gnum += int(outn)
			} else if i == 4 {
				outn,_ := strconv.ParseInt(chr, 16, 64)
				bnum += 16*int(outn)
			} else {
				outn,_ := strconv.ParseInt(chr, 16, 64)
				bnum += int(outn)
				fmt.Printf("\033[38;2;%d;%d;%dm%s",rnum, gnum, bnum, "█");
				rnum = 0
				gnum = 0
				bnum = 0
			}
			i = (i+1)%6
		}
	}
}

func main() {
	dpath := os.Args[2]
	fps, _ := strconv.Atoi(os.Args[1])
	files, err := filepath.Glob(filepath.Join(dpath, "*.frm"))
	color, _ := strconv.Atoi(os.Args[3])
	if err != nil {
		log.Fatal(err)
	}
	sort.Sort(list_sort(files))
	tempc := make(chan bool)
	stopt := time.Second/time.Duration(fps)
	stopc := time.Duration(0)
	if color == 1 {
		for _, f := range files {
			go func(){
				outfc(f)
				tempc <- true
			}()
			t := time.Now()
			select {
				case <- tempc :
					time.Sleep(stopt - time.Now().Sub(t))
					stopc = 0
				case <- time.After(stopt - stopc):
					stopc = stopt - time.Now().Sub(t)
			}
		}
	} else {
		for _, f := range files {
			outf(f)
			time.Sleep(time.Second/time.Duration(fps))
		}
	}
	
}
