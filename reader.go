package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
	"time"
)

type list_sort []string

func (s list_sort) Len() int { return len(s) }
func (s list_sort) Less(i, j int) bool {
	ni, _ := strconv.Atoi(strings.TrimSuffix(filepath.Base(s[i]), ".frm"))
	nj, _ := strconv.Atoi(strings.TrimSuffix(filepath.Base(s[j]), ".frm"))
	return ni < nj
}
func (s list_sort) Swap(i, j int) { s[i], s[j] = s[j], s[i] }

func main() {
	if len(os.Args) < 4 {
		fmt.Fprintln(os.Stderr, "Usage: reader <fps> <output_dir> <color_flag>")
		os.Exit(1)
	}

	fps, _ := strconv.Atoi(os.Args[1])
	outputDir := os.Args[2]
	color, _ := strconv.Atoi(os.Args[3])

	files, err := filepath.Glob(filepath.Join(outputDir, "*.frm"))
	if err != nil {
		fmt.Fprintln(os.Stderr, "Glob error:", err)
		os.Exit(1)
	}
	sort.Sort(list_sort(files))

	if len(files) == 0 {
		fmt.Fprintln(os.Stderr, "No .frm files found in", outputDir)
		os.Exit(1)
	}

	frameDelay := time.Second / time.Duration(fps)

	for _, f := range files {
		start := time.Now()

		if color == 1 {
			// Use 'cat' for faster colored output
			cmd := exec.Command("cat", f)
			cmd.Stdout = os.Stdout
			cmd.Run()
			// Reset color and move cursor to top-left
			fmt.Print("\033[0m\033[;H")
		} else {
			// For monochrome, clear screen and print
			data, err := os.ReadFile(f)
			if err != nil {
				continue
			}
			fmt.Print("\033[2J\033[H")
			fmt.Print(string(data))
		}

		elapsed := time.Since(start)
		remaining := frameDelay - elapsed
		if remaining > 0 {
			time.Sleep(remaining)
		}
	}
}
