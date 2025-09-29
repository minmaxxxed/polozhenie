package phfilter

import (
	"image"
)

type Request struct {
	Img image.Image
	//blurRadius int
	FontPath string
	Text     string
}
