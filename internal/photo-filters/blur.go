package phfilter

import (
	"image"
	"log"
)

type BlurFilter struct {
	init bool
}

func NewBlurFilter() *BlurFilter {
	return &BlurFilter{true}
}

func (f *BlurFilter) Process(request Request) (image.Image, error) {

	log.Print("Proccess_moc... blur filter inited: ", f.init)
	return request.Img, nil
}
